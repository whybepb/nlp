"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🐍 PYTHON BASICS CRASH COURSE 🐍                           ║
║                    Interactive Tutorial for Beginners                         ║
║                                                                               ║
║  This file will teach you Python from scratch!                                ║
║  Each section has:                                                            ║
║    📚 Concept explanation                                                     ║
║    💡 Examples you can run                                                    ║
║    ✏️  Practice exercises (like your exam!)                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

HOW TO USE:
1. Read each section carefully
2. Run this file to see outputs: python python_basics_tutorial.py
3. Complete the practice exercises at the bottom
4. Your exercises will be auto-tested!
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: VARIABLES AND DATA TYPES
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 1: VARIABLES AND DATA TYPES")
print("="*70)

"""
In Python, you don't need to declare variable types (unlike Java/C++).
Python figures it out automatically!

COMPARISON WITH OTHER LANGUAGES:
┌─────────────────┬────────────────────────────────────┐
│ Other Languages │ Python                             │
├─────────────────┼────────────────────────────────────┤
│ int x = 5;      │ x = 5                              │
│ String s = "hi" │ s = "hi"                           │
│ float f = 3.14  │ f = 3.14                           │
└─────────────────┴────────────────────────────────────┘
"""

# Integer
age = 25
print(f"age = {age}, type: {type(age)}")  # <class 'int'>

# Float (decimal)
height = 5.9
print(f"height = {height}, type: {type(height)}")  # <class 'float'>

# String (text)
name = "Prathmesh"
print(f"name = {name}, type: {type(name)}")  # <class 'str'>

# Boolean (True/False)
is_student = True
print(f"is_student = {is_student}, type: {type(is_student)}")  # <class 'bool'>

# None (like null in other languages)
nothing = None
print(f"nothing = {nothing}, type: {type(nothing)}")  # <class 'NoneType'>


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: LISTS (Like Arrays in other languages)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 2: LISTS (Arrays)")
print("="*70)

"""
Lists are like arrays but MORE POWERFUL!
- Can hold different types
- Can grow/shrink dynamically
- 0-indexed (like most languages)
"""

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Can mix types!
empty = []

print(f"numbers = {numbers}")
print(f"mixed types = {mixed}")

# Accessing elements (0-indexed)
print(f"\nnumbers[0] = {numbers[0]}")  # First element: 1
print(f"numbers[-1] = {numbers[-1]}")  # Last element: 5 (negative indexing!)
print(f"numbers[-2] = {numbers[-2]}")  # Second last: 4

# Slicing (very powerful!)
print(f"\nnumbers[1:4] = {numbers[1:4]}")  # Elements 1,2,3 (end not included)
print(f"numbers[:3] = {numbers[:3]}")      # First 3 elements
print(f"numbers[2:] = {numbers[2:]}")      # From index 2 to end
print(f"numbers[::2] = {numbers[::2]}")    # Every 2nd element

# Common list operations
numbers.append(6)           # Add to end
print(f"After append(6): {numbers}")

numbers.insert(0, 0)        # Insert at index 0
print(f"After insert(0, 0): {numbers}")

popped = numbers.pop()      # Remove and return last
print(f"After pop(): {numbers}, popped value: {popped}")

# Length of list
print(f"len(numbers) = {len(numbers)}")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: LOOPS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 3: LOOPS")
print("="*70)

"""
Python uses INDENTATION instead of braces {}
This is CRITICAL - wrong indentation = error!

COMPARISON:
┌─────────────────────────────┬─────────────────────────────┐
│ Other Languages (C/Java)    │ Python                      │
├─────────────────────────────┼─────────────────────────────┤
│ for(int i=0; i<5; i++) {    │ for i in range(5):          │
│     print(i);               │     print(i)                │
│ }                           │                             │
└─────────────────────────────┴─────────────────────────────┘
"""

# For loop with range
print("\nFor loop with range(5):")
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"  i = {i}")

# For loop with start, stop
print("\nFor loop with range(2, 6):")
for i in range(2, 6):  # 2, 3, 4, 5
    print(f"  i = {i}")

# For loop with step
print("\nFor loop with range(0, 10, 2):")
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(f"  i = {i}")

# Looping through a list
fruits = ["apple", "banana", "cherry"]
print("\nLooping through fruits list:")
for fruit in fruits:
    print(f"  {fruit}")

