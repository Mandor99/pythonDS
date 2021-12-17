# write Stack class with a certain size of [] with 5 methods [push, pop, isEmpty, print, peek]

class Stack:
    def __init__(self, maxSize):
        self.data = []
        self.maxSize = maxSize

    def isEmpty(self):
        return self.data == []

    def push(self, ele):
        if self.maxSize == len(self.data):
            print('stack is full!!')
        else:
            self.data.append(ele)

    def pop(self):
        if self.isEmpty():
            return 'stack is empty'
        else:
            self.data.pop()

    def printStack(self):
        # print(self.data)
        for item in self.data:
            print(item)

    def peek(self):
        if len(self.data > 0):
            return self.data[len(self.data) - 1]
        else:
            return None
