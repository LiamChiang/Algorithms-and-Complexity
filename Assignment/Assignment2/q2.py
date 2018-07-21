import queue

class merged_sort:
	def __init__(self, x1, x2):
		self.x1 = x1
		self.x2 = x2
	def __lt__(self, other):
		return self.x1 < other.x1


n = int(input())
left = []
l = int(input())
for _ in range(l):
    x,y = map(float, input().split()[:2])
    left.append((x,y))
r = int(input())
right = []
for _ in range(r):
	x,y = map(float, input().split()[:2])
	right.append((x,y))

count_array = [0] * (l + r)
merged_array = left + right

pq = queue.PriorityQueue()
for result in merged_array:
	pq.put(merged_sort(result[0], result[1]))

results = []
while not pq.empty():
	imp = pq.get()
	results.append(imp.x2)
	
# print(results)

count = 0
for i in range(len(results)):
	for j in range(i+1):
		if results[i] > results[j]:
			if results[i] > results[j]:
				count += 1
	count_array[i] = count
	count = 0


for _ in range(len(count_array)):
	print(count_array[_])