# SUPER USEFUL: enumerate() - get index AND value
print("\nUsing enumerate() for index + value:")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# SUPER USEFUL: zip() - loop through multiple lists together
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print("\nUsing zip() for multiple lists:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# While loop
print("\nWhile loop:")
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1  # Python doesn't have ++ operator!


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 4: FUNCTIONS")
print("="*70)

"""
COMPARISON:
┌─────────────────────────────────┬─────────────────────────────────┐
│ Other Languages                 │ Python                          │
├─────────────────────────────────┼─────────────────────────────────┤
│ int add(int a, int b) {         │ def add(a, b):                  │
│     return a + b;               │     return a + b                │
│ }                               │                                 │
└─────────────────────────────────┴─────────────────────────────────┘
"""

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Prathmesh"))

# Function with type hints (optional but recommended!)
def add(a: int, b: int) -> int:
    """This adds two numbers together."""
    return a + b

print(f"add(3, 5) = {add(3, 5)}")

# Function with default parameters
def power(base, exponent=2):  # Default exponent is 2
    return base ** exponent

print(f"power(3) = {power(3)}")       # 3^2 = 9
print(f"power(3, 3) = {power(3, 3)}") # 3^3 = 27

# Multiple return values (super cool!)
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {minimum}, Max: {maximum}")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5: CONDITIONALS (if/else)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 5: CONDITIONALS")
print("="*70)

"""
COMPARISON:
┌─────────────────────────────────┬─────────────────────────────────┐
│ Other Languages                 │ Python                          │
├─────────────────────────────────┼─────────────────────────────────┤
│ if (x > 0) {                    │ if x > 0:                       │
│     // code                     │     # code                      │
│ } else if (x < 0) {             │ elif x < 0:                     │
│     // code                     │     # code                      │
│ } else {                        │ else:                           │
│     // code                     │     # code                      │
│ }                               │                                 │
└─────────────────────────────────┴─────────────────────────────────┘

NOTE: Python uses 'elif' not 'else if'!
NOTE: Python uses 'and', 'or', 'not' instead of &&, ||, !
"""

x = 5

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# Logical operators
a, b = True, False
print(f"\nTrue and False = {a and b}")
print(f"True or False = {a or b}")
print(f"not True = {not a}")

