def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return "Error: Both num and divisor must be numeric"
    
    # Check if divisor is not zero to avoid division by zero error
    if divisor == 0:
        return "Error: Divisor cannot be zero"
    
    # Return True if num is divisible by divisor, otherwise False
    return num % divisor == 0



# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
