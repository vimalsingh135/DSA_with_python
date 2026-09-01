# implementation of stack data structure in python
class ArrayStack:
    def __init__(self, size=1000):  # constructor to initialize the stack with a given size
        self.stackArray = [0] * size
        self.capacity = size
        self.Indextop = -1  # initializing the top of the stack to -1

    def push(self, x):
        if self.Indextop >= self.capacity - 1:
            print("stack overflow")
            return
        self.Indextop += 1
        self.stackArray[self.Indextop] = x

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return -1
        top_element = self.stackArray[self.Indextop]
        self.Indextop -= 1
        return top_element

    def top(self):
        if self.isEmpty():
            print("the stack is empty")
            return -1
        return self.stackArray[self.Indextop]

    def isEmpty(self):
        return self.Indextop == -1


# Main function
if __name__ == "__main__":
    stack = ArrayStack()
    commands = ["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(stack.pop(), end=" ")
        elif commands[i] == "top":
            print(stack.top(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "false", end=" ")
        elif commands[i] == "ArrayStack":
            print("null", end=" ")

# implementation of queue in data stucture in python
class ArrayQueue:
    def __init__(self):
        self.size=[0]*10
        self.start=-1
        self.end=-1
        self.currsize=0
        self.maxsize=10
        

    def enqueue(self,x):

        if self.currsize==self.maxsize:
            print("the queue is full/exiting...")
            exit(1)
        if self.end==-1:
            self.start=0
            self.end=0

        else:
            self.end=(self.end+1)%self.maxsize
        self.size[self.end]=x
        self.currsize+=1

    def dequeue(self):
        if self.currsize==0:
            print("the queue is empty/existing...")
            exit(1)
        dequeued_element=self.size[self.start]

        if self.start== self.end:
            self.start = -1
            self.end = -1
        else:
            self.start=(self.start+1)%self.maxsize
        self.currsize-=1
        return dequeued_element

    def peek(self):
        if self.currsize==-1:
            print("the queue is empty/existing...")
            exit(1)
        return (self.size[self.start])

    def _isempty(self):
        return self.currsize==0


if __name__ == "__main__":
    queue = ArrayQueue()
    commands = ["ArrayQueue", "enqueue", "dequeue", "peek", "dequeue", "isEmpty"]
    inputs = [[], [5], [10], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "enqueue":
            queue.enqueue(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "dequeue":
            print(queue.dequeue(), end=" ")
        elif commands[i] == "peek":
            print(queue.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if queue._isempty() else "false", end=" ")
        elif commands[i] == "ArrayQueue":
            print("null", end=" ")

        