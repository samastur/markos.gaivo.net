# -*- coding: utf-8 -*-
import appuifw
import e32
import e32dbm
import graphics
import sysinfo
import dir_iter
from key_codes import *
import camera
import socket
import os, os.path, sys
import httplib, urllib
import random
import string

e32.ao_yield()

SettingsDB = "d:\\mup.db"
ImageFile = "d:\\mup_photo.jpg"
Settings = None
db = None
mup = None
screenSize = (0,0)

MARELA_HOST = "www.marela.si"
MARELA_BASE_URL = "/as/rest/?methods=system.login,photo.uploadPhotos&rtype=javascript"

#
# Translation dictionary and function
#
trans = { u"Drive" : "Pogon",
		u"Select" : "Izberi",
		u"Remove" : "Odstrani",
		u"Sending image..." : "Pošiljam sliko...",
		u"Add tags" : "Dodaj oznake",
		u"Select used" : "Izberi uporabljene",
		u"Remove tags" : "Odstrani oznake",
		u"Send" : "Pošlji",
		u"<no tags>" : "<ni oznak>",
		u"Remove tag '%s'" : "Odstranim oznako '%s'",
		u"Public" : "Javna",
		u"Private" : "Zasebna",
		u"Change" : "Spremeni",
		u"Username" : "Upor. ime",
		u"Password" : "Geslo",
		u"Privacy" : "Zasebnost",
		u"Default tags" : "Privzete oznake",
		u"Image" : "Slika",
		u"Tags" : "Oznake",
		u"CHEESE!" : "GLEJ PTIČKA!",
		u"Select image" : "Izberi sliko",
		u"Settings" : "Nastavitve",
		u"Exit" : "Izhod",
		u"Marela uploader" : "Marelin nalagalnik",
		u"Upload has failed. Try again?" : "Nalaganje je spodletelo. Poskusim znova?",
		u"Upload has finished." : "Nalaganje je končano.",
		u"Your Marela username" : "Tvoje Marelino ime",
		u"Your Marela password" : "Tvoje Marelino geslo"
	}

def _(txt):
	if txt in trans and trans[txt]:
		return unicode(trans[txt], "utf-8")
	return txt

#
# Dictionary copied from http://www.bigbold.com/snippets/tag/series60#post1641
#
phone_mapping = {
	'RM-51': '3230',
	'RM-38': '3250',
	'NHM-10': '3600',
	'NHM-10X': '3620',
	'NHL-8': '3650',
	'NHL-8X': '3660',
	'RM-25': '6260',
	'RM-29': '6260',
	'NHL-10': '6600',
	'NHL-12': '6620',
	'NHL-12X': '6620',
	'RM-1': '6630',
	'RH-67': '6670',
	'RH-68': '6670',
	'RM-36': '6680',
	'RM-57': '6681',
	'RM-58': '6682',
	'RH-51': '7610',
	'RH-52': '7610',
	'NHL-2NA': '7650',
	'RM-49': 'E60',
	'RM-89': 'E61',
	'RM-10': 'E70',
	'RM-24': 'E70',
	'NEM-4': 'N-Gage',
	'RH-29': 'N-Gage QD',
	'RH-47': 'N-Gage QD',
	'RM-84': 'N70',
	'RM-99': 'N70',
	'RM-67': 'N71',
	'RM-112': 'N71',
	'RM-91': 'N80',
	'RM-92': 'N80',
	'RM-42': 'N90',
	'RM-43': 'N91',
	'RM-158': 'N91' }

#
# Camera handling together with keyboard handling
#
# Keyboard class written by Jurgen Scheible (http://www.mobilenin.com)
#
class Keyboard(object):
	def __init__(self,onevent=lambda:None):
		self._keyboard_state={}
		self._downs={}
		self._onevent=onevent

	def handle_event(self,event):
		if event['type'] == appuifw.EEventKeyDown:
			code=event['scancode']
			if not self.is_down(code):
				self._downs[code]=self._downs.get(code,0)+1
			self._keyboard_state[code]=1
		elif event['type'] == appuifw.EEventKeyUp:
			self._keyboard_state[event['scancode']]=0
		self._onevent()

	def is_down(self,scancode):
		return self._keyboard_state.get(scancode,0)

	def pressed(self,scancode):
		if self._downs.get(scancode,0):
			self._downs[scancode]-=1
			return True
		return False

