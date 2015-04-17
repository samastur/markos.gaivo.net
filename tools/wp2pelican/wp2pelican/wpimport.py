#!/usr/bin/env python

# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import argparse
try:
    from html import unescape  # py3.4+
except ImportError:
    from six.moves.html_parser import HTMLParser
    unescape = HTMLParser().unescape
import os
import re
import subprocess
import sys
import time
import logging

from codecs import open
from six.moves.urllib.error import URLError
from six.moves.urllib.parse import urlparse
from six.moves.urllib.request import urlretrieve

# pelican.log has to be the first pelican module to be loaded
# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init
from pelican.utils import slugify

logger = logging.getLogger(__name__)


def decode_wp_content(content, br=True):
    pre_tags = {}
    if content.strip() == "":
        return ""

    content += "\n"
    if "<pre" in content:
        pre_parts = content.split("</pre>")
        last_pre = pre_parts.pop()
        content = ""
        pre_index = 0

        for pre_part in pre_parts:
            start = pre_part.find("<pre")
            if start == -1:
                content = content + pre_part
                continue
            name = "<pre wp-pre-tag-{0}></pre>".format(pre_index)
            pre_tags[name] = pre_part[start:] + "</pre>"
            content = content + pre_part[0:start] + name
            pre_index += 1
        content = content + last_pre

    content = re.sub(r'<br />\s*<br />', "\n\n", content)
    allblocks = ('(?:table|thead|tfoot|caption|col|colgroup|tbody|tr|'
                 'td|th|div|dl|dd|dt|ul|ol|li|pre|select|option|form|'
                 'map|area|blockquote|address|math|style|p|h[1-6]|hr|'
                 'fieldset|noscript|samp|legend|section|article|aside|'
                 'hgroup|header|footer|nav|figure|figcaption|details|'
                 'menu|summary)')
    content = re.sub(r'(<' + allblocks + r'[^>]*>)', "\n\\1", content)
    content = re.sub(r'(</' + allblocks + r'>)', "\\1\n\n", content)
    #    content = content.replace("\r\n", "\n")
    if "<object" in content:
        # no <p> inside object/embed
        content = re.sub(r'\s*<param([^>]*)>\s*', "<param\\1>", content)
        content = re.sub(r'\s*</embed>\s*', '</embed>', content)
        #    content = re.sub(r'/\n\n+/', '\n\n', content)
    pgraphs = filter(lambda s: s != "", re.split(r'\n\s*\n', content))
    content = ""
    for p in pgraphs:
        content = content + "<p>" + p.strip() + "</p>\n"
    # under certain strange conditions it could create a P of entirely whitespace
    content = re.sub(r'<p>\s*</p>', '', content)
    content = re.sub(r'<p>([^<]+)</(div|address|form)>', "<p>\\1</p></\\2>", content)
    # don't wrap tags
    content = re.sub(r'<p>\s*(</?' + allblocks + r'[^>]*>)\s*</p>', "\\1", content)
    #problem with nested lists
    content = re.sub(r'<p>(<li.*)</p>', "\\1", content)
    content = re.sub(r'<p><blockquote([^>]*)>', "<blockquote\\1><p>", content)
    content = content.replace('</blockquote></p>', '</p></blockquote>')
    content = re.sub(r'<p>\s*(</?' + allblocks + '[^>]*>)', "\\1", content)
    content = re.sub(r'(</?' + allblocks + '[^>]*>)\s*</p>', "\\1", content)
    if br:
        def _preserve_newline(match):
            return match.group(0).replace("\n", "<WPPreserveNewline />")
        content = re.sub(r'/<(script|style).*?<\/\\1>/s', _preserve_newline, content)
        # optionally make line breaks
        content = re.sub(r'(?<!<br />)\s*\n', "<br />\n", content)
        content = content.replace("<WPPreserveNewline />", "\n")
    content = re.sub(r'(</?' + allblocks + r'[^>]*>)\s*<br />', "\\1", content)
    content = re.sub(r'<br />(\s*</?(?:p|li|div|dl|dd|dt|th|pre|td|ul|ol)[^>]*>)', '\\1', content)
    content = re.sub(r'\n</p>', "</p>", content)

    if pre_tags:
        def _multi_replace(dic, string):
            pattern = r'|'.join(map(re.escape, dic.keys()))
            return re.sub(pattern, lambda m: dic[m.group()], string)
        content = _multi_replace(pre_tags, content)

    return content


