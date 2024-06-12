
my_list = [1, 2, 3, 4, 5]

my_list.sort(reverse=True)

print(my_list)


def my_decorator(func):
    def wrapper():
        print('list sorted')
        func()
    return wrapper
