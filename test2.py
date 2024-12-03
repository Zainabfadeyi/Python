from collections import deque

def first_non_repeating_char_queue(s: str) -> str:
    """
    Finds the first non-repeating character in a string using a queue.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: The first non-repeating character. If none, returns an empty string.
    """
    # Dictionary to store the count of each character
    char_count = {}
    
    # Queue to maintain the order of non-repeating characters
    queue = deque()
    
    # Traverse the string and populate the count and queue
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            queue.append(char)
        
        # Remove characters from the front of the queue if they are repeated
        while queue and char_count[queue[0]] > 1:
            queue.popleft()
    
    # The first character in the queue is the first non-repeating character
    return queue[0] if queue else ""

# Example usage:
input_string = "swiss"
result = first_non_repeating_char_queue(input_string)
print(f"The first non-repeating character in '{input_string}' is: {result}")
