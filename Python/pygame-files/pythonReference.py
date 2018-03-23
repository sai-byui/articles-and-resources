import os


class Player:

	# class default constructor
	def __init__(self): #keyword 'self' used in all class methods as the first parameter
		self.x = 0
		self.y = 0
		self.name = "unknown"
		self.dx = 0
		self.dy = 0

	#class desctructor
	def __del__(self):
		print("destroying object")


	# Member functions
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def setName(self, name):
		self.name = name

	def printName(self):
		print(self.name)
		
#inheriting from another class
class NPC(Player):
	
	def talk(self, name):
		print("hello " + name)
	

# creating an object
Player1 = Player()
seller = NPC()


#calling a member functions
Player1.setName("Hero")
Player1.printName()

seller.talk(Player1.name)

#opening a file
fileName = raw_input('Enter a file name')
try:
	fileHandle = open(fileName)
except:
	print('file: ' + filename + ' cannot be opened')
	exit()
#don't forget to close
fileHandle.close()

#destroying an object
Player1.__del__()
