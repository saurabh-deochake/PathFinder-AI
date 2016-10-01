from collections import defaultdict
from heapq import *
import math
from pandas import *

def heuristic_cost_estimate(a, b):
    # return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def dist_between(array,current,neighbor):
    if neighbor[0] >= 0 and neighbor[0] < len(array):
        if neighbor[1] >= 0 and neighbor[1] < len(array[0]): 
            if array[current[0]][current[1]] == array[neighbor[0]][neighbor[1]] == 1:
                if round(math.sqrt((neighbor[0]-current[0]) ** 2 + (neighbor[1]-current[1]) ** 2),2) == 1.41:
                    return math.sqrt(2)
                else:
                    return 1
            elif array[current[0]][current[1]] == array[neighbor[0]][neighbor[1]] == 2:
                if round(math.sqrt((neighbor[0]-current[0]) ** 2 + (neighbor[1]-current[1]) ** 2),2) == 1.41:
                    return math.sqrt(8)
                else:
                    return 2
            elif array[current[0]][current[1]] == 1 and array[neighbor[0]][neighbor[1]] == 2:
                if round(math.sqrt((neighbor[0]-current[0]) ** 2 + (neighbor[1]-current[1]) ** 2),2) == 1.41:
                    return ((math.sqrt(2) + math.sqrt(8))/2)
                else:
                    return 1.5
            elif  array[current[0]][current[1]] == 2 and array[neighbor[0]][neighbor[1]] == 1:
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
            elif array[current[0]][current[1]] == 1 and array[neighbor[0]][neighbor[1]] == 'a':
                return 0.25
            elif array[current[0]][current[1]] == 'a' and array[neighbor[0]][neighbor[1]] == 1:
                return 0.25
            elif array[current[0]][current[1]] == 2 and array[neighbor[0]][neighbor[1]] == 'b':
                return 0.5
            elif array[current[0]][current[1]] == 'b' and array[neighbor[0]][neighbor[1]] == 2:
                return 0.5
            elif array[current[0]][current[1]] == 1 and array[neighbor[0]][neighbor[1]] == 'b':
                return 0.375
            elif array[current[0]][current[1]] == 'b' and array[neighbor[0]][neighbor[1]] == 1:
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
    			fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)
    			heappush(openSet, (fScore[neighbor], neighbor))


    return False


def reconstruct_path(cameFrom, current):
	total_path = [current]
	while current in cameFrom:
		current = cameFrom[current]
		total_path.append(current)
	return total_path

map= [
[1,1,'a',1,0,0,0],
[1,1,'a',1,0,0,0],
[0,1,'a',0,2,2,0],
[0,0,'a',1,2,2,1]
]

start = (0,0)
goal = (3,6)
a= astar(map, start, goal)


if a:
	d,e  = a
	print "path", d
	print "----------------"
	print "cost", e[goal]
else:
	print "no path"

for x,y in d:
    map[x][y] = 3

map[start[0]][start[1]] = 3
print "----------------"
print DataFrame(map)