def get_items(xml):
    """Opens a wordpress xml file and returns a list of items"""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        error = ('Missing dependency '
                 '"BeautifulSoup4" and "lxml" required to import Wordpress XML files.')
        sys.exit(error)
    with open(xml, encoding='utf-8') as infile:
        xmlfile = infile.read()
    soup = BeautifulSoup(xmlfile, "xml")
    items = soup.rss.channel.findAll('item')
    return items


def get_filename(filename, post_id):
    if filename is not None:
        return filename
    else:
        return post_id


def wp2fields(xml, wp_custpost=False):
    """Opens a wordpress XML file, and yield Pelican fields"""

    items = get_items(xml)
    for item in items:

        if item.find('status').string in ["publish", "draft"]:

            try:
                # Use HTMLParser due to issues with BeautifulSoup 3
                title = unescape(item.title.contents[0])
            except IndexError:
                title = 'No title [%s]' % item.find('post_name').string
                logger.warning('Post "%s" is lacking a proper title', title)

            filename = item.find('post_name').string
            post_id = item.find('post_id').string
            filename = get_filename(filename, post_id)

            content = item.find('encoded').string
            raw_date = item.find('post_date').string
            date_object = time.strptime(raw_date, "%Y-%m-%d %H:%M:%S")
            date = time.strftime("%Y-%m-%d %H:%M", date_object)
            author = item.find('creator').string

            categories = [cat.string for cat in item.findAll('category', {'domain': 'category'})]
            # caturl = [cat['nicename'] for cat in item.find(domain='category')]

            tags = [tag.string for tag in item.findAll('category', {'domain': 'post_tag'})]
            # To publish a post the status should be 'published'
            status = 'published' if item.find('status').string == "publish" else item.find('status').string

            kind = 'article'
            post_type = item.find('post_type').string
            if post_type == 'page':
                kind = 'page'
            elif wp_custpost:
                if post_type == 'post':
                    pass
                # Old behaviour was to name everything not a page as an article.
                # Theoretically all attachments have status == inherit so
                # no attachments should be here. But this statement is to
                # maintain existing behaviour in case that doesn't hold true.
                elif post_type == 'attachment':
                    pass
                else:
                    kind = post_type
            yield (title, content, filename, date, author, categories, tags, status,
                   kind, "wp-html")


def build_header(title, date, author, categories, tags, slug, status=None, attachments=None):
    from docutils.utils import column_width

    """Build a header from a list of fields"""
    header = '%s\n%s\n' % (title, '#' * column_width(title))
    if date:
        header += ':date: %s\n' % date
    if author:
        header += ':author: %s\n' % author
    if categories:
        header += ':category: %s\n' % ', '.join(categories)
    if tags:
        header += ':tags: %s\n' % ', '.join(tags)
    if slug:
        header += ':slug: %s\n' % slug
    if status:
        header += ':status: %s\n' % status
    if attachments:
        header += ':attachments: %s\n' % ', '.join(attachments)
    header += '\n'
    return header


def build_markdown_header(title, date, author, categories, tags, slug, status=None,
                          attachments=None):
    """Build a header from a list of fields"""
    header = 'Title: %s\n' % title
    if date:
        header += 'Date: %s\n' % date
    if author:
        header += 'Author: %s\n' % author
    if categories:
        header += 'Category: %s\n' % ', '.join(categories)
    if tags:
        header += 'Tags: %s\n' % ', '.join(tags)
    if slug:
        header += 'Slug: %s\n' % slug
    if status:
        header += 'Status: %s\n' % status
    if attachments:
        header += 'Attachments: %s\n' % ', '.join(attachments)
    header += '\n'
    return header


def get_ext(out_markup, in_markup='html'):
    if in_markup == 'markdown' or out_markup == 'markdown':
        ext = '.md'
    else:
        ext = '.rst'
    return ext


