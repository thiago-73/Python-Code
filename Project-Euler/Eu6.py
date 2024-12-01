# Problem 6: Sum square difference
# The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 + 3^2 + ... + 10^2 = 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 = 385
# The square of the sum of the first ten natural numbers is:
# (1 + 2 + 3 + ... + 10)^2 = 55^2 = 3025
# Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
# 3025 - 385 = 2640
#
# The task is to find the difference between the sum of the squares of the first n natural numbers and the square of the sum for a given n.

n = int(input("Ingrese número: "))

def Suma_Cuadrado(n):
    s1 = 0
    s2 = 0
    
    # Calculate the sum of the first n natural numbers
    for i in range(1, n+1):
        s1 += i
    # Calculate the sum of the squares of the first n natural numbers
    for i in range(1, n+1):
        s2 += (i ** 2)
        
    # Calculate the difference: sum of squares - square of the sum
    result = s2 - (s1 ** 2)
    
    return result

# Print the result
print(Suma_Cuadrado(n))
