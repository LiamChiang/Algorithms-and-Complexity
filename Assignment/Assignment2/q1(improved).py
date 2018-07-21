import queue

class Point:
	def __init__(self, value):
		self.value = value
	
	def __lt__(self, other):
		return self.value < other.value

class Importance:
	def __init__(self, point, value):
		self.point = point
		self.value = value
	
	def __lt__(self, other):
		return self.value < other.value

class ReversedPriorityQueue(queue.PriorityQueue):
	def put(self, point):
		point.value *= -1
		queue.PriorityQueue.put(self, point)
	
	def get(self):
		point = queue.PriorityQueue.get(self)
		point.value *= -1
		return point
		
# reversed priority queue
rpq = ReversedPriorityQueue()
		
n = int(input())
for _ in range(n):
    p = float(input())
    rpq.put(Point(p))

importance_hash_map = {}
importance_count_hash_map = {}

while not rpq.empty():
	max_point = rpq.get()
	if max_point.value in importance_hash_map:
		importance_hash_map[max_point.value] -= 1
		importance_count_hash_map[max_point.value] += 1
	else:
		importance_hash_map[max_point.value] = rpq.qsize()
		importance_count_hash_map[max_point.value] = 1
	
pq = queue.PriorityQueue()

keys = importance_hash_map.keys()
for key in keys:
	pq.put(Importance(key, importance_hash_map[key]))
	
while not pq.empty():
	imp = pq.get()
	cnt = importance_count_hash_map[imp.point]
	while cnt > 0:
		print(imp.value)
		cnt -= 1
