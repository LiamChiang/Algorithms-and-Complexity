import queue

class X_sort:
	def __init__(self, x, y, imp):
		self.x = x
		self.y = y
		self.imp = imp
	def __lt__(self, other):
		return self.x < other.x
	
class Y_sort:
	def __init__(self, x, y, imp):
		self.x = x
		self.y = y
		self.imp = imp
	def __lt__(self, other):
		return self.y < other.y


n = int(input())
left = []
l = int(input())
for _ in range(l):
    x,y,imp = map(float, input().split())
    left.append((x,y,imp))
r = int(input())
right = []
for _ in range(r):
	x,y,imp = map(float, input().split())
	right.append((x,y,imp))
	
def merge (left, right):
	leftIndex = 0
	rightIndex = 0
	count = 0
	result = []
	while (leftIndex < len(left)) and (rightIndex < len(right)):
		# if leftIndex <= rightIndex:
		if left[leftIndex][1] < right[rightIndex][1]:
			result.append(left[leftIndex])
			leftIndex += 1
			count += 1
		else:
			right[rightIndex][2] += count
			result.append(right[rightIndex])
			rightIndex += 1
	
	result += left[leftIndex:]
	
	while rightIndex < len(right):
		# print(rightIndex)
		right[rightIndex][2] += count
		result.append(right[rightIndex])
		rightIndex += 1
				
	# print(rightIndex)
	
	return result

rpq = queue.PriorityQueue()
lpq = queue.PriorityQueue()

# sort right points with y value in ascending order
for right_result in right:
	rpq.put(Y_sort(right_result[0], right_result[1], right_result[2]))

right_sort = []
while not rpq.empty():
	r_output = rpq.get()
	right_sort.append([r_output.x, r_output.y, r_output.imp])

# sort left points with y value in ascending order
for left_result in left:
	lpq.put(Y_sort(left_result[0], left_result[1], left_result[2]))
	
left_sort = []
while not lpq.empty():
	l_output = lpq.get()
	left_sort.append([l_output.x, l_output.y, l_output.imp])


result = merge(left_sort,right_sort)	

out_pq = queue.PriorityQueue()
for final_output in result:
	out_pq.put(X_sort(final_output[0],final_output[1],final_output[2]))
	
while not out_pq.empty():
	outputs = out_pq.get()
	print(int(outputs.imp))
	
