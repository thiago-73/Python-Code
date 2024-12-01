# Problem Explanation:
# You are tasked with finding the 10001st prime number.
# A prime number is a number greater than 1 that cannot be formed by multiplying two smaller positive integers.
# In other words, a prime number has only two divisors: 1 and itself.
# The goal is to write a program that finds the 10001st prime number.

# List to store prime numbers
primos = []  

# Start checking from number 2, the first prime number
numeros = 2  

# Loop until we find the 10001st prime
while len(primos) < 10001:
    # Check divisibility from 2 to the square root of the current number
    for i in range(2, int(numeros ** 0.5) + 1):
        if numeros % i == 0:  # If divisible, the number is not prime
            break  # Exit the for loop if a divisor is found
    else:
        # If no divisors were found, the number is prime
        primos.append(numeros)  

    # Increment the number to check the next one
    numeros += 1  

# Output the 10001st prime number, which is the last one in the list
print(primos[-1])  # Output: 104743
