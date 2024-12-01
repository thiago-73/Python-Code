# 1. Multiples of 3 or 5
# Find the sum of all the multiples of 3 or 5 below 1000.
# Result: 233168

# Initialize the sum
sum_multiples = 0

# Iterate through numbers below 1000
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_multiples += i

print(sum_multiples)
