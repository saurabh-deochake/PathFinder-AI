# CS520: Artificial Intelligence Project 1
# Contributors: Saurabh Deochake, Rohit Bobade 
# Email: {saurabh.deochake, rohit.bobade}@rutgers.edu

import random

class Map:
	def _create_grid(self):
		# Creating a grid of size 120 x160 and setting 
		# all cells as walkable
		rows, columns = 120, 160
		grid = [[1 for x in range(columns)] for y in range(rows)] 
		self._harder_to_traverse(grid)

	def _harder_to_traverse(self, grid):
		random_x_coordinates = [x for x in random.sample(range(0, 160), 8)]
		random_y_coordinates = [y for y in random.sample(range(0, 120), 8)]

		#print random_x_coordinates, random_y_coordinates
		
		
		x_min, x_max, y_min, y_max = 0,0,0,0
		for i in range(0, len(random_x_coordinates)):
			
			if random_x_coordinates[i] - 15 < 0:
				x_min = 0
				x_max = (15 - random_x_coordinates[i]) + 15 + random_x_coordinates[i]
			else:
				x_min = random_x_coordinates[i] - 15
				x_max = random_x_coordinates[i] + 15

			if random_x_coordinates[i] + 15 > 159: 
				x_max = 159
				x_min = (random_x_coordinates[i] - 15) - (15 -(159- random_x_coordinates[i]))
			#else:
				#x_max = random_x_coordinates[i] + 15
				
			if random_y_coordinates[i] - 15 < 0:
				y_min = 0
				y_max = (15 - random_y_coordinates[i]) + 15 + random_y_coordinates[i]
				
			else: 
				y_min = random_y_coordinates[i] - 15 
				y_max = random_y_coordinates[i] + 15

			if random_y_coordinates[i] + 15 > 119: 
				y_max = 119
				y_min = (random_y_coordinates[i] - 15) - (15 -(119 - random_y_coordinates[i]))
				
			for i in range(x_min, x_max+1):
				for j in range(y_min, y_max+1):
					if random.randint(0,1) == 0:
						grid[j][i] = 2	
		
		#return grid
		self._create_highway(grid)

		
	
	def _create_highway(self, grid):
		#choice = random.randint(0,3)
		choice = 2
		if choice % 2 == 0:
			rand_x = [x for x in random.sample(range(0, 120), 4)]
			rand_y = 0
			x_max = max(rand_x)
			x_min = min(rand_x)
			arr = [0, 0, 0, 0] #1 - > left, 2 -> right, 3 -> both
			if choice == 2:
				rand_y = 159
				x_middle1= -1
				x_middle2 = -1
				for x_coord in rand_x:
					if x_middle1 == -1 and x_coord != x_max and x_coord != x_min:
						x_middle1 = x_coord
					elif x_middle1 != -1 and x_coord != x_max and x_coord != x_min:
						x_middle2 = x_coord
				if x_middle2 < x_middle1:
					x_middle1, x_middle2 = x_middle2, x_middle1
				
				#so we have so far that it would be x_min, x_middle1, x_middle2, x_max

				count = 1

				for y_coord in range(rand_y, -1, -1):
					x,y = -1, y_coord
					arrMove = [0, 0, 0, 0]
					if count > 1:
						for i in range(0,len(arr)):
							if arr[i] > 0:
								#check for the probability
								if(random.sample(range(0,8), 1) > 5):
									arrMove[i] = 1

					for step in range(1, 21):
						for x_coord in range(0, len(rand_x)):
							if arr[x_coord] == -1 or arr[x_coord] == 0 or count == 1:
								y = y-1
								x = rand_x[x_coord] ### rand_x[index] to rand_x[x_coord] ?
							elif arr[x_coord] > 0 and count > 1 and arrMove[x_coord] > 0:
								#truning left or right with the probability
								if x == -1:
									x = rand_x[x_coord]
								if arr[x_coord] == 1:
									x = x -1
									y = y_coord
								elif arr[x_coord] == 2:
									x = x + 1
									y = y_coord
 								elif arr[x_coord] == 3:
 									if random.sample(range(0,2)) == 0:
 										#you are moving left
 										x = x - 1
 										y = y_coord
 									else:
 										x = x + 1
 										y = y_coord

							if grid[x][y] == 2:
								grid[x][y] = 'b'
							else:
								grid[x][y] = 'a'

					
					if count > 1 and count % 2 == 0:
						#its the round that was used to turn
						for index in range(0,len(rand_x)):
							arr[index] = -1
					elif count > 1 and count % 2 == 1:
						#it was the round that was not used to turn
						for index in range(0,len(rand_x)):
							arr[index] = 0

					count = count + 1					
					for index in range(0,len(rand_x)):
						if arr[index] == -1:
							break
						elif rand_x[index] == x_max and x_max + 20 < 120:
							arr[index] = 2
						elif rand_x[index] == x_min and x_min - 20 >= 0:
							arr[index] = 1
						elif rand_x[index] == x_middle1:
							#the rand_x is in the middle, the one closer to x_min
							if x_min < x_middle1 - 20:
								#can trun left
								arr[index] = 1
							elif x_middle1 + 20 < x_middle2:
								arr[index] = 2 
						elif rand_x[index] == x_middle2:
							#the rand_x is in the middle and the one which is closer to the x_max
							if x_max > x_middle2 + 20:
								#can trun left
								arr[index] = 2
							if x_middle1 + 20 < x_middle2:
								if arr[index] == 2:
									arr[index] = 3
								else:
									arr[index] = 1 


					rand_y = rand_y - 19
	

def main():
	map_obj = Map()
	map_obj._create_grid()

if __name__ == '__main__':
	main()

	
