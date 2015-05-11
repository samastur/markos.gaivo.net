from BeautifulSoup import BeautifulSoup

class InputError(Exception): pass

class FAQ(dict):
	def __init__(self, txt):
		try:
			soup = BeautifulSoup(txt)
			content = soup("div", {"id": "content"})[0].contents

			while '\n' in content:
				content.remove('\n')

			self.buildDict(content)
		except:
			raise InputError

	def buildDict(self, txt):
		elmID = 0
		elmQuestion = ""
		elmAnswer = ""
		for line in txt:
			elmName = line.name.lower()
			if elmName in ["h1", "h2", "h3", "h4", "h5", "h6"]:
				if elmID:
					self.__setitem__(elmID, [elmQuestion, elmAnswer])
					elmAnswer = ""
				num, q = line.string.split(":")
				elmID = int(num.strip())
				elmQuestion = q.strip()
			else:
				elmAnswer += line.prettify().strip()
		self.__setitem__(elmID, [elmQuestion, elmAnswer])
