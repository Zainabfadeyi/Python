def first_non_repeating_char(s: str) -> str:
    """
    Finds the first non-repeating character in a string.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: The first non-repeating character. If none, returns an empty string.
    """
    # Dictionary to store the count of each character
    char_count = {}

    # Step 1: Populate the dictionary with character counts
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Step 2: Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If no non-repeating character is found
    return ""

# Example usage:
input_string = "swiss"
result = first_non_repeating_char(input_string)
print(f"The first non-repeating character in '{input_string}' is: {result}")
