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
		print [x % 120 for x in random.sample(range(0, 159), 16)]


def main():
	map_obj = Map()
	map_obj._create_grid()

if __name__ == '__main__':
	main()

	
