# CS520: Artificial Intelligence Project 1
# Contributors: Saurabh Deochake, Rohit Bobade 
# Email: {saurabh.deochake, rohit.bobade}@rutgers.edu

import random
import math
class Map:
	
	def __init__(self):
		# Creating a grid of size 120 x160 and setting 
		# all cells as walkable
		rows, columns = 120, 160 
		grid = [['1' for x in range(columns)] for y in range(rows)] 
		
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
						grid[j][i] = '2'	
		
		#return grid
		self._create_highway(grid, random_x_coordinates, random_y_coordinates)

	def _helper_create_highway_horizontal(self, grid, yVal, xVal, check_val, add):
		finished = 0 #this variable will keep track of when a highway touched
		finish = [0, 0, 0, 0]
		arr = [0, 0, 0, 0] #1 - > left, 2 -> right, 3 -> both
		count = 1
		while (finished < 4):
			#print "3 xVal :", xVal, " yVal: ", yVal
			arrMove = [0, 0, 0, 0]
			if count > 1:
				for i in range(0,len(arr)):
					if arr[i] > 0:
						#check for the probability
						if(random.sample(range(0,8), 1) > 5):
							arrMove[i] = 1
			#print "*************** COUNT: ", count, " arrMove", arrMove, " arr", arr

			for x_coord in range(0, len(xVal)):
				#print "4 xVal :", xVal, " yVal: ", yVal
				#print "***********************X COORDINATE ", xVal[x_coord], " Y COORDINATE: ", yVal[x_coord]
				#print "FINISHED: ", finish
				x, y = xVal[x_coord], yVal[x_coord]
				#check for #3 as an input
				if arr[x_coord] == 3:
						if random.randint(0,1) == 0:
						#you are moving left
							arr[x_coord] = 1
						else:
							arr[x_coord] = 2

				for step in range(1, 21):
					if finish[x_coord] == 1:
						break
					if arr[x_coord] == -1 or arr[x_coord] == 0 or count == 1:
						y = y + add
						x = xVal[x_coord] ### rand_x[index] to rand_x[x_coord] ?
					elif arr[x_coord] > 0 and count > 1 and arrMove[x_coord] > 0:
						#truning left or right with the probability	
						if x == -1:
							x = xVal[x_coord]
						if arr[x_coord] == 1:
							x = x -1
							y = yVal[x_coord]
						elif arr[x_coord] == 2:
							x = x + 1
							y = yVal[x_coord]

					if grid[x][y] == '2':
						xVal[x_coord] = x
						yVal[x_coord] = y
						#print xVal[x_coord], " ", yVal[x_coord], " ", grid[x][y], " ", 'b'
						grid[x][y] = 'b'
					else:
						xVal[x_coord] = x
						yVal[x_coord] = y
						#print xVal[x_coord], " ", yVal[x_coord], " ", grid[x][y], " ", 'a'
						grid[x][y] = 'a'
					#check to be done
					if xVal[x_coord] == 0 or yVal[x_coord] == check_val or xVal[x_coord] == 119:
						finished = finished + 1
						finish[x_coord] = 1

			#print "1 xVal :", xVal, " yVal: ", yVal
			if count > 1 and count % 2 == 0:
				#its the round that was used to turn
				for index in range(0,len(xVal)):
					arr[index] = -1
			elif count > 1 and count % 2 == 1:
				#it was the round that was not used to turn
				for index in range(0,len(xVal)):
					arr[index] = 0

			count = count + 1					
			#rearrange all the values
			x_max = max(xVal)
			x_min = min(xVal)
			x_middle1= -1
			x_middle2 = -1
			for x_coord in xVal:
				if x_middle1 == -1 and x_coord != x_max and x_coord != x_min:
					x_middle1 = x_coord
				elif x_middle1 != -1 and x_coord != x_max and x_coord != x_min:
					x_middle2 = x_coord
			if x_middle2 < x_middle1:
				x_middle1, x_middle2 = x_middle2, x_middle1
			#so we have so far that it would be x_min, x_middle1, x_middle2, x_max
			for index in range(0,len(xVal)):
				if arr[index] == -1:
					break
				elif xVal[index] == x_max and x_max + 20 < 120:
					arr[index] = 2
				elif xVal[index] == x_min and x_min - 20 >= 0:
					arr[index] = 1
				elif xVal[index] == x_middle1:
					#the rand_x is in the middle, the one closer to x_min
					if x_min < x_middle1 - 20:
						#can trun left
						arr[index] = 1
					elif x_middle1 + 20 < x_middle2:
						arr[index] = 2 
				elif xVal[index] == x_middle2:
					#the rand_x is in the middle and the one which is closer to the x_max
					if x_max > x_middle2 + 20:
						#can trun left
						arr[index] = 2
					if x_middle1 + 20 < x_middle2:
						if arr[index] == 2:
							arr[index] = 3
						else:
							arr[index] = 1 
	


	def _helper_create_highway_vertical(self, grid, yVal, xVal, check_val, add):
		finished = 0 #this variable will keep track of when a highway touched
		finish = [0, 0, 0, 0]
		arr = [0, 0, 0, 0] #1 - > left, 2 -> right, 3 -> both
		count = 1
		while (finished < 4):
			#print "3 xVal :", xVal, " yVal: ", yVal
			arrMove = [0, 0, 0, 0]
			if count > 1:
				for i in range(0,len(arr)):
					if arr[i] > 0:
						#check for the probability
						if(random.sample(range(0,8), 1) > 5):
							arrMove[i] = 1
			#print "*************** COUNT: ", count, " arrMove", arrMove, " arr", arr

			for x_coord in range(0, len(yVal)):
				#print "4 xVal :", xVal, " yVal: ", yVal
				#print "***********************X COORDINATE ", xVal[x_coord], " Y COORDINATE: ", yVal[x_coord]
				#print "FINISHED: ", finish
				x, y = xVal[x_coord], yVal[x_coord]
				#check for #3 as an input
				if arr[x_coord] == 3:
						if random.randint(0,1) == 0:
						#you are moving left
							arr[x_coord] = 1
						else:
							arr[x_coord] = 2

				for step in range(1, 21):
					if finish[x_coord] == 1:
						break
					if arr[x_coord] == -1 or arr[x_coord] == 0 or count == 1:
						x = x + add
						y = yVal[x_coord] ### rand_x[index] to rand_x[x_coord] ?
					elif arr[x_coord] > 0 and count > 1 and arrMove[x_coord] > 0:
						#truning left or right with the probability	
						if y == -1:
							y = yVal[x_coord]
						if arr[x_coord] == 1:
							y = y -1
							x = xVal[x_coord]
						elif arr[x_coord] == 2:
							y = y + 1
							x = xVal[x_coord]

					if grid[x][y] == '2':
						xVal[x_coord] = x
						yVal[x_coord] = y
						#print xVal[x_coord], " ", yVal[x_coord], " ", grid[x][y], " ", 'b'
						grid[x][y] = 'b'
					else:
						xVal[x_coord] = x
						yVal[x_coord] = y
						#print xVal[x_coord], " ", yVal[x_coord], " ", grid[x][y], " ", 'a'
						grid[x][y] = 'a'
					#check to be done
					if yVal[x_coord] == 0 or xVal[x_coord] == check_val or yVal[x_coord] == 159:
						finished = finished + 1
						finish[x_coord] = 1

			#print "1 xVal :", xVal, " yVal: ", yVal
			if count > 1 and count % 2 == 0:
				#its the round that was used to turn
				for index in range(0,len(xVal)):
					arr[index] = -1
			elif count > 1 and count % 2 == 1:
				#it was the round that was not used to turn
				for index in range(0,len(xVal)):
					arr[index] = 0

			count = count + 1					
			#rearrange all the values
			x_max = max(yVal)
			x_min = min(yVal)
			x_middle1= -1
			x_middle2 = -1
			for y_coord in yVal:
				if x_middle1 == -1 and y_coord != x_max and y_coord != x_min:
					x_middle1 = y_coord
				elif x_middle1 != -1 and y_coord != x_max and y_coord != x_min:
					x_middle2 = y_coord
			if x_middle2 < x_middle1:
				x_middle1, x_middle2 = x_middle2, x_middle1
			#so we have so far that it would be x_min, x_middle1, x_middle2, x_max
			for index in range(0,len(yVal)):
				if arr[index] == -1:
					break
				elif yVal[index] == x_max and x_max + 20 < 159:
					arr[index] = 2
				elif yVal[index] == x_min and x_min - 20 >= 0:
					arr[index] = 1
				elif yVal[index] == x_middle1:
					#the rand_x is in the middle, the one closer to x_min
					if x_min < x_middle1 - 20:
						#can trun left
						arr[index] = 1
					elif x_middle1 + 20 < x_middle2:
						arr[index] = 2 
				elif yVal[index] == x_middle2:
					#the rand_x is in the middle and the one which is closer to the x_max
					if x_max > x_middle2 + 20:
						#can trun left
						arr[index] = 2
					if x_middle1 + 20 < x_middle2:
						if arr[index] == 2:
							arr[index] = 3
						else:
							arr[index] = 1 



	def _create_highway(self, grid, random_x_coordinates, random_y_coordinates):
		choice = random.randint(0,3)
		if choice % 2 == 0:
			rand_x = [x for x in random.sample(range(0, 120), 4)]
			if choice == 2:
				#this will have current value for x and y
				xVal = [x for x in rand_x]
				yVal = [159, 159, 159, 159]
				self._helper_create_highway_horizontal(grid, yVal, xVal, 0, -1)
			if choice == 0:
				#this will have current value for x and y
				xVal = [x for x in rand_x]
				yVal = [0, 0, 0, 0]
				self._helper_create_highway_horizontal(grid, yVal, xVal, 159, 1)
		
		else: 
			#the value is for vertical
			rand_y = [x for x in random.sample(range(0, 160), 4)]
			if choice == 1:
				#this will have current value for x and y
				yVal = [x for x in rand_y]
				xVal = [0, 0, 0, 0]
				self._helper_create_highway_vertical(grid, yVal, xVal, 119, 1)
			if choice == 3:
				#this will have current value for x and y
				yVal = [x for x in rand_y]
				xVal = [119, 119, 119, 119]
				self._helper_create_highway_vertical(grid, yVal, xVal, 0, -1)


		#self._write_grid(grid)
		grid = self._create_blocked_cells(grid)
		self._set_start_end_nodes(grid,(choice%2), random_x_coordinates, random_y_coordinates)

	def _create_blocked_cells(self, grid):
		
		i = 0
		while (i < 3840):
			x = random.sample(range(0, 120), 1)[0]
			y = random.sample(range(0, 160), 1)[0]

			if grid[x][y] == 'a' or grid[x][y] == 'b' or grid[x][y] == '2' or grid[x][y] == '0':
				continue
			else:
				grid[x][y] = '0'
				i = i + 1

		return grid


	def _set_start_end_nodes(self, grid, v, random_x_coordinates, random_y_coordinates):
		if v == 1:
			#starting node
			row_choice_s, col_choice_s = random.randint(0,20), random.randint(0,159)
			#gaol node
			row_choice_g, col_choice_g = random.randint((119-row_choice_s),119), random.randint(0,159)
			check = math.hypot(row_choice_s - row_choice_g, col_choice_s - col_choice_g)

			while(check < 100) or (grid[row_choice_s][col_choice_s] != '1' and grid[row_choice_s][col_choice_s] != '2') or (grid[row_choice_g][col_choice_g] != '1' and grid[row_choice_g][col_choice_g] != '2'):
				row_choice_s, col_choice_s = random.randint(0,20), random.randint(0,159)
				row_choice_g, col_choice_g = random.randint((119-row_choice_s),119), random.randint(0,159)
				check = math.hypot(row_choice_s - row_choice_g, col_choice_s - col_choice_g)

			grid[row_choice_s][col_choice_s], grid[row_choice_g][col_choice_g] = '1','1'
		else:
			#starting node
			col_choice_s, row_choice_s = random.randint(0,20), random.randint(0,119)
			#gaol node
			col_choice_g, row_choice_g = random.randint((159-col_choice_s),159), random.randint(0,119)
			check = math.hypot(row_choice_s - row_choice_g, col_choice_s - col_choice_g)
			
			while(check < 100) or (grid[row_choice_s][col_choice_s] != '1' and grid[row_choice_s][col_choice_s] != '2') or (grid[row_choice_g][col_choice_g] != '1' and grid[row_choice_g][col_choice_g] != '2'):
				col_choice_s, row_choice_s = random.randint(0,20), random.randint(0,119)
				col_choice_g, row_choice_g = random.randint((159-col_choice_s),159), random.randint(0,119)
				check = math.hypot(row_choice_s - row_choice_g, col_choice_s - col_choice_g)
			
			grid[row_choice_s][col_choice_s], grid[row_choice_g][col_choice_g] = 'S','G'

		self._write_grid(grid, row_choice_s, col_choice_s, row_choice_g, col_choice_g, random_x_coordinates, random_y_coordinates)

	def _write_grid(self, grid, row_choice_s, col_choice_s, row_choice_g, col_choice_g, random_x_coordinates, random_y_coordinates):
		f = open("mapfile.txt", 'w')

		start = "S: " + str(row_choice_s) + ", " + str(col_choice_s) + "\n"
		end = "G: " + str(row_choice_g) + ", "  + str(col_choice_g) + "\n"
		f.write(start)
		f.write(end)
		#writing all the points
		for i in range(0, len(random_x_coordinates)):
			string = "HT" + str(i+1) + ": " + str(random_x_coordinates[i]) + ", " + str(random_y_coordinates[i]) + "\n"
			f.write(string)
		#writing the grid
		for grid_line in grid:
			val = str(grid_line)
			val = val[1:-1]
			val = val.replace(",", "")
			val = val.replace("'", "")
			val = val + "\n"
			f.write(val)
		f.close()

def main():
	map_obj = Map()

if __name__ == '__main__':
	main()

	