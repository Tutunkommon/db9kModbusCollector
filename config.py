
import json

class target():
		def __init__(self, name, ip):
			self.name = name
			self.ip = ip

class device():
		def __init__(self, name, location, target):
			properties = dict()
			self.name = name
			self.location = location
			self.target = target

		def setProperty(self, name, address, dataType):
			prop = property(address,datatype)
			self.properties[name]=prop

		def getProperty(self, name):
			if(name in self.properties):
				prop=property(self.properties[name])


class property():
	def __init__(self, address, dataType):
		self.address = address
		self.type = dataType




