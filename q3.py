def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        # If key exists, print the original value and update it
        print(f"Original value for '{key}': {dct[key]}")
    
    # Update the dictionary with the new key-value pair
    dct[key] = value
    
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
thisdct={}
print(update_dictionary(thisdct, "name", "Alice"))
print(update_dictionary(thisdct, "age", 25))
print(update_dictionary(thisdct, "age", 26))
