from GraphStuff import Point, Edge, Graph 


class ClientClass:

	def main():
		
		
		aPt = Point("A")
		bPt = Point("B")
		cPt = Point("C")
		dPt = Point("D")
		ePt = Point("E")
		fPt = Point("F")
		# gPt = Point("G")
		# hPt = Point("H")
		# iPt = Point("I")
		# jPt = Point("J")
		# kPt = Point("K")

		pts = [aPt, bPt, cPt, dPt, ePt, fPt] #, hPt,gPt, iPt, jPt, kPt
		
		myGraph = Graph(pts)

		#(self, pt1: Point, pt2: Point, weight, name):

		myGraph.addEdge(aPt,bPt,2,"line1")
		myGraph.addEdge(aPt,dPt,4,"line2")
		myGraph.addEdge(bPt,dPt,6,"line3")
		myGraph.addEdge(bPt,fPt,8,"line4")
		myGraph.addEdge(cPt,dPt,10,"line5")
		myGraph.addEdge(cPt,ePt,12,"line6")
		myGraph.addEdge(cPt,fPt,14,"line7")
		myGraph.addEdge(dPt,ePt,16,"line8")
		
		print(myGraph.shortestPath(fPt,aPt))

		#count = 0
		#for u in myGraph.graph:
		#	for y in u:
		#		print(myGraph.table[y.otherpt.name],end="")
		#	print()
		#print("hello")
															
		

	if __name__ == '__main__':
		main()