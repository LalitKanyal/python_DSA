# Find the sum of digits of a positive integer number using recursion

def sumofDigits(n):
    assert n>=0 and int(n)==n, 'Number should be positive integer'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(2222))