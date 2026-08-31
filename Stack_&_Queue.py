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
    def queue(self,size=1000):
        