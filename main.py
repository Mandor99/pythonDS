print('this \n to \tmake new line\'s')
name = input("inter your name: ")
age = input("inter your age: ")
print('hello ' + name + ' your age is ' + age)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]
list1.extend(list2)
print(list1)
list2 += list3
print(list2)
list3 = list3 + list4
print(list3)

list_of_tuples = [(0, 1), (1, 1), (1, 0), (0, 0), (1, 2, 3, 4, 5)]
print(list_of_tuples)


def get_power(num, power):
    res = 1
    for n in range(power):
        res *= num
    return res


print(get_power(5, 2))

x = 10
print(type(x)) # class int
