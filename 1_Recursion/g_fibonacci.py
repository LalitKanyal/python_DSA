def fibonacci(n):
    assert n>=0 and int(n) == n, 'Fibonacci number cannot be negative number or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
# print(fibonacci(4))