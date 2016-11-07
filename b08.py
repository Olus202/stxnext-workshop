def fibonacci_generator(n):
    a, b = 0, 1
    i = 0
    while i != n:
        yield a
        a, b = b, a+b
        i += 1

fib_gen = fibonacci_generator(14)

for j in fib_gen:
    print(j)
