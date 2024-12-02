"""
This program is a unit converter that allows the user to convert between different
units of measurement, including length, weight, and temperature. The user can select
the type of conversion and provide the value to be converted.

Features:
1. Supports conversions for:
    - Length (meters to kilometers, miles, etc.)
    - Weight (kilograms to pounds, grams, etc.)
    - Temperature (Celsius to Fahrenheit, Kelvin, etc.)
2. Handles invalid inputs gracefully.
3. Modular design with separate functions for each conversion type.

Author: Thiago (example)
"""

def convert_length():
    """
    Converts between different units of length.
    Options: meters to kilometers, meters to miles, etc.
    """
    print("Length Conversion Options:")
    print("1 - Meters to Kilometers")
    print("2 - Meters to Miles")
    print("3 - Kilometers to Meters")
    
    choice = int(input("Select conversion type (1-3): "))
    value = float(input("Enter the value to convert: "))
    
    if choice == 1:
        return f"{value} meters = {value / 1000} kilometers"
    elif choice == 2:
        return f"{value} meters = {value / 1609.34} miles"
    elif choice == 3:
        return f"{value} kilometers = {value * 1000} meters"
    else:
        return "Invalid conversion type selected."

def convert_weight():
    """
    Converts between different units of weight.
    Options: kilograms to pounds, grams to kilograms, etc.
    """
    print("Weight Conversion Options:")
    print("1 - Kilograms to Pounds")
    print("2 - Grams to Kilograms")
    
    choice = int(input("Select conversion type (1-2): "))
    value = float(input("Enter the value to convert: "))
    
    if choice == 1:
        return f"{value} kilograms = {value * 2.20462} pounds"
    elif choice == 2:
        return f"{value} grams = {value / 1000} kilograms"
    else:
        return "Invalid conversion type selected."

def convert_temperature():
    """
    Converts between different temperature units.
    Options: Celsius to Fahrenheit, Celsius to Kelvin, etc.
    """
    print("Temperature Conversion Options:")
    print("1 - Celsius to Fahrenheit")
    print("2 - Celsius to Kelvin")
    
    choice = int(input("Select conversion type (1-2): "))
    value = float(input("Enter the value to convert: "))
    
    if choice == 1:
        return f"{value} Celsius = {(value * 9/5) + 32} Fahrenheit"
    elif choice == 2:
        return f"{value} Celsius = {value + 273.15} Kelvin"
    else:
        return "Invalid conversion type selected."

def main():
    """
    Main function of the unit converter program. Allows the user to select the type of
    conversion and calls the corresponding function.
    """
    try:
        print("Welcome to the Unit Converter!")
        print("Choose the type of conversion:")
        print("1 - Length")
        print("2 - Weight")
        print("3 - Temperature")
        
        conversion_type = int(input("Enter the type of conversion (1-3): "))
        
        if conversion_type == 1:
            result = convert_length()  # Call length conversion function.
        elif conversion_type == 2:
            result = convert_weight()  # Call weight conversion function.
        elif conversion_type == 3:
            result = convert_temperature()  # Call temperature conversion function.
        else:
            print("Invalid conversion type selected.")
            return
        
        print(result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# This ensures the script runs only when executed directly, not when imported as a module.
if __name__ == "__main__":
    main()