def get_out_filename(output_path, filename, ext, kind,
                     dirpage, dircat, categories, wp_custpost):
    filename = os.path.basename(filename)

    # Enforce filename restrictions for various filesystems at once; see
    # http://en.wikipedia.org/wiki/Filename#Reserved_characters_and_words
    # we do not need to filter words because an extension will be appended
    filename = re.sub(r'[<>:"/\\|?*^% ]', '-', filename)  # invalid chars
    filename = filename.lstrip('.')  # should not start with a dot
    if not filename:
        filename = '_'
    filename = filename[:249]  # allow for 5 extra characters

    out_filename = os.path.join(output_path, filename + ext)
    # option to put page posts in pages/ subdirectory
    if dirpage and kind == 'page':
        pages_dir = os.path.join(output_path, 'pages')
        if not os.path.isdir(pages_dir):
            os.mkdir(pages_dir)
        out_filename = os.path.join(pages_dir, filename + ext)
    elif not dirpage and kind == 'page':
        pass
    # option to put wp custom post types in directories with post type
    # names. Custom post types can also have categories so option to
    # create subdirectories with category names
    elif kind != 'article':
        if wp_custpost:
            typename = slugify(kind)
        else:
            typename = ''
            kind = 'article'
        if dircat and (len(categories) > 0):
            catname = slugify(categories[0])
        else:
            catname = ''
        out_filename = os.path.join(output_path, typename,
                                    catname, filename + ext)
        if not os.path.isdir(os.path.join(output_path, typename, catname)):
            os.makedirs(os.path.join(output_path, typename, catname))
    # option to put files in directories with categories names
    elif dircat and (len(categories) > 0):
        catname = slugify(categories[0])
        out_filename = os.path.join(output_path, catname, filename + ext)
        if not os.path.isdir(os.path.join(output_path, catname)):
            os.mkdir(os.path.join(output_path, catname))

    return out_filename


def get_attachments(xml):
    """returns a dictionary of posts that have attachments with a list
    of the attachment_urls
    """
    items = get_items(xml)
    names = {}
    attachments = []

    for item in items:
        kind = item.find('post_type').string
        filename = item.find('post_name').string
        post_id = item.find('post_id').string

        if kind == 'attachment':
            attachments.append((item.find('post_parent').string,
                               item.find('attachment_url').string))
        else:
            filename = get_filename(filename, post_id)
            names[post_id] = filename
    attachedposts = {}
    for parent, url in attachments:
        try:
            parent_name = names[parent]
        except KeyError:
            #attachment's parent is not a valid post
            parent_name = None

        try:
            attachedposts[parent_name].append(url)
        except KeyError:
            attachedposts[parent_name] = []
            attachedposts[parent_name].append(url)
    return attachedposts


def download_attachments(output_path, urls):
    """Downloads wordpress attachments and returns a list of paths to
    attachments that can be associated with a post (relative path to output
    directory). Files that fail to download, will not be added to posts"""
    locations = []
    for url in urls:
        path = urlparse(url).path
        #teardown path and rebuild to negate any errors with
        #os.path.join and leading /'s
        path = path.split('/')
        filename = path.pop(-1)
        localpath = ''
        for item in path:
            if sys.platform != 'win32' or ':' not in item:
                localpath = os.path.join(localpath, item)
        full_path = os.path.join(output_path, localpath)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        print('downloading {}'.format(filename))
        try:
            urlretrieve(url, os.path.join(full_path, filename))
            locations.append(os.path.join(localpath, filename))
        except (URLError, IOError) as e:
            #Python 2.7 throws an IOError rather Than URLError
            logger.warning("No file could be downloaded from %s\n%s", url, e)
    return locations


def fields2pelican(fields, out_markup, output_path,
                   dircat=False, strip_raw=False, disable_slugs=False,
                   dirpage=False, filename_template=None, filter_author=None,
                   wp_custpost=False, wp_attach=False, attachments=None):
    for (title, content, filename, date, author, categories, tags, status,
            kind, in_markup) in fields:
        if filter_author and filter_author != author:
            continue
        slug = not disable_slugs and filename or None

        if wp_attach and attachments:
            try:
                urls = attachments[filename]
                attached_files = download_attachments(output_path, urls)
            except KeyError:
                attached_files = None
        else:
            attached_files = None

        ext = get_ext(out_markup, in_markup)
        if ext == '.md':
            header = build_markdown_header(title, date, author, categories,
                                           tags, slug, status, attached_files)
        else:
            out_markup = "rst"
            header = build_header(title, date, author, categories,
                                  tags, slug, status, attached_files)

        out_filename = get_out_filename(output_path, filename, ext,
                                        kind, dirpage, dircat, categories, wp_custpost)
        print(out_filename)

        if in_markup in ("html", "wp-html"):
            html_filename = os.path.join(output_path, filename + '.html')

            with open(html_filename, 'w', encoding='utf-8') as fp:
                # Replace newlines with paragraphs wrapped with <p> so
                # HTML is valid before conversion
                if in_markup == "wp-html":
                    new_content = decode_wp_content(content)
                else:
                    paragraphs = content.splitlines()
                    paragraphs = ['<p>{0}</p>'.format(p) for p in paragraphs]
                    new_content = ''.join(paragraphs)

                fp.write(new_content)

            parse_raw = '--parse-raw' if not strip_raw else ''
            cmd = ('pandoc --normalize {0} --from=html'
                   ' --to={1} -o "{2}" "{3}"').format(parse_raw, out_markup,
                                                      out_filename, html_filename)

            try:
                rc = subprocess.call(cmd, shell=True)
                if rc < 0:
                    error = "Child was terminated by signal %d" % -rc
                    exit(error)

                elif rc > 0:
                    error = "Please, check your Pandoc installation."
                    exit(error)
            except OSError as e:
                error = "Pandoc execution failed: %s" % e
                exit(error)

            os.remove(html_filename)

            with open(out_filename, 'r', encoding='utf-8') as fs:
                content = fs.read()
                if out_markup == "markdown":
                    # In markdown, to insert a <br />, end a line with two or more spaces & then a end-of-line
                    content = content.replace("\\\n ", "  \n")
                    content = content.replace("\\\n", "  \n")

        with open(out_filename, 'w', encoding='utf-8') as fs:
            fs.write(header + content)
    if wp_attach and attachments and None in attachments:
        print("downloading attachments that don't have a parent post")
        urls = attachments[None]


