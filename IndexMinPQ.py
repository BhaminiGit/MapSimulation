
#for floata
class IndexMinPQ():

    def __init__(self,max):
        self.maxN = max
        self.n = 0
        self.keys = [0.0 for x in range(max +1)]
        self.pq = [0 for x in range(max + 1)]
        self.qp = [-1 for x in range(max + 1)]
        
    def isEmpty(self) -> bool:
    	return self.n == 0


    def contains(self,i : int) -> bool:
     	return self.qp[i] != -1
     
    def size(self) -> int:
    	return self.n

    def insert(self,i: int, key: float):
    	self.n += 1
    	self.qp[i] = self.n
    	self.pq[self.n] = i
    	self.keys[i] = key
    	self.swim(self.n,)

    def minIndex(self) -> int:
    	if self.n == 0:
    		return None
    	else:
    		return self.pq[1]

    def minKey(self) -> float:
    	if self.n == 0:
    		return None
    	else:
    		return self.keys[pq[1]]

    def delMin(self) -> int:
    	if self.n == 0:
    		return None
    	min = self.pq[1]
    	self.exch(1,self.n)
    	self.n -= 1
    	self.sink(1)
    	self.qp[min] = -1
    	self.keys[min] = None
    	self.pq[self.n+1] = -1
    	return min


    def keyOf(self,i: int) -> float:
    	return self.keys[i]


    def changeKey(self,i: int, key: float):
    	self.keys[i] = keys
    	self.swim(self.qp[i])
    	self.sink(self.qp[i])


    def decreaseKey(self, i: int, key: float):
        self.keys[i] = key
        self.swim(self.qp[i])

    

   
    def increaseKey(self, i: int, key: float):
        self.keys[i] = key
        self.sink(self.qp[i])
    

   
    def delete(self, i: int):
        index = self.qp[i]
        self.exch(index, self.n)
        self.n -= 1
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1
    

	#some helper functions########################################################
    def greater(self, i:int, j:int) -> bool:
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i:int, j:int):
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j


    def swim(self, k:int):
        while k<1 and self.greater(k/2,k):
            self.exch(k,k/2)
            k = k/2

    def sink(self, k: int):
        while 2*k <= self.n:
            j = 2*k
            if j<self.n and self.greater(j,j+1):
                j+=1
            if not self.greater(k,j):
                break
            self.exch(k,j)
            k= j

###################################################################################
class IllegalArgumentError(ValueError):
    pass
