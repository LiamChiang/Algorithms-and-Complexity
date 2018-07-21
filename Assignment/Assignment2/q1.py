import queue

class importance:
	def __init__(self, count):
		self.count = count
	def __lt__(self, other):
		return self.count < other.count
	
	
n = int(input())
points = []
for _ in range(n):
    p = float(input())
    points.append(p)
	
count_array = [0] * n
count = 0
#spend O(n^2)
for i in range(len(points)):
	for point2 in points:
		if points[i] != point2:
			if points[i] > point2:
				count += 1
	count_array[i] = count
	count = 0
	
pq = queue.PriorityQueue()
# spend O(n log n)
for counts in count_array:
	pq.put(importance(counts))
	
while not pq.empty():
	imp = pq.get()
	print(imp.count)