def main():
    parser = argparse.ArgumentParser(
        description="Transform WordPress "
                    "files into reST (rst) or Markdown (md) files. Be sure to "
                    "have pandoc installed.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(dest='input', help='The input file to read')
    parser.add_argument(
        '--wpfile', action='store_true', dest='wpfile',
        help='Wordpress XML export')
    parser.add_argument(
        '-o', '--output', dest='output', default='output',
        help='Output path')
    parser.add_argument(
        '-m', '--markup', dest='markup', default='rst',
        help='Output markup format (supports rst & markdown)')
    parser.add_argument(
        '--dir-cat', action='store_true', dest='dircat',
        help='Put files in directories with categories name')
    parser.add_argument(
        '--dir-page', action='store_true', dest='dirpage',
        help=('Put files recognised as pages in "pages/" sub-directory'
              ' (wordpress import only)'))
    parser.add_argument(
        '--filter-author', dest='author',
        help='Import only post from the specified author')
    parser.add_argument(
        '--strip-raw', action='store_true', dest='strip_raw',
        help="Strip raw HTML code that can't be converted to "
             "markup such as flash embeds or iframes (wordpress import only)")
    parser.add_argument(
        '--wp-custpost', action='store_true',
        dest='wp_custpost',
        help='Put wordpress custom post types in directories. If used with '
             '--dir-cat option directories will be created as '
             '/post_type/category/ (wordpress import only)')
    parser.add_argument(
        '--wp-attach', action='store_true', dest='wp_attach',
        help='(wordpress import only) Download files uploaded to wordpress as '
             'attachments. Files will be added to posts as a list in the post '
             'header. All files will be downloaded, even if '
             "they aren't associated with a post. Files with be downloaded "
             'with their original path inside the output directory. '
             'e.g. output/wp-uploads/date/postname/file.jpg '
             '-- Requires an internet connection --')
    parser.add_argument(
        '--disable-slugs', action='store_true',
        dest='disable_slugs',
        help='Disable storing slugs from imported posts within output. '
             'With this disabled, your Pelican URLs may not be consistent '
             'with your original posts.')

    args = parser.parse_args()

    input_type = None
    if args.wpfile:
        input_type = 'wordpress'
    else:
        error = "You must provide either --wpfile"
        exit(error)

    if not os.path.exists(args.output):
        try:
            os.mkdir(args.output)
        except OSError:
            error = "Unable to create the output folder: " + args.output
            exit(error)

    if args.wp_attach and input_type != 'wordpress':
        error = "You must be importing a wordpress xml to use the --wp-attach option"
        exit(error)

    fields = wp2fields(args.input, args.wp_custpost or False)

    if args.wp_attach:
        attachments = get_attachments(args.input)
    else:
        attachments = None

    init()  # init logging

    fields2pelican(fields, args.markup, args.output,
                   dircat=args.dircat or False,
                   dirpage=args.dirpage or False,
                   strip_raw=args.strip_raw or False,
                   disable_slugs=args.disable_slugs or False,
                   filter_author=args.author,
                   wp_custpost=args.wp_custpost or False,
                   wp_attach=args.wp_attach or False,
                   attachments=attachments or None)
