import pygame

class Findr(pygame.sprite.Sprite):   #inheritance
	def __init__(self,empty_path):
		# basic
		super().__init__()
		self.image = pygame.image.load('person.png').convert_alpha()
		self.rect = self.image.get_rect(center = (60,60))
		# movement 
		self.pos = self.rect.center
		self.speed = 2
		self.direction = pygame.math.Vector2(0,0)
		# path
		self.path = []
		self.collision_rects = []
		self.empty_path = empty_path
	
	def get_coord(self):
		col = self.rect.centerx // 32
		row = self.rect.centery // 32
		return (col,row)
	
	def set_path(self,path):
		self.path = path
		self.create_collision_rects()
		self.get_direction()
	
	def create_collision_rects(self):
		if self.path:
			self.collision_rects = []
			for point in self.path:
				x = (point[0] * 32) + 16
				y = (point[1] * 32) + 16
				rect = pygame.Rect((x - 2,y - 2),(4,4))
				self.collision_rects.append(rect)
	
	def get_direction(self):
		if self.collision_rects:
			start = pygame.math.Vector2(self.pos)
			end = pygame.math.Vector2(self.collision_rects[0].center)
			self.direction = (end - start).normalize()
		else:
			self.direction = pygame.math.Vector2(0,0)
			self.path = []
	
	def check_collisions(self):
		if self.collision_rects:
			for rect in self.collision_rects:
				if rect.collidepoint(self.pos):
					del self.collision_rects[0]
					self.get_direction()
		else:
			self.empty_path()
	
	def update(self):
		self.pos += self.direction * self.speed
		self.check_collisions()
		self.rect.center = self.pos
