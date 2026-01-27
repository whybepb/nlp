"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 9: GENERATING CHARACTER N-GRAMS                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Create a function that generates Character Bigrams (N=2) for a given word.   ║
║ A bigram is a sequence of two adjacent characters.                           ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ N-grams are contiguous sequences of N items from a given sample.             ║
║   • Unigram (N=1): Single characters                                         ║
║   • Bigram (N=2):  Pairs of adjacent characters                              ║
║   • Trigram (N=3): Triplets of adjacent characters                           ║
║                                                                               ║
║ N-grams are used in:                                                          ║
║   • Spell checking (similar n-grams = similar words)                         ║
║   • Text prediction (predict next character)                                 ║
║   • Language identification                                                   ║
║                                                                               ║
║ EXAMPLE (Bigrams):                                                            ║
║   Word: "PYTHON"                                                              ║
║   Position: P Y T H O N                                                       ║
║             ├─┘ │ │ │ │    → "PY"                                            ║
║               ├─┘ │ │ │    → "YT"                                            ║
║                 ├─┘ │ │    → "TH"                                            ║
║                   ├─┘ │    → "HO"                                            ║
║                     ├─┘    → "ON"                                            ║
║                                                                               ║
║   Output: ['PY', 'YT', 'TH', 'HO', 'ON']                                     ║
║                                                                               ║
║ FORMULA:                                                                      ║
║   Number of n-grams for word of length L = L - N + 1                         ║
║   For bigrams (N=2): "PYTHON" (L=6) → 6 - 2 + 1 = 5 bigrams                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

def generate_bigrams(word: str) -> list:
    """
    Generate character bigrams (N=2) for a word.
    
    Args:
        word: Input string
    
    Returns:
        List of bigram strings
    """
    bigrams = []
    
    # Loop through the word, taking pairs of adjacent characters
    for i in range(len(word) - 1):
        bigram = word[i] + word[i + 1]  # Current char + next char
        bigrams.append(bigram)
    
    return bigrams


def generate_bigrams_v2(word: str) -> list:
    """Alternative using list comprehension."""
    return [word[i:i+2] for i in range(len(word) - 1)]


def generate_ngrams(word: str, n: int) -> list:
    """
    Generate character n-grams of any size.
    
    Args:
        word: Input string
        n: Size of each n-gram
    
    Returns:
        List of n-gram strings
    """
    if n > len(word):
        return []
    
    ngrams = []
    for i in range(len(word) - n + 1):
        ngram = word[i:i+n]  # Slice from i to i+n
        ngrams.append(ngram)
    
    return ngrams


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_ngrams():
    """Visual explanation of n-gram generation."""
    print("=" * 60)
    print("CHARACTER N-GRAMS - STEP BY STEP")
    print("=" * 60)
    
    word = "PYTHON"
    print(f"\nWord: '{word}' (length = {len(word)})")
    
    print("\n" + "-" * 40)
    print("BIGRAMS (N=2): Pairs of adjacent characters")
    print("-" * 40)
    print(f"\nNumber of bigrams = length - 2 + 1 = {len(word)} - 2 + 1 = {len(word) - 1}")
    print("\nVisualization:")
    print(f"  Positions: {'  '.join(str(i) for i in range(len(word)))}")
    print(f"  Characters: {'  '.join(word)}")
    print()
    
    for i in range(len(word) - 1):
        # Visual representation
        indicator = ' ' * (i * 3) + '└─┘'
        print(f"  {indicator} → '{word[i]}{word[i+1]}' (positions {i} and {i+1})")
    
    bigrams = generate_bigrams(word)
    print(f"\nBigrams: {bigrams}")
    
    print("\n" + "-" * 40)
    print("OTHER N-GRAM TYPES:")
    print("-" * 40)
    
    # Unigrams
    unigrams = generate_ngrams(word, 1)
    print(f"\nUnigrams (N=1): {unigrams}")
    
    # Trigrams
    trigrams = generate_ngrams(word, 3)
    print(f"Trigrams (N=3): {trigrams}")
    
    # 4-grams
    fourgrams = generate_ngrams(word, 4)
    print(f"4-grams (N=4):  {fourgrams}")
    
    print("\nFORMULA VERIFICATION:")
    print("─" * 40)
    for n in [1, 2, 3, 4]:
        expected = len(word) - n + 1
        actual = len(generate_ngrams(word, n))
        print(f"  N={n}: Expected = {len(word)} - {n} + 1 = {expected}, Actual = {actual}")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_ngrams()
    
    print("\n" + "=" * 60)
    print("CHARACTER BIGRAMS - TEST CASES")
    print("=" * 60)
    
    # Test Case 1: Given example
    word = "PYTHON"
    result = generate_bigrams(word)
    expected = ['PY', 'YT', 'TH', 'HO', 'ON']
    print(f"\nTest 1: '{word}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 2: Short word
    word = "AB"
    result = generate_bigrams(word)
    expected = ['AB']
    print(f"\nTest 2: '{word}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 3: Single character
    word = "A"
    result = generate_bigrams(word)
    expected = []
    print(f"\nTest 3: '{word}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected} (no bigrams possible)")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 4: Lowercase
    word = "hello"
    result = generate_bigrams(word)
    expected = ['he', 'el', 'll', 'lo']
    print(f"\nTest 4: '{word}'")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 5: With spaces (if word has spaces)
    word = "A B"
    result = generate_bigrams(word)
    expected = ['A ', ' B']
    print(f"\nTest 5: '{word}' (includes space)")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 6: N-grams of different sizes
    print("\n" + "-" * 40)
    print("BONUS: Different N-gram Sizes")
    print("-" * 40)
    
    word = "ABCDE"
    for n in range(1, 6):
        ngrams = generate_ngrams(word, n)
        print(f"\n  '{word}' with N={n}: {ngrams}")
    
    print("\n" + "=" * 60)
    print("PRACTICAL APPLICATIONS:")
    print("=" * 60)
    print("""
    1. SPELL CHECKING:
       - "teh" bigrams: ['te', 'eh']
       - "the" bigrams: ['th', 'he']
       - Compare overlap to find similar words!
    
    2. WORD SIMILARITY:
       - More shared bigrams = more similar words
       - "python" and "pythons" share many bigrams
    
    3. TEXT PREDICTION:
       - Given "th", what comes next?
       - Train on bigram frequencies from text corpus
    """)
