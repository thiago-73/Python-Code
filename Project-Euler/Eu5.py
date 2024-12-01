# 5. Smallest Multiple
# Find the smallest number that is evenly divisible by all the numbers from 1 to 20.
# Result: 232792560

import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

result = 1
for i in range(1, 21):
    result = lcm(result, i)

print(result)
