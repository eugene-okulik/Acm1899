def fib(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
        yield a


def print_n_fib(n):
    last = None
    for last in fib(n):
        pass
    print(last)


nums = [5, 200, 1000, 100000]
for n in nums:
    print_n_fib(n)
