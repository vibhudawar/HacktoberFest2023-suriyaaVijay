# import library for min heap
import heapq
from typing import List

# Node class
	# contains the value of the current node
	# contains the row number of the current node
	# in the matrix
	# contains the column number of the current
	# node in the matrix
class Node:
	def __init__(self, data: int, row: int, col: int):
		self.data = data
		self.row = row
		self.col = col
	def __lt__(self, other):
		return self.data < other.data

# Solution class contains the main logic to find median
class Solution:
	# median function
	def median(self, matrix, R, C):
		# minheap is a priority queue implemented using min
		# heap data structure. It stores the nodes in
		# ascending order based on their values.
		minheap = []
		# count variable to keep track of the
		# number of nodes processed so far
		count = 0
		# median variable to store the median value in the
		# end medianindex is the index of the median in the
		# matrix
		median = -1
		medianindex = (R * C) // 2

		# Push the first elements of each row in the min
		# heap
		for i in range(R):
			temp = Node(matrix[i][0], i, 0)
			heapq.heappush(minheap, temp)

		# Repeat until we reach the medianindex
		while count <= medianindex:
			top = heapq.heappop(minheap) # remove the node with
								# the smallest value from
								# the min heap
			row = top.row
			col = top.col
			median = top.data

			count += 1
			# if the current node is not the last element
			# in its row, push the next element from the
			# same row into the min heap
			if col + 1 < C:
				col += 1
				temp = Node(matrix[row][col], row, col)
				heapq.heappush(minheap, temp)

		return median

# Main class contains the main method
if __name__ == "__main__":
	r = 3
	c = 3
	matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]

	obj = Solution()
	print(obj.median(matrix, r, c))
