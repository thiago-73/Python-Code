# 2. Even Fibonacci Numbers
# Find the sum of the even Fibonacci numbers whose values do not exceed four million.
# Result: 4613732

a, b = 1, 2
sum_even_fib = 0

while b <= 4000000:
    if b % 2 == 0:
        sum_even_fib += b
    a, b = b, a + b

print(sum_even_fib)
