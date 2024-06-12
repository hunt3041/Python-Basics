def fib(number):
    f_prev0 = 0
    f_prev1 = 1
    print(f_prev0)
    print(f_prev1)
    for i in range(number-1):
        fib_next = f_prev0 + f_prev1
        yield fib_next
        f_prev0 = f_prev1
        f_prev1 = fib_next


for i in fib(20):
    print(i)


_myvar = 10
my-var = 10
