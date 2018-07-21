import queue

class sorting:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def __lt__(self, other):
        return self.x1 < other.x1

n = int(input())
points = []
for _ in range(n):
    x, y = map(float, input().split())
    points.append((x,y))

    
count_array = [0] * n

pq = queue.PriorityQueue()
for sort_queue in points:
    pq.put(sorting(sort_queue[0], sort_queue[1]))

results = []
while not pq.empty():
    imp = pq.get()
    results.append(imp.x2)
    
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
    
    
    
    
    
    
