# map, filter, zip, and reduce
from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiplyBy2(item):
    return item*2


def onlyOdd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item

# print('original list: ', my_list)
# print(list(map(multiplyBy2, my_list)))

# print(list(filter(onlyOdd, my_list)))

# print(list(zip(my_list, your_list)))


print(my_list)
print(reduce(accumulator, my_list, 0))
