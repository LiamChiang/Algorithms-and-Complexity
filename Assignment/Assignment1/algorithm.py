import collections


def isConnected(hashtable, startingPoint, endingPoint):
	todoSet = set()
	visitedSet = set()
	todoSet.add(startingPoint)
	while len(todoSet) != 0:
		vertice = todoSet.pop()
		visitedSet.add(vertice)
		if hashtable[vertice] is not None:
			for neighbour in hashtable[vertice]:
				if neighbour == endingPoint:
					return True
				if neighbour not in visitedSet:
					todoSet.add(neighbour)
	return False



# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

edges, queries = [], []

for _ in range(m):
    edges.append(input().split())

q = int(input())

for _ in range(q):
    queries.append(input().split())


# for _ in range(q):
# 	connection.append('false')

# for _ in range(n):
# 	visited.append('false')
		
	
#create a hash table	
hashtable = {}

#store Set with each vertex in hashtable
for sub_array in edges:
	
	starting_point = sub_array[0]
	if starting_point in hashtable:
		the_set = hashtable[starting_point]
		the_set.add(sub_array[1])
		hashtable[starting_point] = the_set
	else:
		hashtable[starting_point] = {sub_array[1]}
		
	starting_point = sub_array[1]
	if starting_point in hashtable:
		the_set = hashtable[starting_point]
		the_set.add(sub_array[0])
		hashtable[starting_point] = the_set
	else:
		hashtable[starting_point] = {sub_array[0]}

	

for ver_edge in queries:
	start_vertex = ver_edge[0]
	end_vertex = ver_edge[1]
	print(int(isConnected(hashtable, start_vertex, end_vertex)))
				
			
			
	







# # print(queries)
# # print(collections.OrderedDict(sorted(hashtable.items())))

# # Print a `1` to stdout for each query. This section should be altered to instead print a `1` where the
# # query indicates a connection and `0` else.
# for _ in queries:
# 	if connection[queries.index(_)] is 'true':
# 		print(int(True))
# 	else:
# 		print(int(False))



