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
    