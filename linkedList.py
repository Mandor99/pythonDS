# linkedList ==>>> [1. isEmpty-2. search-3. print-4. add(start, end, position)-5. remove(start, end, position) ]
# linkedList ==>>>

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def printList(self):
        current = self.head
        while current is not None:
            print(current.val, end=' ')
            current = current.next

    def search(self, val):
        current = self.head
        exist = False
        while current is not None:
            if current.val == val:
                exist = True
                break
            else:
                current = current.next
        return exist

    def addStart(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode

    def addEnd(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

    def addAfter(self, prevVal, val):
        if self.search(prevVal):
            current = self.head
            while current.val != prevVal:
                current = current.next
            newNode = Node(val)
            newNode.next = current.next
            current.next = newNode
        else:
            print('previous node value is not exist1!!')

    def removeStart(self):
        if self.isEmpty():
            return 'list is empty!!'
        else:
            removedVal = self.head
            self.head = self.head.next
            return removedVal

    def removeEnd(self):
        if self.isEmpty():
            return 'list is empty!!'
        else:
            removed = self.head
            newTail = removed
            while removed.next is not None:
                newTail = removed
                removed = removed.next
            self.tail = newTail
            self.tail.next = None
        return removed

    def remove(self, val):
        if self.search(val):
            prev = self.head
            removed = prev.next
            while removed.val != val:
                prev = removed
                removed = removed.next
            prev.next = removed.next
        else:
            return 'item not found!'