class Camera:
	def __init__(self, mup):
		global screenSize
		global ImageFile
		self.mup = mup
		self.keyboard = Keyboard()
		self.c = appuifw.Canvas(event_callback=self.keyboard.handle_event, redraw_callback=self.redraw)
		appuifw.app.body = self.c
		appuifw.app.menu = []
		appuifw.app.exit_key_handler = self.exit_key_handler

		self.running = 1
		switch = 1

		# Set sizes of preview and final image
		cscreenSize = (0,0)
		imgSize = (0,0)

		sizes = camera.image_sizes()
		# Check rotation
		rot = 0
		for size in sizes:
			if size[0] >  size[1]: # Landscape
				rot = 0
			else: # Portrait
				rot = 1
			# Select the biggest format that fits the screen
			if size[0] > cscreenSize[0] and size[0] < screenSize[0] and \
				size[1] > cscreenSize[1] and size[1] < screenSize[1]:
					cscreenSize = size

			# Select the largest format that is not bigger than 800x600
			if size[0+rot] <=800 and size[0+rot] > imgSize[0] and \
				size[1-rot] <=600 and size[1-rot] > imgSize[1]:
					imgSize = size

		# Start shooting
		self.screen_picture = camera.take_photo(size = cscreenSize)

		while self.running:
			if switch == 1:
				# Take photo
				self.screen_picture = camera.take_photo(size = cscreenSize)

			self.redraw()
			e32.ao_yield()

			if self.keyboard.pressed(EScancodeLeftSoftkey):
				switch = 1
		
			if self.keyboard.pressed(EScancodeSelect):
				switch = 0
				e32.ao_yield()
				image = camera.take_photo(size = imgSize)
				image.save(ImageFile)
				self.running = 0
				e32.ao_yield()

		# We get here only by taking a picture. Save it and
		# proceed
		self.mup.handlePhoto(ImageFile)


	def redraw(self):
		self.c.blit(self.screen_picture, scale=1)

	def exit_key_handler(self):
		# Reset GUI
		appuifw.app.body = None
		appuifw.app.exit_key_handler = None
		self.running = 0
		self.mup.refresh()


#
# File browser for selection of images
#
class Filebrowser:
	def __init__(self, mup):
		self.mup = mup
		self.dir_stack = []
		self.current_dir = dir_iter.Directory_iter(e32.drive_list())

	def __keepDirsAndImages(self, entries):
		rslt = []
		for entry in entries:
			if entry[0][0] == "[" or (os.path.splitext(entry[0])[1] in ['.jpg', '.gif', '.png']) or \
				entry[1].strip() == _(u"Drive"):
				rslt.append(entry)
		return rslt

	def run(self):
		entries = self.current_dir.list_repr()
		if not self.current_dir.at_root:
			entries.insert(0, (u"..", u""))
		self.lb = appuifw.Listbox(entries, self.lbox_observe)
		self.lb.bind(EKeyLeftArrow, lambda: self.lbox_observe(0))
		self.refresh()

	def refresh(self):
		appuifw.app.menu = []
		appuifw.app.exit_key_handler = self.exit_key_handler
		appuifw.app.body = self.lb

	def exit_key_handler(self):
		appuifw.app.exit_key_handler = None
