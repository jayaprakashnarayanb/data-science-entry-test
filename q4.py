def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return "Error: Input must be a string"
    
    # Initialize an empty string for the reversed result
    reversed_str = ''
    
    # Loop through the string in reverse order and construct the reversed string
    for char in s:
        reversed_str = char + reversed_str
    
    return reversed_str


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"
print(string_reverse("Hello World")) 
print(string_reverse("Python"))