# Comparison in one line (Python allows chaining!)
age = 25
if 18 <= age <= 65:  # Same as: age >= 18 and age <= 65
    print("Working age")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6: LIST COMPREHENSIONS (Python's Superpower!)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 6: LIST COMPREHENSIONS")
print("="*70)

"""
List comprehensions let you create lists in ONE LINE!
This is used A LOT in your exam questions.

PATTERN: [expression for item in iterable if condition]
"""

# Normal way to create a list of squares
squares_normal = []
for i in range(5):
    squares_normal.append(i ** 2)
print(f"Normal way: {squares_normal}")

# List comprehension way (same result, one line!)
squares_comp = [i ** 2 for i in range(5)]
print(f"Comprehension: {squares_comp}")

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehension (for 2D arrays/matrices)
matrix = [[i * j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 7: DICTIONARIES (Like Maps/Objects)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 7: DICTIONARIES")
print("="*70)

"""
Dictionaries store key-value pairs.
Like HashMap in Java or Object in JavaScript.
"""

# Creating a dictionary
student = {
    "name": "Prathmesh",
    "age": 22,
    "grades": [85, 90, 78]
}

print(f"student = {student}")

# Accessing values
print(f"student['name'] = {student['name']}")
print(f"student.get('age') = {student.get('age')}")
print(f"student.get('gpa', 0) = {student.get('gpa', 0)}")  # Default value if key missing

# Adding/updating
student["university"] = "XYZ University"
print(f"After adding university: {student}")

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"\nSquares dict: {squares_dict}")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 8: STRINGS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 8: STRINGS")
print("="*70)

"""
Strings in Python are IMMUTABLE (can't change in place).
But there are many useful methods!
"""

text = "Hello, World!"

# Common string methods
print(f"Original: '{text}'")
print(f"lower(): '{text.lower()}'")
print(f"upper(): '{text.upper()}'")
print(f"replace('World', 'Python'): '{text.replace('World', 'Python')}'")
print(f"split(','): {text.split(',')}")

# String slicing (like lists!)
print(f"\ntext[0:5] = '{text[0:5]}'")
print(f"text[::-1] = '{text[::-1]}'")  # Reverse string!

# f-strings (formatted strings) - THE BEST WAY!
name = "Prathmesh"
age = 22
print(f"\nf-string: My name is {name} and I am {age} years old")
print(f"Math in f-string: 2 + 3 = {2 + 3}")

# Join strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"Join example: '{sentence}'")


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 9: USEFUL BUILT-IN FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 9: USEFUL BUILT-IN FUNCTIONS")
print("="*70)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(f"numbers = {numbers}")
print(f"len(numbers) = {len(numbers)}")         # Length
print(f"sum(numbers) = {sum(numbers)}")         # Sum
print(f"min(numbers) = {min(numbers)}")         # Minimum
print(f"max(numbers) = {max(numbers)}")         # Maximum
print(f"sorted(numbers) = {sorted(numbers)}")   # Sorted (returns new list)
print(f"reversed: {list(reversed(numbers))}")   # Reversed

# abs() - absolute value
print(f"\nabs(-5) = {abs(-5)}")

# round() - rounding
print(f"round(3.14159, 2) = {round(3.14159, 2)}")

# any() and all()
bools = [True, False, True]
print(f"\nany([True, False, True]) = {any(bools)}")  # True if ANY is True
print(f"all([True, False, True]) = {all(bools)}")  # True only if ALL are True


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 10: IMPORTING MODULES
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("📚 SECTION 10: IMPORTING MODULES")
print("="*70)

"""
Python has TONS of built-in modules. Here's how to use them:
"""

# Different ways to import
import math
from math import sqrt, pi
from math import factorial as fact  # Rename

print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"sqrt(16) = {sqrt(16)}")  # Direct use after from import
print(f"pi = {pi}")
print(f"fact(5) = {fact(5)}")  # 5! = 120

# Common math operations
print(f"\nmath.ceil(3.2) = {math.ceil(3.2)}")   # Round up: 4
print(f"math.floor(3.8) = {math.floor(3.8)}") # Round down: 3
print(f"math.pow(2, 3) = {math.pow(2, 3)}")   # 2^3 = 8
print(f"2 ** 3 = {2 ** 3}")                    # Same thing!


# ═══════════════════════════════════════════════════════════════════════════════
#                        ✏️ PRACTICE EXERCISES ✏️
# ═══════════════════════════════════════════════════════════════════════════════
# Complete the functions below. Each is similar to your exam format!
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("✏️ PRACTICE EXERCISES - Complete these!")
print("="*70)


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 1: Sum of List
# ─────────────────────────────────────────────────────────────────────────────
"""
TASK: Return the sum of all numbers in the list.
Do NOT use the built-in sum() function!

INPUT: numbers: list of integers, e.g., [1, 2, 3, 4, 5]
OUTPUT: int: sum of all numbers

SAMPLE:
    Input: [1, 2, 3, 4, 5]
    Output: 15
"""

def sum_of_list(numbers: list) -> int:
    # YOUR CODE HERE
    # Hint: Use a loop to add up all numbers
    total = 0
    for num in numbers:
        total += num
    return total


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 2: Find Maximum
# ─────────────────────────────────────────────────────────────────────────────
"""
TASK: Return the maximum value in a list.
Do NOT use the built-in max() function!

INPUT: numbers: list of integers
OUTPUT: int: maximum value

SAMPLE:
    Input: [3, 1, 4, 1, 5, 9, 2, 6]
    Output: 9
"""

def find_maximum(numbers: list) -> int:
    # YOUR CODE HERE
    # Hint: Track the largest number seen so far
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 3: Count Vowels
# ─────────────────────────────────────────────────────────────────────────────
"""
TASK: Count the number of vowels (a, e, i, o, u) in a string.

INPUT: text: string
OUTPUT: int: count of vowels

SAMPLE:
    Input: "Hello World"
    Output: 3 (e, o, o)
"""

def count_vowels(text: str) -> int:
    # YOUR CODE HERE
    # Hint: Check each character if it's in "aeiouAEIOU"
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 4: Reverse List
# ─────────────────────────────────────────────────────────────────────────────
"""
TASK: Reverse a list without using built-in reverse() or [::-1]

INPUT: items: list
OUTPUT: list: reversed list

SAMPLE:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
"""

def reverse_list(items: list) -> list:
    # YOUR CODE HERE
    # Hint: Build a new list from end to start
    reversed_items = []
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])
    return reversed_items


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 5: List Comprehension Practice
# ─────────────────────────────────────────────────────────────────────────────
"""
TASK: Return a list of squares of even numbers from 0 to n (exclusive).
Use a LIST COMPREHENSION (one line!)

INPUT: n: int
OUTPUT: list of squares of even numbers

SAMPLE:
    Input: 10
    Output: [0, 4, 16, 36, 64]  (0², 2², 4², 6², 8²)
"""

def squares_of_evens(n: int) -> list:
    # YOUR CODE HERE (use list comprehension!)
    return [i ** 2 for i in range(n) if i % 2 == 0]


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 6: Word Frequency (using Dictionary)
# ─────────────────────────────────────────────────────────────────────────────
"""
TASK: Count the frequency of each word in a sentence.
Words should be converted to lowercase.

INPUT: sentence: string
OUTPUT: dict: word -> count

SAMPLE:
    Input: "Hello hello world"
    Output: {"hello": 2, "world": 1}
"""