#		self.script_lock.signal()
		self.mup.refresh()

	def lbox_observe(self, ind = None):
		if not ind == None:
			index = ind
		else:
			index = self.lb.current()
		focused_item = 0

		if self.current_dir.at_root:
			self.dir_stack.append(index)
			self.current_dir.add(index)
		elif index == 0:                              # ".." selected
			focused_item = self.dir_stack.pop()
			self.current_dir.pop()
		elif os.path.isdir(self.current_dir.entry(index-1)):
			self.dir_stack.append(index)
			self.current_dir.add(index-1)
		else:
			item = self.current_dir.entry(index-1)
			i = -1
			if os.path.splitext(item)[1] in ['.jpg', '.png', '.gif']:
				i = appuifw.popup_menu([_(u"Select"), _(u"Remove")])
			if i == 0:
				try:
					# Select image and leave file browser
					self.mup.handlePhoto(item)
				except:
					type, value = sys.exc_info() [:2]
					appuifw.note(unicode(str(type)+'\n'+str(value)), "info")
				return
			elif i == 1:
				os.remove(item)
				focused_item = index - 1

		entries = self.current_dir.list_repr()
		#entries = self.__keepDirsAndImages(entries)
		if not self.current_dir.at_root:
			entries.insert(0, (u"..", u""))
		self.lb.set_list(entries, focused_item)

#
# Marela API handler
#
#  _encode_multipart_formdata (c) Jure Koren, 2006
#         Code subject to LGPL 2.1 or later,
#         (http://www.gnu.org/copyleft/lesser.html)
#
class MarelaAPI:
	def __init__(self, user, pwd):
		self.url = MARELA_BASE_URL + \
			"&system.login.user=%s&system.login.passwd=%s" % (user, pwd)
		self.settings = { 'privacy': '2' }

#	def generateURL(self):
#		items = [ ('photo.uploadPhotos.'+x[0], x[1]) for x in self.settings.items() ]
#		self.url += "&" + urllib.urlencode(items)

	def __encode_multipart_formdata(self, files):
		"""
		Wrapping files into a MIME multipart/form-data blob that goes
		over the wire through HTTP.
		Mostly stolen from http://fabien.seisen.org/python/urllib2_file.py
		"""
		# used to generate MIME boundaries
		key = ''
		for i in range(30):
			key += random.choice(string.letters+string.digits)

		BOUNDARY = '----------' + key
		CRLF = '\r\n'
		lines = []

		# Add parameters, if they exist
		for key in self.settings.keys():
			lines.append('--' + BOUNDARY)
			lines.append('Content-Disposition: form-data; name="%s"' % key)
			lines.append('')
			lines.append(self.settings[key].encode('utf-8'))

		# Add files
		for name, fh in files:
			buf = ''
			if type(fh) is not file:
				# Presume its string
				buf = fh
			else:
				buf = fh.read()
			lines.append('--' + BOUNDARY)
			lines.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (name, name))
			lines.append('Content-Type: application/octet-stream')
			lines.append('Content-Length: %d' % len(buf))
			lines.append('')
			lines.append(buf)
		lines.append('--' + BOUNDARY + '--')
		lines.append('')
		body = CRLF.join(lines)
		content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
		return content_type, body

	def uploadImage(self, f):
		"""
		Upload image with metadata to Marela. f can be a file descriptor or an
		image stored as a string.
		"""
#		self.generateURL()
		ctype, body = self.__encode_multipart_formdata([('file1',f)])
		headers = {"Content-type": ctype}

		appuifw.note(_(u"Sending image..."))
		post = httplib.HTTPConnection(MARELA_HOST)
		post.request("POST", self.url, body, headers)

		response = post.getresponse()

		if response.status != 200:
			return False, response.reason

		rsp = eval(response.read())
		if rsp.has_key('photo.uploadPhotos_err') or rsp.has_key('system.login_err'):
			return False, rsp

		return True, rsp

#
# Handling Photo
#
class Photo:
	def __init__(self, mup, imgfile):
		global screenSize
		self.mup = mup
		self.File = imgfile
		self.Img = graphics.Image.open(imgfile)
		self.Thumb = self.Img.resize(screenSize, keepaspect=1)
		self.c = None

	def refresh(self):
		appuifw.app.menu = [(_(u"Send"), self.mup.upload)]
		appuifw.app.exit_key_handler = self.mup.exitPhoto
		self.c = appuifw.Canvas(redraw_callback=self.redraw)
		appuifw.app.body = self.c
		self.c.blit(self.Thumb)

	def redraw(self, part):
		self.c.blit(self.Thumb)

