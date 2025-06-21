import math

# Ask the user to enter a number
try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root and logarithm are not defined for negative numbers.")
    elif number == 0:
        print("Square root of 0 is 0")
        print("logarithm of 0 is undefined")
        print(f"Sine of 0 is: {math.sin(0)}")
    else:
        sqrt_result = math.sqrt(number)
        log_result = math.log(number)  # logarithm (base e)
        sine_result = math.sin(number)  # Assumes number is in radians

        print(f"\nResults for the number {number}:")
        print(f"Square root: {sqrt_result}")
        print(f"Natural logarithm (ln): {log_result}")
        print(f"Sine (in radians): {sine_result}")

except ValueError:
    print("Invalid input. Please enter a valid numeric value.")
