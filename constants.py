import pygame

width, height = 450, 500
rows, cols = 9, 9
square_size = width//cols
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
gray = (58, 18, 228)

sudoku = []
sudoku.append([5, 3, 0, 0, 7, 0 ,0, 0, 0])
sudoku.append([6, 0, 0, 1, 9, 5 ,0, 0, 0])
sudoku.append([0, 9, 8, 0, 0, 0 ,0, 6, 0])
sudoku.append([8, 0, 0, 0, 6, 0 ,0, 0, 3])
sudoku.append([4, 0, 0, 8, 0, 3 ,0, 0, 1])
sudoku.append([7, 0, 0, 0, 2, 0 ,0, 0, 6])
sudoku.append([0, 6, 0, 0, 0, 0 ,2, 8, 0])
sudoku.append([0, 0, 0, 4, 1, 9 ,0, 0, 5])
sudoku.append([0, 0, 0, 0, 8, 0 ,0, 7, 9])
select = []
permanent = []
temp = []
for i in range(9):
	for j in range(9):
		if sudoku[i][j] != 0:
			permanent.append([i, j, sudoku[i][j]])
		else:
			temp.append([i, j])