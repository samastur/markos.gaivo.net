#!/bin/bash

wp2pelican --wpfile -o old_posts wordpress.2015-03-02.xml --wpposts dump/posts/ -m markdown
mv old_posts/* articles/content/
rmdir old_posts
