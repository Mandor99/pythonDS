# print('this \n to \tmake new line\'s')
# name = input("inter your name: ")
# age = input("inter your age: ")
# print('hello ' + name + ' your age is ' + age)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]
# list4 = [10, 11, 12]
# list1.extend(list2)
# print(list1)
# list2 += list3
# print(list2)
# list3 = list3 + list4
# print(list3)
#
# list_of_tuples = [(0, 1), (1, 1), (1, 0), (0, 0), (1, 2, 3, 4, 5)]
# print(list_of_tuples)
#
#
# def get_power(num, power):
#     res = 1
#     for n in range(power):
#         res *= num
#     return res
#
#
# print(get_power(5, 2))
#
# x = 10
# print(type(x)) # class int

############################################################################

############################################################################

from stack import Stack

# n = int(input('enter stack size: '))
# s = Stack(n)
# while True:
#     el = int(input('1 for push\n2 for pop\n3 to check if empty\n4 to print\n5 to peek\n6 to exist'))
#     if el == 1:
#         item = input('push an item to stack: ')
#         s.push(item)
#     if el == 2:
#         print(s.pop())
#     if el == 3:
#         print(s.isEmpty())
#     if el == 4:
#         s.printStack()
#     if el == 5:
#         print(s.peek())
#     if el == 6:
#         break

# ################################################################### #
from linearSearch import linearSearch
from sort import BubbleSort
from sort import SelectionSort
from sort import InsertionSort

# list = []
# val = int(input('Enter the size of the list:'))
# print('Enter values for the list separated by ENTER :')
# for i in range(val):
    # list.append(input()) # linearSearch
    # list.append(int(input()))  # sort numerical data

# val = input('enter a value you need to get it: ') # linearSearch
# print('value index is:', linearSearch(list, val)) ## linearSearch
# print(BubbleSort(list))
# print(SelectionSort(list))
# print(InsertionSort(list))

# ############################################################ #
from linkedList import LinkedList

# l1 = LinkedList()
# l1.addStart(5)
# l1.addStart(4)
# l1.addStart(7)
# l1.addStart(3)
# l1.addEnd(55)
# l1.addAfter(7, 99)
# l1.addAfter(77, 100)
# l1.printList()
# print(l1.search(7))
# print(l1.search(77))
# l1.removeStart()
# l1.removeEnd()
# l1.remove(99)
# l1.printList()

# l2 = LinkedList()
# while True:
#     el = (input('1 for addStart\n2 for addEnd\n3 to check if addAfter\n4 to removeStart\n5 to removeEnd\n6 to removeItem\n7 to searchVal\n 8 to check isEmpty\n 9 to printList\n and other key to exist\n'))
#     if el == '1':
#         val = input('Enter value to the linked list:\n')
#         l2.addStart(val)
#     elif el == '2':
#         val = input('Enter value to the linked list:\n')
#         l2.addEnd(val)
#     elif el == '3':
#         val = input('Enter value to the linked list:\n')
#         prev = input('Enter the previous val\n')
#         l2.addAfter(prev, val)
#     elif el == '4':
#         l2.removeStart()
#     elif el == '5':
#         l2.removeEnd()
#     elif el == '6':
#         val = input('enter val:\n')
#         l2.remove(val)
#     elif el == '7':
#         val = input('search val:\n')
#         l2.search(val)
#     elif el == '8':
#         print(l2.isEmpty())
#     elif el == '9':
#         l2.printList()
#     else:
#         break

# ############################################################################ #
from queue import Queue

# n = int(input('enter the max size of the queue:\n'))
# q = Queue(n)
# while True:
#     el = int(input('\nclick\n1 to enqueu\n2 to dequeue\n3 to check is empty\n4 to check is full\n5 to print\n another button to exist'))
#     if el == 1:
#         val = input('enter value to queue:\n')
#         q.enqueue(val)
#     elif el == 2:
#         q.dequeue()
#     elif el == 3:
#         print(q.isEmpty())
#     elif el == 4:
#         print(q.isFull())
#     elif el == 5:
#         q.printQueue()
#     else:
#         break

# ##################################################################### #
from queue import CircularQueue

n = int(input('enter the max size of the queue:\n'))
cq = CircularQueue(n)
while True:
    el = int(input('\nclick\n1 to enqueu\n2 to dequeue\n3 to check is empty\n4 to check is full\n5 to print\n another button to exist'))
    if el == 1:
        val = input('enter value to queue:\n')
        cq.enqueue(val)
    elif el == 2:
        cq.dequeue()
    elif el == 3:
        print(cq.isEmpty())
    elif el == 4:
        print(cq.isFull())
    elif el == 5:
        cq.printQueue()
    else:
        break

