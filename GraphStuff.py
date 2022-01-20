from IndexMinPQ import IndexMinPQ

class Point():
	idCountP = 0

	def __init__(self, name):
		self.name = name
		self.id = Point.idCountP
		Point.idCountP += 1

class Edge():
	
	idCountE = 0
	def __init__(self, pt1: Point,pt2: Point,weight: int,name: str):
		#curpt aka pt1 is the starting pt
		#otherpt aka pt2 is the one in the table
		self.curpt = pt1
		self.otherpt = pt2
		self.weight = weight
		self.name = name
		self.id = Edge.idCountE
		Edge.idCountE += 1
		
	def getOther(self,pt: Point) -> Point: 
		if pt == self.pt1:
			return pt2
		elif pt == self.pt2:
			return pt1
		else:
			print("incorrect input")
			return None


class Graph():
	
	pointCount = 0

	def __init__(self,pointsList):
		self.graph = [[] for x in range(len(pointsList))] #adj matrix
		self.numPoints = len(pointsList)
		self.ptsList = pointsList
		self.table = {} 
		for pt in pointsList:
			self.table[pt.name] = Graph.pointCount
			Graph.pointCount += 1


	def addPoint(self, pt: Point):
		temp = []
		self.graph.append(temp)
		self.table[pt.name] = Graph.pointCount
		Graph.pointCount += 1



	def addEdge(self, pt1: Point, pt2: Point, weight, name):
		pt1Num = self.table[pt1.name]
		pt2Num = self.table[pt2.name]

		#point one
		newEdge = Edge(pt1, pt2, weight, name)
		self.graph[pt1Num].append(newEdge) 

		#point two
		newEdge1 = Edge(pt2, pt1, weight, name)
		self.graph[pt2Num].append(newEdge1) 


	def shortestPath(self, pt1: Point, pt2: Point) -> float:
		
		x = self.table[pt1.name]
		y = self.table[pt2.name]

		print("x: %d  y: %d" %(x,y))
		size = self.numPoints
		distPQ = IndexMinPQ(size)
		dist = [None for x in range(size)]
		via = [None for x in range(size)]
		visited = [False for x in range(size)]

		cur = x

		distPQ.insert(x,0.0)
		dist[x] = 0.0


		while not visited[y]:
			print("\ncur= %d" %cur)
			for i in self.graph[cur]:
				temp = self.table[i.otherpt.name]
				print(temp)
				w = i.weight

				if dist[temp] is None:
					dist[temp] = dist[cur] + w
					distPQ.insert(temp,dist[temp])
					via[temp] = cur
				else:
					if dist[temp] > (dist[cur] + w):
						dist[temp] = dist[cur] + w
						distPQ.changeKey(temp,dist[temp])
						via[temp] = cur


			visited[cur] = True
			distPQ.delete(cur)

		
			print(dist)
			print(via)
		
			if(cur == y):
				break

			if(distPQ.n != 0):
				cur = distPQ.minIndex()
			else:
				print("Something went wrong")
				return None

		
		v = via[y]
		path = [self.ptsList[y].name, self.ptsList[v].name]
		while v!= x:
			v = via[v]
			path.append(self.ptsList[v].name)
	
		return path
