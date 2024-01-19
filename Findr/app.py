import pygame, sys
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from findr import Findr

class Model:
	def __init__(self,matrix):
		# setup
		self.matrix = matrix   # setting the matrix
		self.grid = Grid(matrix = matrix)   # creating the grid
		self.select_surf = pygame.image.load('select.png'). convert_alpha()   #creating the selection pointer
		# pathfinding
		self.path = []   #creating a empty list
		self.dist = 0
		self.time = 0
		self.text_font = pygame.font.SysFont("Arial", 10)
		# Findr
		self.findr = pygame.sprite.GroupSingle(Findr(self.empty_path))   #Creating instance of findr class
	
	def empty_path(self):
		self.path = []
	
	def draw_active_cell(self):
		mouse_pos = pygame.mouse.get_pos()   #getting mouse position
		row =  mouse_pos[1] // 32
		col =  mouse_pos[0] // 32
		current_cell_value = self.matrix[row][col]
		if current_cell_value == 1:   #pointing only on rectangles with 1 value
			rect = pygame.Rect((col * 32,row * 32),(32,32))  #creating small rectangles 
			screen.blit(self.select_surf,rect)   #selecting small rectangles
	
	def create_path(self):
		# startposition
		start_x, start_y = self.findr.sprite.get_coord()
		start = self.grid.node(start_x,start_y)   #getting actual start node
		# endposition
		mouse_pos = pygame.mouse.get_pos()
		end_x,end_y =  mouse_pos[0] // 32, mouse_pos[1] // 32  
		end = self.grid.node(end_x,end_y)   #getting end node
		### path
		finder = AStarFinder(diagonal_movement = DiagonalMovement.always)   #defining path finding algorithm
		self.path,_ = finder.find_path(start,end,self.grid)   #finding the path
		self.grid.cleanup()   #reseting the path
		self.findr.sprite.set_path(self.path)
		# print(self.path)
	
	def draw_path(self):
		if self.path:   #checking the path is not empty
			points = []
			for point in self.path:
				x = (point[0] * 32) + 16
				y = (point[1] * 32) + 16   #getting the actual point
				points.append((x,y))   #appending points
			pygame.draw.lines(screen,'#ffffff',False,points,9)   #drawing the line

	def calc_dist(self):
		if self.path:
			self.dist = (len(self.path) - 1) * 90
			# print(self.dist)

	def calc_time(self):
		if self.dist:
			self.time = round(self.dist * 0.013,2)
			# print(self.time)

	def draw_text(self):
		font = pygame.font.SysFont(None, 55)
		text = f"{str(self.time)}min({str(self.dist)}m)"
		text_col = (255, 255, 255)
		text_pos = (40, 800)
		img = font.render(text, True, text_col)
		screen.blit(img, text_pos)

	def update(self):
		self.draw_active_cell()
		self.draw_path()
		self.calc_dist()
		self.calc_time()
		self.draw_text()
		
		# findr updating and drawing
		self.findr.update()
		self.findr.draw(screen)

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 896
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

# game setup
bg_surf = pygame.image.load('map.png').convert()
matrix = [[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
[0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
[0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0],
[0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0]]

#Object
pathfinder = Model(matrix)

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pathfinder.create_path()   #creating a path whenever the player clicks a button

	screen.blit(bg_surf,(0,0))
	pathfinder.update()

	pygame.display.update()
	clock.tick(60)
