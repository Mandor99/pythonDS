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

list = []
val = int(input('Enter the size of the list:'))
print('Enter values for the list separated by ENTER :')
for i in range(val):
    # list.append(input()) # linearSearch
    list.append(int(input()))  # sort numerical data

# val = input('enter a value you need to get it: ') # linearSearch
# print('value index is:', linearSearch(list, val)) ## linearSearch
# print(BubbleSort(list))
# print(SelectionSort(list))
print(InsertionSort(list))

# ############################################################ #
