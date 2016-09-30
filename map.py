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

		print random_x_coordinates, random_y_coordinates
		
		
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
				
			#else: 
				#y_max = random_y_coordinates[i] + 15

				
			print [x_min, y_min, x_max, y_max]

		
		#print random_coordinates[0], random_coordinates[1]

		'''for k in range(1, 16):
			grid[random_coordinates[0]-k][random_coordinates[1]] = 2
			for grid_line in grid:
				print grid_line
		'''

		




def main():
	map_obj = Map()
	map_obj._create_grid()

if __name__ == '__main__':
	main()

	
