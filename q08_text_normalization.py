"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 8: TEXT NORMALIZATION AND CLEANING               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Write a function that takes a string and:                                     ║
║   1. Converts all text to lowercase                                           ║
║   2. Removes all punctuation                                                  ║
║   3. Removes all numerical digits                                             ║
║   4. Returns a list of individual words (tokens)                              ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ Text normalization is essential preprocessing for NLP tasks.                  ║
║ It helps in:                                                                  ║
║   • Reducing vocabulary size ("Hello" and "hello" become same)               ║
║   • Removing noise (punctuation, numbers)                                     ║
║   • Standardizing text format for processing                                  ║
║                                                                               ║
║ WHAT IS PUNCTUATION?                                                          ║
║   Characters like: . , ! ? ; : ' " ( ) [ ] { } - / \ @ # $ % & * etc.        ║
║   Python's string.punctuation contains all of these                           ║
║                                                                               ║
║ EXAMPLE:                                                                      ║
║   Input:  "Hello World! I have 3 cats... Do you?"                            ║
║   Output: ['hello', 'world', 'i', 'have', 'cats', 'do', 'you']               ║
║                                                                               ║
║ STEPS:                                                                        ║
║   "Hello World! 3 cats."                                                      ║
║   → "hello world! 3 cats."  (lowercase)                                       ║
║   → "hello world 3 cats"    (remove punctuation)                             ║
║   → "hello world  cats"     (remove digits)                                   ║
║   → ['hello', 'world', 'cats'] (tokenize)                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import string

def normalize_text(text: str) -> list:
    """
    Normalize and clean text, returning list of tokens.
    
    Steps:
    1. Convert to lowercase
    2. Remove punctuation
    3. Remove digits
    4. Split into tokens
    
    Args:
        text: Input string
    
    Returns:
        List of cleaned tokens (words)
    """
    # Step 1: Convert to lowercase
    text = text.lower()
    
    # Step 2: Remove punctuation
    # string.punctuation contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    for char in string.punctuation:
        text = text.replace(char, ' ')
    
    # Step 3: Remove numerical digits (0-9)
    for digit in '0123456789':
        text = text.replace(digit, ' ')
    
    # Step 4: Split into tokens and remove empty strings
    tokens = text.split()
    
    return tokens


def normalize_text_v2(text: str) -> list:
    """
    Alternative implementation using list comprehension.
    """
    # Step 1: Convert to lowercase
    text = text.lower()
    
    # Step 2 & 3: Keep only alphabetic characters and spaces
    cleaned = ''
    for char in text:
        if char.isalpha():  # Keeps only letters (a-z)
            cleaned += char
        else:
            cleaned += ' '  # Replace everything else with space
    
    # Step 4: Split and filter empty strings
    tokens = [token for token in cleaned.split() if token]
    
    return tokens


def normalize_text_regex(text: str) -> list:
    """
    Alternative implementation using regular expressions.
    """
    import re
    
    # Step 1: Convert to lowercase
    text = text.lower()
    
    # Step 2 & 3: Remove non-alphabetic characters
    # [^a-z\s] means "not a lowercase letter or whitespace"
    text = re.sub(r'[^a-z\s]', ' ', text)
    
    # Step 4: Split and filter
    tokens = text.split()
    
    return tokens


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_normalization():
    """Visual explanation of text normalization."""
    print("=" * 60)
    print("TEXT NORMALIZATION - STEP BY STEP")
    print("=" * 60)
    
    text = "Hello World! I have 3 cats... Do you?"
    print(f"\nOriginal text: '{text}'")
    
    print("\n" + "-" * 40)
    print("STEP 1: Convert to Lowercase")
    print("-" * 40)
    step1 = text.lower()
    print(f"  Result: '{step1}'")
    print("  Why? 'Hello' and 'hello' should be treated as same word")
    
    print("\n" + "-" * 40)
    print("STEP 2: Remove Punctuation")
    print("-" * 40)
    print(f"  Punctuation characters: {string.punctuation}")
    step2 = step1
    for char in string.punctuation:
        if char in step2:
            print(f"  Removing '{char}'...")
        step2 = step2.replace(char, ' ')
    print(f"  Result: '{step2}'")
    
    print("\n" + "-" * 40)
    print("STEP 3: Remove Digits")
    print("-" * 40)
    step3 = step2
    for digit in '0123456789':
        if digit in step3:
            print(f"  Removing '{digit}'...")
        step3 = step3.replace(digit, ' ')
    print(f"  Result: '{step3}'")
    
    print("\n" + "-" * 40)
    print("STEP 4: Tokenize (Split into Words)")
    print("-" * 40)
    step4 = step3.split()
    print(f"  Result: {step4}")
    print(f"  Count: {len(step4)} tokens")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_normalization()
    
    print("\n" + "=" * 60)
    print("TEXT NORMALIZATION - TEST CASES")
    print("=" * 60)
    
    # Test Case 1: Basic example
    text = "Hello World! I have 3 cats... Do you?"
    result = normalize_text(text)
    expected = ['hello', 'world', 'i', 'have', 'cats', 'do', 'you']
    print(f"\nTest 1: '{text}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 2: Mixed case and numbers
    text = "Python3.9 is AWESOME!!!"
    result = normalize_text(text)
    expected = ['python', 'is', 'awesome']
    print(f"\nTest 2: '{text}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 3: Special characters
    text = "Email: test@email.com, Price: $99.99"
    result = normalize_text(text)
    expected = ['email', 'test', 'email', 'com', 'price']
    print(f"\nTest 3: '{text}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 4: Only numbers and punctuation
    text = "12345!@#$%"
    result = normalize_text(text)
    expected = []
    print(f"\nTest 4: '{text}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected} (empty list)")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 5: Multiple spaces and tabs
    text = "Hello   World\t\tTest"
    result = normalize_text(text)
    expected = ['hello', 'world', 'test']
    print(f"\nTest 5: '{text}' (has extra spaces/tabs)")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 6: Verify all methods give same result
    text = "Test-123: Hello, World! (2024)"
    r1 = normalize_text(text)
    r2 = normalize_text_v2(text)
    r3 = normalize_text_regex(text)
    print(f"\nTest 6: Comparing implementations")
    print(f"  Input: '{text}'")
    print(f"  Method 1 (loop):      {r1}")
    print(f"  Method 2 (isalpha):   {r2}")
    print(f"  Method 3 (regex):     {r3}")
    print(f"  All same: {r1 == r2 == r3}")
    
    print("\n" + "=" * 60)
    print("PYTHON STRING METHODS CHEAT SHEET:")
    print("=" * 60)
    print("""
    str.lower()      → Convert to lowercase
    str.upper()      → Convert to uppercase
    str.split()      → Split by whitespace into list
    str.replace(a,b) → Replace 'a' with 'b'
    str.strip()      → Remove leading/trailing whitespace
    
    char.isalpha()   → True if character is a letter (a-z, A-Z)
    char.isdigit()   → True if character is a digit (0-9)
    char.isalnum()   → True if letter or digit
    char.isspace()   → True if whitespace
    
    string.punctuation → All punctuation characters
    """)
