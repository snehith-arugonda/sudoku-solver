import pygame
pygame.init()
from sudoku.constants import width, height, square_size, cols, rows, black, blue, gray, white, sudoku, permanent, temp, select
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('sudoku')
FPS = 60		

def square_pos(pos):
	x, y = pos
	row = y//square_size
	col = x//square_size
	return row, col

def draw_squares():
		win.fill(white)
		for row in range(0, rows, 1):
			pygame.draw.line(win, black, (0, row*square_size), (width, row*square_size), 1)

		for row in range(0, rows+1, 3):
			pygame.draw.line(win, black, (0, row*square_size), (width, row*square_size), 3)			
										  
		for col in range(0, cols, 3):
			pygame.draw.line(win, black, (col*square_size, 0), (col*square_size, height-50), 3)

		for col in range(0, cols, 1):
			pygame.draw.line(win, black, (col*square_size, 0), (col*square_size, height-50), 1)	

def timer(secons):
	font = pygame.font.Font('freesansbold.ttf', 16)
	text = font.render('time:' + str(secons), True, black)
	textRect = text.get_rect()
	textRect.center = (width-3*square_size, height - square_size//2)
	win.blit(text, textRect)

def permanent_elements():
	for i in range(len(permanent)):
		font = pygame.font.Font('freesansbold.ttf', 16)
		text = font.render(str(permanent[i][2]), True, black)
		textRect = text.get_rect()
		textRect.center = (permanent[i][0]*square_size + square_size//2,permanent[i][1]*square_size + square_size//2)
		win.blit(text, textRect)


def answers(col, row, key):
	sudoku[row][col] = key

def all_elements():
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] != 0 and ([i, j] in temp):
				font = pygame.font.Font('freesansbold.ttf', 16)
				text = font.render(str(sudoku[i][j]), True, gray)
				textRect = text.get_rect()
				textRect.center = (i*square_size + square_size//2,j*square_size + square_size//2)
				win.blit(text, textRect)

def selected(row, col):
	for i in range(9):
		select.append([False]*9)
	return True

def reset():
	for [i, j] in temp:
		sudoku[i][j] = 0
	main()	

def find_elem():
	for [i, j] in temp:
		if sudoku[i][j] == 0:
			return i, j
	return None

def valid(num, posx, posy):
	for i in range(9):
		if num == sudoku[posx][i] and sudoku[posx][posy]!= num:
			return False
	for i in range(9):
		if num == sudoku[i][posy] and sudoku[posx][posy]!= num:
			return False

	box_x = posx//3
	box_y = posy//3	
	for i in range(box_x*3, box_x*3 + 3):
		for j in range(box_y*3, box_y*3 + 3):
			if num == sudoku[i][j] and sudoku[posx][posy]!= num:
				return False
	return True				

def solve():

	clock = pygame.time.Clock()
	if find_elem() == None:
		return True

	else:
		posx, posy = find_elem()
		for i in range(1, 10):
			if valid(i, posx, posy):
				sudoku[posx][posy] = i
				
				# solving visualizer

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_r:
							solving = False
							reset()
				win.fill(white)
				draw_squares()
				permanent_elements()
				all_elements()
				pygame.display.update()
				# ends here

				if solve():
					return True
				sudoku[posx][posy] = 0

		return False
			
def result():

	result = True
	clock = pygame.time.Clock()
	for [i, j] in temp:
		sudoku[i][j] = 0
	solve()

	while result:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				result = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					result = False
					reset()		

		draw_squares()
		permanent_elements()
		all_elements()
		
		pygame.display.update()	
	pygame.quit()
	quit()		

def ifFinished():

	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0 or not(valid(sudoku[i][j], i, j)):
				return False
	return True

def gameOver():

	game_over = True
	clock = pygame.time.Clock()	

	while game_over:

		clock.tick(FPS)
		draw_squares()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					game_over = False
					reset()			

		permanent_elements()
		all_elements()
		font = pygame.font.Font('freesansbold.ttf', 32)
		text = font.render('game over', True, blue)
		textRect = text.get_rect()
		textRect.center = (width//2,(height-50)//2)
		win.blit(text, textRect)

		pygame.display.update()
	pygame.quit()
	quit()				

def main():
	run = True
	clock = pygame.time.Clock()		
	#start_ticks=pygame.time.get_ticks()
	mouse_pressed = False

	while run:
		clock.tick(FPS)
		draw_squares()
		#seconds=(pygame.time.get_ticks()-start_ticks)/1000
		permanent_elements()
		#timer(seconds)
		all_elements()
		if ifFinished():
			run = False
			gameOver()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					result()
				if event.key == pygame.K_1:
					key = 1
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_2:
					key = 2	
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_3:
					key = 3	
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_4:
					key = 4
					if select[row][col]:
						answers(row, col, key)	
				if event.key == pygame.K_5:
					key = 5	
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_6:
					key = 6	
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_7:
					key = 7	
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_8:
					key = 8
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_9:
					key = 9	
					if select[row][col]:
						answers(row, col, key)
				if event.key == pygame.K_DELETE:
					key = 0	
					if select[row][col]:
						answers(row, col, key)						

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				row, col = square_pos(pos)
				select[row][col] = selected(row, col)
				mouse_pressed = True

		if mouse_pressed:
			pygame.draw.rect(win, blue, (col*square_size, row*square_size, square_size, square_size), 1)
		pygame.display.update()
			
	pygame.quit()
	quit()
				
main()