#
# Handling tags (tag tab)
#
class Tags:
	def __init__(self, mup, tags = [], otags = []):
		#old_menu = appuifw.app.menu
		self.mup = mup
		appuifw.app.menu = [(_(u"Add tags"), self.addTag), (_(u"Select used"), self.selectTag),
				(_(u"Remove tags"), self.removeTag), (_(u"Send"), self.mup.upload)]
		appuifw.app.exit_key_handler = self.mup.exitPhoto
		self.tags = tags
		self.oldtags = otags
		if self.tags:
			self.lb = appuifw.Listbox(self.tags, self.remove)
		else:
			self.lb = appuifw.Listbox([_(u"<no tags>")], self.remove)
		appuifw.app.body = self.lb

	def refresh(self):
		if self.tags:
			self.lb.set_list(self.tags)
		else:
			self.lb.set_list([_(u"<no tags>")])
		if appuifw.app.body != self.lb:
			appuifw.app.body = self.lb
			appuifw.app.menu = [(_(u"Add tags"), self.addTag), (_(u"Select used"), self.selectTag),
					(_(u"Remove tags"), self.removeTag), (_(u"Send"), self.mup.upload)]
			appuifw.app.exit_key_handler = self.mup.exitPhoto

	def refreshTags(self, tags):
		for tag in tags:
			if tag in self.oldtags:
				self.oldtags.remove(tag)
			self.oldtags.append(tag)
		if db:
			db["old_tags"] = ",".join(self.oldtags)

	def clear(self):
		self.tags = []
		self.refresh()

	def remove(self):
		if not self.tags: return
		current = self.lb.current()
		gone = appuifw.query(_(u"Remove tag '%s'") % self.tags[current], "query")
		if gone: # Remove tag
			self.tags.remove(self.tags[current])
		self.refresh()

	def addTag(self):
		input = appuifw.query(_(u"Add tags"), "text")
		if input:
			tags = input.split(",")
			tags = [tag.strip() for tag in tags]
			for tag in tags:
				if tag not in self.tags:
					self.tags.append(tag)
			self.refreshTags(tags)
		self.refresh()

	def selectTag(self):
		# Don't show already added
		ntags = []
		for tag in self.oldtags:
			if tag not in self.tags:
				ntags.append(tag)

		if not ntags:
			return
		# Show and handle only this selection
		selection = appuifw.multi_selection_list(ntags, "checkbox", 1)
		if selection:
			tags = [ntags[i] for i in selection]
			for tag in tags:
				if tag not in self.tags:
					self.tags.append(tag)
			self.refreshTags(tags)
		self.refresh()

	def removeTag(self):
		if not self.tags: return
		selection = appuifw.multi_selection_list(self.tags, "checkbox", 1)
		if selection:
			tags = [self.tags[i] for i in selection]
			for tag in tags:
				self.tags.remove(tag)
		self.refresh()


#
# Handling privacy
#
class Privacy:
	def __init__(self, mup):
		self.mup = mup
		self.private = [_(u"Public")]
		self.privacy = Settings["privacy"]
		appuifw.app.menu = [(_(u"Change"), self.change), (_(u"Send"), self.mup.upload)]
		appuifw.app.exit_key_handler = self.mup.exitPhoto
		self.lb = appuifw.Listbox(self.private, self.change)
		appuifw.app.body = self.lb

	def refresh(self):
		self.lb.set_list(self.private)
		if appuifw.app.body != self.lb:
			appuifw.app.body = self.lb
			appuifw.app.menu = [(_(u"Change"), self.change), (_(u"Send"), self.mup.upload)]
			appuifw.app.exit_key_handler = self.mup.exitPhoto

	def change(self):
		options = [_(u"Public"), _(u"Private")]
		index = appuifw.popup_menu(options)
		if index:
			self.private = [options[index]]
			if index:
				self.privacy = "2"
		self.refresh()

