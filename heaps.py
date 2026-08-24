class solution:
    def heaps(self):
        self.heap=[]

    def insert(self, value):
        self.heap.append(value)
        self._shiftUp(len(self.heap)-1)

    def changeValue(self, index, newValue):
        oldValue=self.heap[index]
        self.heap[index]=newValue
        if newValue>oldValue:
            self._shiftUp(index)
        else:
            self._sdhiftDown(index)
    def extractMax(self):
        if len(self.heap)==0:
            return None
        maxValue=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        self._shiftDown(0)
        return maxValue
    def isempty(self):
        return len(self.heap)==0
    def getmax(self):
        return self.heap[0] if self.heap else None
    def heapsize(self):
        return len(self.heap)

    def _shiftUp(self, index):
        while index>0:
            parent=(index-1)//2
            if self.heap[index]>self.heap[parent]:
                self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
                index=parent
            else:
                break
    def _shiftDown(self, index):
        size=len(self.heap)
        while index<size:
            left=2*index+1
            right=2*index+2
            largest=index
            if left<size and self.heap[left]>self.heap[largest]:
                largest=left
            if right<size and self.heap[right]>self.heap[largest]:
                largest=right
            if largest!=index:
                self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
                index=largest
            else:
                break

print("Heap Implementation")
heap=solution()