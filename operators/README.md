# Understanding Equality in Python: `is` vs `==`

This Python script demonstrates the differences between the `is` operator and the `==` operator in Python. The `is` operator checks for object identity (whether two references point to the same object in memory), while the `==` operator checks for value equality (whether the values of two objects are the same).

## Features

1. **Equality Checks**:
   The script prints the results of various equality checks using `==` and `is` for different types of values, including booleans, numbers, strings, lists, and tuples.

2. **Examples of Comparisons**:
   ```python
   print(True == 1)           # True: Both are equivalent
   print(True == '1')         # False: Different types
   print(True == ' ')         # False: String with space is not equal to True
   print(True == True)        # True: Same boolean value
3. **Identity Comparisons:**:
   ```python
    print('True is True ', True is True)    # True: Both point to the same object
    print('True == True ', True == True)    # True: Both have the same value
    print('True is False ', True is False)   # False: Different boolean values
    print('False is False ', False is False) # True: Same boolean value

4. **Different Data Types**:
 * Comparison between different data types and structures:
   ```python
    print(1 == 1.0)            # True: Equivalent values (integer and float)
    print(' ' == '\0')        # False: Different string representations
    print([] == ())            # False: List and tuple are different types
    print('1' == 1)            # False: String and integer are different types
    print((1, 2, 3) == [1, 2, 3])  # False: Tuple and list are different types
    print((1, 2, 3) == (1, 2, 3))  # True: Same tuple values
    print([1, 2, 3] == [1, 2, 3])  # True: Same list values
    print([1, 2, 3] == (1, 2, 3))  # False: List and tuple are different types

5. **Object Identity**:
  * Demonstrates that two lists can have the same contents but different identities:
    ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = (1, 2, 3)
    print('a is b ', a is b)        # False: Different objects in memory
    print('a == b ', a == b)        # True: Same contents
    print('a is a ', a is a)        # True: Same object
    print('a == c ', a == c)        # False: Different types (list and tuple)

# Running the Script
To execute the script, ensure you have Python installed on your machine. Clone the repository and run the script using:
  ```python
    python is_vs_equals.py
