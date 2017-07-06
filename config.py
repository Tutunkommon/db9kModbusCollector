
import pickle
import collections
import sys


class target():
		def __init__(self, name, ip):
			self.name = name
			self.ip = ip

class device():
		def __init__(self, name, location, target):
			self.properties = collections.OrderedDict()
			self.name = name
			self.location = location
			self.target = target

		def setProperty(self, name, address, dataType):
			prop = property(address,dataType)
			self.properties[name]=prop

		def getProperty(self, name):
			if(name in self.properties):
				prop=self.properties[name]
				return(prop)
			return(None)


class property():
	def __init__(self, address, dataType):
		self.address = address
		self.type = dataType


class configuration():
	def __init__(self):
		self.devices = []

	def addDevice(self, newDev):
		self.devices.append(newDev)

def saveFile(cfList):
	filename = 'config.pkl'
	file = open(filename,"wb")
	pickle.dump(cfList,file)
	file.close()

def readFile():
	filename = 'config.pkl'
	file = open(filename,'rb')
	#configList = configuration()
	cfl = pickle.load(file)
	file.close()
	print(cfl)
	print(cfl.devices)

def createSample():
	configList=configuration()
	print("Creating Target:")
	print("tgt=target('test','127.0.0.1')")
	tgt=target('test','127.0.0.1')

	print("Creating device:")
	print("dev = device('Laser123','line1:station1','tgt')")
	dev = device('Laser123','line1:station1','tgt')

	print("Creating a property for device:")
	print("dev.setProperty('height','400010','INT')")
	print("dev.setProperty('width','400011','INT')")
	dev.setProperty('height','400010','INT')
	dev.setProperty('width','400011','INT')

	print("Adding the device to the list")
	print("configList.addDevice(dev)")
	configList.addDevice(dev)

	print("Saving the config list")
	saveFile(configList)

def displayData():
	'''
	for i in cfl.devices:
		print("DEVICE:  ",i.name)
		print("\t Location:\t",i.location)
'''
	print(cfl)
	print(cfl.devices)

if(__name__ == '__main__'):
	cfl=configuration()
	while(True):
		print("1. Create Sample")
		print("2. Read Config file")
		print("3. Display Config Data")
		print("4. Exit")
		select = input("-> ")

		if(select == "1"):
			createSample()

		if(select == "2"):
			readFile()

		if(select=="3"):
			displayData()

		if(select == "4"):
			sys.exit()




