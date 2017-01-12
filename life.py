###################################
##SCORIA GAMES, INC (C) 2011-2017##
##    CREATIOEXICNEVSEXITIVM     ##
## DNA SCRIPT BY HEBER CASILLAS  ##
###################################
print("Initializing...")
import random, pygame, sys
from pygame.locals import *
pygame.init()
gameClock = pygame.time.Clock()
gameClock.tick(24)
screenWidth = 1280
screenHeight = 720
DISPLAY = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Homunculus Life Engine')
alphabet = ['a','b','c','d','aa','bb','cc','dd']
creatureSpawns = 5
creatureCount = 0
DISPLAY.fill((  0,   0,   0))

class DNALetter:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.letter = random.choice(alphabet)
		
class Creature:
	def __init__(self, x, y):
		self.cID = creatureCount
		self.dx = 0
		self.dy = 0
		self.x = x
		self.y = y
		self.xtmp = x
		self.ytmp = y
		self.newX = 0
		self.newy = 0
		self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.dnaStep = 0
		self.dnaLimit = random.randint(3, 10**4)
		self.dna = []
		self.creatureObj = 0
		self.radius = 0
		self.borderWidth = 0
		self.excenChoice = ['-1','0','1']
		self.excentricity = int(random.choice(self.excenChoice))
		self.isBorn = 0
		self.life = 0
		self.maxLife = 100
		while self.dnaStep < self.dnaLimit:
			self.dnaStep += 1
			self.dna.append(DNALetter(self.x, self.y))
	def birth(self):
		for i in self.dna:		
			if i.letter == 'a':
				self.xtmp += 1
			elif i.letter == 'aa':
				self.xtmp += 1
				self.ytmp += 1
			elif i.letter == 'b':
				self.xtmp -= 1
			elif i.letter == 'bb':
				self.xtmp -= 1
				self.ytmp -= 1
			elif i.letter == 'c':
				self.ytmp += 1
			elif i.letter == 'cc':
				self.xtmp += 1 + self.excentricity
				self.ytmp += 1 + self.excentricity
			elif i.letter == 'd':
				self.ytmp -= 1
			elif i.letter == 'dd':
				self.ytmp -= 1 + self.excentricity
				self.xtmp -= 1 + self.excentricity
			i.x = self.xtmp
			i.y = self.ytmp
			pygame.draw.circle(DISPLAY, self.color, (i.x, i.y), self.radius, self.borderWidth)
		self.isBorn = 1
	def exist(self):
		self.life += 1
		for i in self.dna:
			if i.letter == 'a':
				self.dx += 1
			elif i.letter == 'aa':
				self.dx += 1
				self.dy += 1
			elif i.letter == 'b':
				self.dx -= 1
			elif i.letter == 'bb':
				self.dx -= 1
				self.dy -= 1 
			elif i.letter == 'c':
				self.dy += 1
			elif i.letter == 'cc':
				self.dy += 1 + self.excentricity
				self.dx += 1 + self.excentricity
			elif i.letter == 'd':
				self.dy -= 1 
			elif i.letter == 'dd':
				self.dy -= 1 + self.excentricity
				self.dx -= 1 + self.excentricity
			i.newX = self.x + self.dx
			i.newY = self.y + self.dy
			i.x = max(0, min(i.newX, screenWidth))
			i.y = max(0, min(i.newY, screenHeight))
			pygame.draw.circle(DISPLAY, self.color, (i.x, i.y), self.radius, self.borderWidth)
		if self.life >= self.maxLife:
			self.destroy()
	def destroy(self):
		for i in self.dna:
			self.dna.remove(i)
		creatures.remove(self)
print("\nHomuculus Life Engine\nScoria Games, Inc 2011 - 2017\n\nSpawning Life...")
creatures = []
while creatureCount < creatureSpawns:
	creatureCount += 1
	creatures.append(Creature(int(screenWidth/2), int(screenHeight/2)))
print("Beginning Simulation...\n")	

while True:
	DISPLAY.fill((  0,   0,   0))
	for i in creatures:
		if i.isBorn == 0:
			i.birth()
			print("Creature", i.cID, "| DNA length:", i.dnaStep, "| Excentricity:", i.excentricity)
		if i.isBorn == 1:
			i.exist()
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == KEYDOWN: 
			if event.key == K_RETURN:
				creatureCount += 1
				creatures.append(Creature(int(screenWidth/2), int(screenHeight/2)))
		
