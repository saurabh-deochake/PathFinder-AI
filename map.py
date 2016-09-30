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
		return grid	

		#for grid_line in grid:
		#	print grid_line
	"""
	def _create_highway(self, grid):
		choice = random.randint(0,3)

		if choice % 2 == 0:
			rand_x = [x for x in random.sample(range(0, 120)), 4]
			rand_y = 0
			x_max = max(rand_x)
			x_min = min(rand_x)

			if choice == 2:
				rand_y = 159

				for y_coord in range((rand_y, 0), -1):
					for step in range(1, 21):
						for x_coord in rand_x:
							if grid[x_coord][rand_y - step] == 2:
								grid[x_coord][rand_y - step] = 'b'
							else:
								grid[x_coord][rand_y - step] = 'a'
					
					arr = [0, 0, 0, 0]
					x_middle = 0
					for index in range(0,len(rand_x)):
						if rand_x[index] == x_max and x_max + 20 < 120:
							arr[index] = 2
						elif rand_x[index] == x_min and x_min - 20 >= 0:
							arr[index] = 1
						elif rand_x[index] != x_min and rand_x[index] != x_max:
							if rand_x[index] - x_min > x_max - rand_x[index]
								# When this index is closer to x_max
								if x_max - rand_x[index] > 20:
									if x_middle != 0 and x_middle > rand_x[index] :
										if x_middle > rand_x[index] + 20:
										# Checking if enough space between
										# x_middle and rand_x[index]
											if rand_x[index] - 20 > x_min:
												arr[index] = 3
											else:
												arr[index] = 2
										else:
											if rand_x[index] - 20 > x_min:
												arr[index] = 1
									elif x_middle != 0 and x_middle < rand_x[index] :
										if x_middle < rand_x[index] - 20:
										# Checking if enough space between
										# x_middle and rand_x[index]
											if rand_x[index] + 20 > x_min:
												arr[index] = 3
											else:
												arr[index] = 2
										else:
											if rand_x[index] - 20 > x_min:
												arr[index] = 1



								if x_middle == 0:
									x_middle = rand_x[index]






					rand_y = rand_y - 19
		"""

def main():
	map_obj = Map()
	map_obj._create_grid()

if __name__ == '__main__':
	main()

	
