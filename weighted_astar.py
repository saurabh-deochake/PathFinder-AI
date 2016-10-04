# CS520: Artificial Intelligence Project 1
# Contributors: Saurabh Deochake, Rohit Bobade 
# Email: {saurabh.deochake, rohit.bobade}@rutgers.edu
# Weighted Astar Algorithm

from collections import defaultdict
from heapq import *
import math
import re
import pygame
import time
import timeit

def heuristic_cost_estimate(a, b):
	# Diagonal Distance
	return (abs(a[0] - b[0]) + abs(a[1] - b[1])) + (math.sqrt(2) - 2)*min(abs(a[0] - b[0]),abs(a[1] - b[1]))
	# Eucledian Distance
	# return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
	# Eucledian square
	# return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
	# Manhattan Distance
	# return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def dist_between(array,current,neighbor):
	if neighbor[0] >= 0 and neighbor[0] < len(array):
		if neighbor[1] >= 0 and neighbor[1] < len(array[0]): 
			if array[current[0]][current[1]] == array[neighbor[0]][neighbor[1]] == '1':
				if round(math.sqrt((neighbor[0]-current[0]) ** 2 + (neighbor[1]-current[1]) ** 2),2) == 1.41:
					return math.sqrt(2)
				else:
					return 1
			elif array[current[0]][current[1]] == array[neighbor[0]][neighbor[1]] == '2':
				if round(math.sqrt((neighbor[0]-current[0]) ** 2 + (neighbor[1]-current[1]) ** 2),2) == 1.41:
					return math.sqrt(8)
				else:
					return 2
			elif array[current[0]][current[1]] == '1' and array[neighbor[0]][neighbor[1]] == '2':
				if round(math.sqrt((neighbor[0]-current[0]) ** 2 + (neighbor[1]-current[1]) ** 2),2) == 1.41:
					return ((math.sqrt(2) + math.sqrt(8))/2)
				else:
					return 1.5
			elif  array[current[0]][current[1]] == '2' and array[neighbor[0]][neighbor[1]] == '1':
				if round(math.sqrt((neighbor[0]-current[0]) ** 2 + (neighbor[1]-current[1]) ** 2),2) == 1.41:
					return ((math.sqrt(2) + math.sqrt(8))/2)
				else:
					return 1.5
			elif array[current[0]][current[1]] == array[neighbor[0]][neighbor[1]] == 'a':
				return 0.25
			elif array[current[0]][current[1]] == array[neighbor[0]][neighbor[1]] == 'b':
				return 0.5
			elif array[current[0]][current[1]] == 'a' and array[neighbor[0]][neighbor[1]] == 'b':
				return 0.375
			elif array[current[0]][current[1]] == 'b' and array[neighbor[0]][neighbor[1]] =='a':
				return 0.375
			elif array[current[0]][current[1]] == '1' and array[neighbor[0]][neighbor[1]] == 'a':
				return 0.25
			elif array[current[0]][current[1]] == 'a' and array[neighbor[0]][neighbor[1]] == '1':
				return 0.25
			elif array[current[0]][current[1]] == '2' and array[neighbor[0]][neighbor[1]] == 'b':
				return 0.5
			elif array[current[0]][current[1]] == 'b' and array[neighbor[0]][neighbor[1]] == '2':
				return 0.5
			elif array[current[0]][current[1]] == '1' and array[neighbor[0]][neighbor[1]] == 'b':
				return 0.375
			elif array[current[0]][current[1]] == 'b' and array[neighbor[0]][neighbor[1]] == '1':
				return 0.375
			else:
				
				return float("infinity")
		else:
			
			return float("infinity")
	else:
		return float("infinity")

def astar(array, start, goal):

	neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

	closedSet = set()

	openSet = []

	cameFrom = {}

	gScore = defaultdict(lambda:float("infinity"))

	gScore[start] = 0

	fScore = defaultdict(lambda:float("infinity"))

	fScore[start] = heuristic_cost_estimate(start, goal)

	heappush(openSet, (fScore[start], start))

	while openSet:
		current = heappop(openSet)[1]

		if current == goal:
			return reconstruct_path(cameFrom, current), fScore

		closedSet.add(current)

		for i,j in neighbors:
			neighbor = ()
			neighbor = current[0] + i, current[1] + j


			tentative_gScore = gScore[current] + dist_between(array, current, neighbor)

			if neighbor in closedSet and tentative_gScore >= gScore[neighbor]:
				continue

			
			if neighbor not in [i[1]for i in openSet] and tentative_gScore < gScore[neighbor]:
				cameFrom[neighbor] = current
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = gScore[neighbor] + 1.25*(heuristic_cost_estimate(neighbor, goal))
				heappush(openSet, (fScore[neighbor], neighbor))


	return False


def reconstruct_path(cameFrom, current):
	total_path = [current]
	while current in cameFrom:
		current = cameFrom[current]
		total_path.append(current)
	return total_path



f = open('mapfile.txt')
line = f.readline()
line = line.split(':', 1)[-1]
line = line.replace('\n', '')
l = line.split(',')
l1 = [ int(x) for x in l]
start = tuple(l1)
line = f.readline()
line = line.split(':', 1)[-1]
line = line.replace('\n', '')
l = line.split(',')
l1 = [ int(x) for x in l]
goal = tuple(l1)

ht1 = f.readline()
ht2 = f.readline()
ht3 = f.readline()
ht4 = f.readline()
ht5 = f.readline()
ht6 = f.readline()
ht7 = f.readline()
ht8 = f.readline()

grid=[]
for i in xrange(120):
	m = f.readline()
	m = re.sub(r'\s+', '', m)
	grid.append(list(m))


start_time = timeit.default_timer()
result= astar(grid, start, goal)
time_taken= timeit.default_timer() - start_time
print "Time taken is ", time_taken,"seconds"


grid[start[0]][start[1]] = 'S'
grid[goal[0]][goal[1]] = 'G'


if result:
	path,e  = result
	print "path", path
	print "----------------"
	print "path length", len(path)
	print "-----------------"
	print "cost", e[goal]
	pygame.init()
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	GREEN = (0,255,0)
	RED = (255,0,0)
	BROWN = (160,82,45)
	BLUE = (0,0,255)
	GREY = (160,160,160)
	DARK = (64,64,64)
	DARKGREEN = (51,0,51)

	WIDTH = 4
	HEIGHT = 4

	MARGIN = 1

	WINDOW_SIZE = [810,610]
	screen = pygame.display.set_mode(WINDOW_SIZE)

	pygame.display.set_caption("Weighted Astar Algorithm")

	done = False

	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			else:
				for i in xrange(len(path)):
					grid[path[i][0]][path[i][1]] = 'p'
		screen.fill(BLACK)

		for row in range(120):
			for column in range(160):
				color = WHITE
				if grid[row][column] == 'S':
					color = GREEN
				if grid[row][column] == 'G':
					color = RED
				if grid[row][column] == '1':
					color = WHITE
				if grid[row][column] == '0':
					color = DARKGREEN
				if grid[row][column] == '2':
					color = BROWN
				if grid[row][column] == 'a':
					color = GREY
				if grid[row][column] == 'b':
					color = DARK
				if grid[row][column] == 'p':
					color = BLUE

				pygame.draw.rect(screen,
							color,
							[(MARGIN + WIDTH) * column + MARGIN,
							(MARGIN + HEIGHT) * row + MARGIN,
							WIDTH,
							HEIGHT])

		time.sleep(1)
		clock.tick(60)

		pygame.display.flip()

	pygame.quit()


else:
	print "no path found"


