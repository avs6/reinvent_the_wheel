def dijsktra(graph, start):
	distance = {}
	visited = {}
	for k, v in graph.iteritems():
		visited[k] =  False
	visited[start] = True
	all_visited = False
	while(not all_visited):
		#look at neighbors
		for k, v in graph[start].iteritems():
			if k not in distance:
				distance[k] = v
			elif distance[k] > v + distance[start]:
				distance[k] = v + distance[start]
		temp = {}
		for k,v in visited.iteritems():
			if (v == False) & (k in distance):
				temp[k] = distance[k]
		if any(temp):
			minimum = min(temp, key=temp.get)
		start = minimum
		visited[minimum] = True
		all_visited = all_true(visited)
		print distance
		print visited
	return distance, visited
def all_true(visited):
	for k,v  in visited.iteritems():
		if v == False:
			return False
	return True

graph = {'a' : {'b' : 3, 'c' : 4}, 'b' : {'d':11}, 'c':{'d':1}, 'd':{'b' : 1}}
distance, visited = dijsktra(graph, 'a')
print "-----Final------"
print distance
print visited