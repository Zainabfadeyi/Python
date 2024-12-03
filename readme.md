# First Non-Repeating Character Finder

This project demonstrates two approaches to solving the problem of finding the first non-repeating character in a string using Python. We will explore the following two approaches:

1. **Dictionary Approach (Two Passes)**
2. **Queue + Dictionary Approach (Single Pass)**

Both approaches are analyzed in terms of their efficiency, including time and space complexity.

---

## Problem Statement

Given a string, the task is to find the first character that does not repeat in the string. If all characters are repeated, the function should return an empty string.

### Example:
- Input: `"swiss"`
- Output: `'w'`

---

## Approach 1: Dictionary Approach (Two Passes)

### Description

In this approach, we use a **dictionary** (or hashmap) to store the count of each character. This is followed by a second iteration over the string to find the first character that occurs only once.

### Steps:

1. **First Pass**: Iterate through the string and populate a dictionary where the keys are characters and the values are their counts.
2. **Second Pass**: Iterate through the string again to find the first character with a count of 1.

### Time Complexity

- The first loop through the string takes **O(n)** time, where `n` is the length of the string.
- The second loop also takes **O(n)** time.
- Therefore, the total time complexity is **O(n)**.

### Space Complexity

- The space complexity is **O(k)**, where `k` is the number of unique characters in the string (since the dictionary holds a key for each unique character).
- In the worst case, **k = n** (when all characters are unique), so the space complexity can be as high as **O(n)**.

### Pros and Cons

- **Pros**: 
  - Simple to implement.
  - Efficient for most practical use cases.
- **Cons**: 
  - Requires two passes through the string, which could be a disadvantage if we aim for a single-pass solution.

---

## Approach 2: Queue + Dictionary Approach (Single Pass)

### Description

This approach uses a combination of a **queue** and a **dictionary** to maintain character order and count in a single pass. The queue helps to track the order of non-repeating characters, while the dictionary maintains the count of each character.

### Steps:

1. **Single Pass**: As we iterate through the string, we update the count of each character in the dictionary and add non-repeating characters to the queue.
2. **Queue Management**: As we go, we remove characters from the front of the queue if they become repeated. This ensures that the first element of the queue is always the first non-repeating character.

### Time Complexity

- We traverse the string once, which takes **O(n)** time.
- Each character is added and removed from the queue at most once, so queue operations are **O(1)** on average.
- Therefore, the overall time complexity is **O(n)**.

### Space Complexity

- The dictionary takes **O(k)** space, where `k` is the number of unique characters.
- The queue, in the worst case, can store all non-repeating characters, leading to **O(n)** space usage.
- Therefore, the total space complexity is **O(n)**.

### Pros and Cons

- **Pros**: 
  - This approach is more efficient when only a single pass is desired.
  - It dynamically tracks the first non-repeating character at every step.
- **Cons**: 
  - Slightly more complex due to the management of both the queue and dictionary.
  - Higher space usage due to the queue in certain cases.

---

## Time and Space Complexity Comparison

| Approach                     | Time Complexity | Space Complexity | Pros                                                    | Cons                                                    |
|-------------------------------|-----------------|------------------|---------------------------------------------------------|---------------------------------------------------------|
| **Dictionary Approach** (Two Pass)| **O(n)**        | **O(k)**          | Simple, intuitive, works well in most scenarios.         | Requires two passes through the string.                 |
| **Queue + Dictionary Approach** (Single Pass)| **O(n)**| **O(n)** | Single-pass solution, tracks first non-repeating in real time.| More complex, higher space usage due to the queue.      |

---
## Possible Improvements

### Dictionary Approach (Two Passes)

- **Early Exit for Edge Cases**: One improvement is handling edge cases, such as empty strings or strings with all repeating characters. This ensures that the function doesn't unnecessarily perform the second pass if the input is empty or contains only repeating characters.
- **Memory Optimization**: While the dictionary approach is efficient, an alternative improvement could involve using a `Counter` from Python’s `collections` module, which simplifies the counting process. This would, however, still maintain **O(n)** space complexity.

### Queue + Dictionary Approach (Single Pass)

- **Space Optimization**: The queue-based approach can be optimized by checking whether a character is already repeated before adding it to the queue. This reduces the queue size, especially for large input strings with many repeating characters.
- **Real-Time Processing**: For cases where the function needs to process streaming data, a sliding window mechanism could be implemented in the future to improve real-time non-repeating character detection without holding the entire string in memory.

Both approaches could further benefit from specific space-saving techniques in memory-constrained environments or by using compressed data structures when processing very large datasets. However, these improvements are usually scenario-specific and may trade off simplicity for complexity.

---


## Conclusion

Both approaches solve the problem in **O(n)** time complexity. The **dictionary-only approach** is more straightforward and suitable for general use. However, if you require a **single-pass solution** that tracks the first non-repeating character dynamically, the **queue-based approach** is a better option, albeit at the cost of slightly higher space complexity.


