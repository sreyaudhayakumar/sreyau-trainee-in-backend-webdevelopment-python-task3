# 6.	Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
 
fibonacci = lambda n: [0] if n == 0 else [0, 1] if n == 1 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-2)[-1]]

def print_fibonacci_series(n):
    fib_series = fibonacci(n)[:n]  
    print("Fibonacci series upto {}:".format(n))
    print(fib_series)
cases = [2, 5, 6]

for n in cases:
    print_fibonacci_series(n)
 