def word_frequency(sentence: str) -> dict:
    # YOUR CODE HERE
    # Hint: Split sentence into words, use dict to count
    words = sentence.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 7: Dot Product
# ─────────────────────────────────────────────────────────────────────────────
"""
TASK: Calculate the dot product of two vectors.
Dot product = sum of (a[i] * b[i]) for all i

INPUT: vec1: list of numbers, vec2: list of numbers
OUTPUT: float: dot product rounded to 2 decimal places

SAMPLE:
    Input: vec1 = [1, 2, 3], vec2 = [4, 5, 6]
    Output: 32.0  (1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32)
"""

def dot_product(vec1: list, vec2: list) -> float:
    # YOUR CODE HERE
    # This is similar to your exam questions!
    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]
    return round(result, 2)


# ═══════════════════════════════════════════════════════════════════════════════
# TEST ALL EXERCISES
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧪 TESTING YOUR EXERCISES")
    print("="*70)
    
    # Test 1: Sum of List
    result = sum_of_list([1, 2, 3, 4, 5])
    expected = 15
    print(f"\n✏️ Exercise 1 - Sum of List")
    print(f"   Input: [1, 2, 3, 4, 5]")
    print(f"   Expected: {expected}, Got: {result}")
    print(f"   {'✅ PASS' if result == expected else '❌ FAIL'}")
    
    # Test 2: Find Maximum
    result = find_maximum([3, 1, 4, 1, 5, 9, 2, 6])
    expected = 9
    print(f"\n✏️ Exercise 2 - Find Maximum")
    print(f"   Input: [3, 1, 4, 1, 5, 9, 2, 6]")
    print(f"   Expected: {expected}, Got: {result}")
    print(f"   {'✅ PASS' if result == expected else '❌ FAIL'}")
    
    # Test 3: Count Vowels
    result = count_vowels("Hello World")
    expected = 3
    print(f"\n✏️ Exercise 3 - Count Vowels")
    print(f"   Input: 'Hello World'")
    print(f"   Expected: {expected}, Got: {result}")
    print(f"   {'✅ PASS' if result == expected else '❌ FAIL'}")
    
    # Test 4: Reverse List
    result = reverse_list([1, 2, 3, 4, 5])
    expected = [5, 4, 3, 2, 1]
    print(f"\n✏️ Exercise 4 - Reverse List")
    print(f"   Input: [1, 2, 3, 4, 5]")
    print(f"   Expected: {expected}, Got: {result}")
    print(f"   {'✅ PASS' if result == expected else '❌ FAIL'}")
    
    # Test 5: Squares of Evens
    result = squares_of_evens(10)
    expected = [0, 4, 16, 36, 64]
    print(f"\n✏️ Exercise 5 - Squares of Evens")
    print(f"   Input: 10")
    print(f"   Expected: {expected}, Got: {result}")
    print(f"   {'✅ PASS' if result == expected else '❌ FAIL'}")
    
    # Test 6: Word Frequency
    result = word_frequency("Hello hello world")
    expected = {"hello": 2, "world": 1}
    print(f"\n✏️ Exercise 6 - Word Frequency")
    print(f"   Input: 'Hello hello world'")
    print(f"   Expected: {expected}, Got: {result}")
    print(f"   {'✅ PASS' if result == expected else '❌ FAIL'}")
    
    # Test 7: Dot Product
    result = dot_product([1, 2, 3], [4, 5, 6])
    expected = 32.0
    print(f"\n✏️ Exercise 7 - Dot Product")
    print(f"   Input: vec1=[1, 2, 3], vec2=[4, 5, 6]")
    print(f"   Expected: {expected}, Got: {result}")
    print(f"   {'✅ PASS' if result == expected else '❌ FAIL'}")
    
    print("\n" + "="*70)
    print("🎓 TUTORIAL COMPLETE!")
    print("="*70)
    print("""
💡 TIPS FOR YOUR EXAM:
1. Read the docstring carefully - it tells you EXACTLY what to do
2. Look at the sample input/output
3. Think about edge cases (empty list, zero, etc.)
4. Use list comprehension when the task involves creating a new list
5. Remember: range(n) goes from 0 to n-1
6. Use zip() when iterating through multiple lists together
7. Use enumerate() when you need both index and value
8. round(value, 2) rounds to 2 decimal places

🔥 COMMON PATTERNS IN YOUR EXAM:
- Summation: sum(x for x in list)
- Element-wise operations: [a[i] + b[i] for i in range(len(a))]
- With zip: [x + y for x, y in zip(a, b)]
- Filtering: [x for x in list if condition]
- Dictionary building: {key: value for key, value in pairs}
""")
