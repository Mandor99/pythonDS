class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.maxSize

    def enqueue(self, val):  # add to end
        if self.isFull():
            print('queue is Full!')
        else:
            self.queue.append(val)

    def dequeue(self):  # remove from end
        if self.isEmpty():
            print('queue is empty!')
        else:
            removed = self.queue.pop(0)
            print(removed)

    def printQueue(self):
        print(self.queue)
        # for i in range(len(self.queue)):
        #     print(self.queue[i], end=' ')


# ############################################ #

class CircularQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.queue = []
        self.head = 0
        self.tail = -1
        self.size = 0
        for el in range(maxSize):
            self.queue.append(None)

    def isEmpty(self):
        # return self.head == 0 and self.tail == -1
        return self.size == 0

    def isFull(self):
        # return self.head == self.tail and (self.tail+1)%self.maxSize != -1 or self.head == 0 and self.tail == self.maxSize - 1
        return self.size == self.maxSize

    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[self.head]

    def rear(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[self.tail]

    def enqueue(self, val):
        if self.isFull():
            return 'queue is Full!'
        else:
            self.tail = (self.tail + 1) % self.maxSize
            self.queue[self.tail] = val
            self.size += 1
            return 'done'

    def dequeue(self):
        if self.isEmpty():
            return 'queue is empty!'
        # if self.head == self.tail:
        #     self.queue[self.tail] = None
        #     self.head = 0
        #     self.tail = -1
        else:
            removed = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.maxSize
            self.size -= 1
            return removed

    def printQueue(self):
        print(self.queue)
