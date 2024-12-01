# 4. Largest Palindrome Product
# Find the largest palindrome made from the product of two 3-digit numbers.
# Result: 906609

def is_palindrome(n):
    return str(n) == str(n)[::-1]

max_palindrome = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product

print(max_palindrome)
