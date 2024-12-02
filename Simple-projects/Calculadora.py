"""
This program is a simple calculator that allows the user to perform basic arithmetic 
operations (addition, subtraction, multiplication, division) and advanced operations 
(square power and square root). The user can choose to work with one or two values.

Features:
1. Handles invalid inputs and exceptions (e.g., division by zero, negative square roots).
2. Organized into functions for better readability and modularity.
3. Includes clear error messages for unsupported operations or invalid inputs.
"""

def calculate_one_value():
    """
    Prompts the user to input a single number and choose between squaring it
    or finding its square root. Returns the result or None in case of an error.
    """
    val = float(input("Enter a number: "))
    opera = int(input("Select operation (1-Square the number, 2-Square root): "))
    
    if opera == 1:
        return val ** 2
    elif opera == 2:
        if val < 0:
            print("Error: Cannot calculate the square root of a negative number.")
            return None
        return val ** 0.5
    else:
        print("Invalid operation.")
        return None

def calculate_two_values():
    """
    Prompts the user to input two numbers and choose an arithmetic operation 
    (addition, subtraction, multiplication, or division). Returns the result 
    or None in case of an error.
    """
    val1 = float(input("Enter the first value: "))
    operation = input("Select operation (+ for addition, - for subtraction, / for division, * for multiplication): ").strip()
    val2 = float(input("Enter the second value: "))
    
    if operation == "+":
        return val1 + val2
    elif operation == "-":
        return val1 - val2
    elif operation == "/":
        if val2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return val1 / val2
    elif operation == "*":
        return val1 * val2
    else:
        print("Invalid operation.")
        return None

def main():
    """
    Main function of the calculator program. It asks the user how many values they 
    want to operate on (1 or 2) and calls the appropriate function to perform the calculation.
    """
    try:
        # Ask the user whether they want to operate with 1 or 2 values.
        op = int(input("Enter the number of values to operate with (1 or 2): "))
        
        if op == 1:
            result = calculate_one_value()  # Call the single-value operation function.
        elif op == 2:
            result = calculate_two_values()  # Call the two-value operation function.
        else:
            print("Invalid number of values.")
            return
        
        if result is not None:
            print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# This ensures the script runs only when executed directly, not when imported as a module.
if __name__ == "__main__":
    main()
