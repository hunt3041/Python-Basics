my_list = [5, 4, 3]


# square list using lamda expression
print(list(map(lambda item: item**2, my_list)))

# List sorting using lambda
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])

print(a)
