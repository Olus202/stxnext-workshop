def fibonacci_generator(n):
    a, b = 0, 1
    i = 0
    while i != n:
        yield a
        a, b = b, a+b
        i += 1

fib_gen = fibonacci_generator(14)

fib_compr_list = [j for j in fibonacci_generator(14) if j % 2 == 0]
print(fib_compr_list)