#
# Handle settings
#
class MarelaSettings(dict):
	def __init__(self):
		s = {"username":"","password":"","privacy":"","default_tags":[],
			"old_tags":[]}
		dict.__init__(self, s)
		self.lb = None
		self.oldmenu = None # Doesn't exist yet

	def read(self):
		global db
		# Read settings
		if os.path.isfile(SettingsDB+".e32dbm"):
			db = e32dbm.open(SettingsDB, "wf")
			for key in ["username", "password", "privacy"] :
				dict.__setitem__(self, key, db[key])
			for key in ["default_tags", "old_tags"]:
				if db[key].strip():
					dict.__setitem__(self, key, [x.strip() for x in db[key].split(",")])
				else:
					dict.__setitem__(self, key, [])

	def __setitem__(self, x, y):
		global db
		# Read settings
		dict.__setitem__(self, x, y)
		if isinstance(y, list):
			db[x] = ','.join(y)
		else:
			db[x] = y

	def __delitem__(self, x):
		global db
		# Read settings
		dict.__delitem__(self, x)
		db.__delitem__(x)

	def get(self, x, y):
		value = y
		try:
			value = self.__getitem__(x)
		except: pass
		return value

	def handleSetting(self):
		index = self.lb.current()
		labels = [_(u"Username"), _(u"Password"), _(u"Privacy"), _(u"Default tags")]
		items = (("username","text"), ("password", "code"), ("privacy", "combo"), ("default_tags", "text"))

		value = self.get(items[index][0], "")

		if items[index][0] == "default_tags":
			query = appuifw.query(labels[index], items[index][1], ",".join(value))
		elif items[index][1] != "combo":
			query = appuifw.query(labels[index], items[index][1], value)
		else:
			query = appuifw.popup_menu([u"Javna", u"Zasebna"],labels[index])

		if query:
			self.__setitem__(items[index][0], query)
			self.save()

	def show(self):
		# Show settings form
		labels = [_(u"Username"), _(u"Password"), _(u"Privacy"), _(u"Default tags")]
		self.lb = appuifw.Listbox(labels, self.handleSetting)
		appuifw.app.body = self.lb
		# Exist, because it gets called from application
		self.oldmenu = appuifw.app.menu
		appuifw.app.menu = []
		appuifw.app.exit_key_handler = self.exit_key_handler

	def save(self):
		global db
		# Read settings
		db.sync()

	def close(self):
		global db
		# Read settings
		db.close()

	def exit_key_handler(self):
		self.save()
		appuifw.app.body = None
		appuifw.app.menu = self.oldmenu
		appuifw.app.exit_key_handler = None
		self.lb = None

#
# Application
#
class Marela:
	def __init__(self):
		self.lock=e32.Ao_lock()

		# Set app data
		self.old_title = appuifw.app.title
		self.Image = None
		self.tabs = [_(u"Image"),_(u"Tags"),_(u"Privacy")]
		self.title = _(u"Marela uploader")
		self.imgTab = None
		self.tagTab = None
		self.privTab = None
		self.settObj = None
		self.Camera = None
		self.FileBrowser = None

		# Set GUI
		appuifw.app.title = self.title
		appuifw.app.menu = [(_(u"CHEESE!"), self.capturePhoto), (_(u"Select image"), self.handleFiles),
			(_(u"Settings"), Settings.show), (_(u"Exit"), self.exit_key_handler)]

		self.refresh()

		# Wait for the user to exit the uploader
		self.lock.wait()

		# Clean up
		appuifw.app.title = self.old_title
		appuifw.app.set_tabs([], self.handlePhotoTab)

		if db:
			db.sync()
			db.close()


	def refresh(self):
		global screenSize
		canvas = appuifw.Canvas(redraw_callback=self.redraw)
		screenSize = canvas.size
		appuifw.app.body = canvas
		appuifw.app.menu = [(_(u"CHEESE!"), self.capturePhoto), (_(u"Select image"), self.handleFiles),
			(_(u"Settings"), Settings.show), (_(u"Exit"), self.exit_key_handler)]

	def redraw(self, part):
		pass

	def capturePhoto(self):
#		self.handlePhoto(u"c:\\mk.jpg")
		self.Camera = Camera(self)

	def handleFiles(self):
		self.FileBrowser = Filebrowser(self)
		self.FileBrowser.run()

	def handlePhoto(self, imgFile):
		if not self.imgTab:
			self.imgTab = Photo(self, imgFile)
		appuifw.app.set_tabs(self.tabs, self.handlePhotoTab)
		appuifw.app.activate_tab(0)
		appuifw.app.exit_key_handler = self.exitPhoto

		self.imgTab.refresh()

	def handlePhotoTab(self, index):
		if index == 0:
			# Show image, if haven't yet
			if not self.imgTab:
				self.imgTab = Photo(self)
			self.imgTab.refresh()
		elif index == 1:
			if not self.tagTab: self.tagTab = Tags(self, Settings["default_tags"], Settings["old_tags"])
			else: self.tagTab.refresh()
		elif index == 2:
			if not self.privTab: self.privTab = Privacy(self)
			else: self.privTab.refresh()
		appuifw.app.title = self.tabs[index]

	def exitPhoto(self):
		# Reset interface
		self.imgTab = None
		self.tagTab = None
		self.privTab = None

		# Display start screen
		appuifw.app.title = self.title
		appuifw.app.set_tabs([], self.handlePhotoTab)
		appuifw.app.menu = [(_(u"CHEESE!"), self.capturePhoto), (_(u"Select image"), self.handleFiles),
			(_(u"Settings"), Settings.show), (_(u"Exit"), self.exit_key_handler)]
		appuifw.app.exit_key_handler = self.exit_key_handler

		self.refresh()

	def upload(self):
		img = self.imgTab.File
		succ = False
		post = MarelaAPI(Settings["username"], Settings["password"])
		if self.privTab:
			post.settings["privacy"] = self.privTab.privacy
		if self.tagTab:
			post.settings["tags"] = ",".join(self.tagTab.tags)

		succ, rsp = post.uploadImage(open(img, 'r'))
		while not succ: # Failed upload
			succ = True
			next = appuifw.query(_(u"Upload has failed. Try again?"), "query")
			if next:
				succ, rsp = post.uploadImage(open(img, 'r'))
		appuifw.note(_(u"Upload has finished."), "info")
		# Reset
		self.exitPhoto()

	def exit_key_handler(self):
		# Now exit
		appuifw.app.exit_key_handler = None
		self.lock.signal()


def firstRun():
	global phone_mapping
	allok = True
	sett = {"old_tags": ""}

	# When application is run for the first time, get and set
	# username and password (and set default privacy and tags)
	username = appuifw.query(_(u"Your Marela username"), "text")
	if not username:
		return False
	sett["username"] = username

	password = appuifw.query(_(u"Your Marela password"), "code")
	if not password:
		return False
	sett["password"] = password

	# Default privacy is public and tags are empty
	sett["privacy"] = "0"

	# Try to find out the phone model (for Nokia phones)
	sett["default_tags"] = ""
	firmware = sysinfo.sw_version().split(' ')[3]
	if phone_mapping.has_key(firmware):
		phone = phone_mapping[firmware]
		sett["default_tags"] = "nokia,%s,nokia %s" % (phone, phone)

	# Write them
	try:
		db = e32dbm.open(SettingsDB, "nf")
		for key in sett:
			db[key] = sett[key]
		db.sync()
		db.close()
	except:
		allok = False
	return allok


if __name__ == '__main__':
	happy = True
#	appuifw.app.body = appuifw.Canvas()

	if not os.path.isfile(SettingsDB+".e32dbm"):
		happy = firstRun()

	if happy:
		Settings = MarelaSettings()
		Settings.read()

		mup = Marela()
