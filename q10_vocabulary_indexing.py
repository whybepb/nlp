"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 10: VOCABULARY INDEXING (BAG OF WORDS)           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Create a vocabulary where each unique word is assigned a unique integer      ║
║ index (starting from 0). Given a list of sentences, return a vocabulary      ║
║ dictionary sorted alphabetically.                                             ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ Vocabulary indexing is the foundation of the "Bag of Words" model.           ║
║ Each unique word gets a unique integer ID, allowing us to represent          ║
║ text as numbers that machine learning models can process.                     ║
║                                                                               ║
║ EXAMPLE:                                                                      ║
║   Input sentences:                                                            ║
║     - "the cat sat"                                                           ║
║     - "the dog ran"                                                           ║
║                                                                               ║
║   Unique words (sorted): ['cat', 'dog', 'ran', 'sat', 'the']                 ║
║                                                                               ║
║   Vocabulary dictionary:                                                      ║
║     {                                                                         ║
║       'cat': 0,                                                               ║
║       'dog': 1,                                                               ║
║       'ran': 2,                                                               ║
║       'sat': 3,                                                               ║
║       'the': 4                                                                ║
║     }                                                                         ║
║                                                                               ║
║ WHY ALPHABETICALLY?                                                           ║
║   Consistent ordering across different runs of the program.                  ║
║   Makes debugging and verification easier.                                    ║
║                                                                               ║
║ INPUT:  List of sentences (strings)                                           ║
║ OUTPUT: Dictionary mapping each unique word to its integer index             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

def create_vocabulary(sentences: list) -> dict:
    """
    Create a vocabulary dictionary from a list of sentences.
    
    Args:
        sentences: List of sentence strings
    
    Returns:
        Dictionary mapping each unique word to a unique integer index,
        sorted alphabetically by word.
    """
    # Step 1: Collect all unique words
    unique_words = set()  # Using set to avoid duplicates
    
    for sentence in sentences:
        words = sentence.split()  # Tokenize by spaces
        unique_words.update(words)  # Add all words to set
    
    # Step 2: Sort words alphabetically
    sorted_words = sorted(unique_words)
    
    # Step 3: Assign indices starting from 0
    vocabulary = {}
    for index, word in enumerate(sorted_words):
        vocabulary[word] = index
    
    return vocabulary


def create_vocabulary_v2(sentences: list) -> dict:
    """Alternative using dictionary comprehension."""
    # Collect all words and get unique ones
    all_words = set()
    for sentence in sentences:
        all_words.update(sentence.split())
    
    # Sort and create dictionary in one step
    vocabulary = {word: idx for idx, word in enumerate(sorted(all_words))}
    
    return vocabulary


def sentence_to_vector(sentence: str, vocabulary: dict) -> list:
    """
    Convert a sentence to a Bag of Words vector using the vocabulary.
    
    Args:
        sentence: Input sentence
        vocabulary: Vocabulary dictionary
    
    Returns:
        List of word counts (Bag of Words representation)
    """
    # Initialize vector with zeros (one position per word in vocabulary)
    vector = [0] * len(vocabulary)
    
    # Count occurrences of each word
    words = sentence.split()
    for word in words:
        if word in vocabulary:
            idx = vocabulary[word]
            vector[idx] += 1
    
    return vector


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_vocabulary():
    """Visual explanation of vocabulary indexing."""
    print("=" * 60)
    print("VOCABULARY INDEXING - STEP BY STEP")
    print("=" * 60)
    
    sentences = [
        "the cat sat on the mat",
        "the dog ran in the park"
    ]
    
    print("\nInput sentences:")
    for i, s in enumerate(sentences):
        print(f"  {i}: '{s}'")
    
    print("\n" + "-" * 40)
    print("STEP 1: Extract All Words")
    print("-" * 40)
    
    all_words = []
    for i, sentence in enumerate(sentences):
        words = sentence.split()
        all_words.extend(words)
        print(f"  Sentence {i}: {words}")
    
    print(f"\n  All words: {all_words}")
    
    print("\n" + "-" * 40)
    print("STEP 2: Get Unique Words")
    print("-" * 40)
    
    unique_words = set(all_words)
    print(f"  Unique words: {unique_words}")
    print(f"  Count: {len(unique_words)} unique words")
    
    print("\n" + "-" * 40)
    print("STEP 3: Sort Alphabetically")
    print("-" * 40)
    
    sorted_words = sorted(unique_words)
    print(f"  Sorted: {sorted_words}")
    
    print("\n" + "-" * 40)
    print("STEP 4: Assign Indices")
    print("-" * 40)
    
    vocabulary = {}
    for idx, word in enumerate(sorted_words):
        vocabulary[word] = idx
        print(f"  '{word}' → index {idx}")
    
    print(f"\nFinal Vocabulary: {vocabulary}")
    
    print("\n" + "-" * 40)
    print("BONUS: BAG OF WORDS REPRESENTATION")
    print("-" * 40)
    
    print("\nUsing the vocabulary to represent sentences as vectors:")
    print(f"Vocabulary order: {sorted_words}")
    
    for sentence in sentences:
        vector = sentence_to_vector(sentence, vocabulary)
        print(f"\n  '{sentence}'")
        print(f"  → Vector: {vector}")
        print("  Breakdown:")
        words = sentence.split()
        for word in sorted_words:
            count = words.count(word)
            if count > 0:
                print(f"    '{word}' (idx={vocabulary[word]}): appears {count} time(s)")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_vocabulary()
    
    print("\n" + "=" * 60)
    print("VOCABULARY INDEXING - TEST CASES")
    print("=" * 60)
    
    # Test Case 1: Basic example
    sentences = ["the cat sat", "the dog ran"]
    result = create_vocabulary(sentences)
    expected = {'cat': 0, 'dog': 1, 'ran': 2, 'sat': 3, 'the': 4}
    print(f"\nTest 1: {sentences}")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 2: Single sentence
    sentences = ["hello world"]
    result = create_vocabulary(sentences)
    expected = {'hello': 0, 'world': 1}
    print(f"\nTest 2: {sentences}")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 3: Repeated words
    sentences = ["a a a b b c"]
    result = create_vocabulary(sentences)
    expected = {'a': 0, 'b': 1, 'c': 2}
    print(f"\nTest 3: {sentences}")
    print(f"  Result: {result}")
    print(f"  (Repeated words only appear once in vocabulary)")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 4: Mixed case (if not normalized)
    sentences = ["Hello hello HELLO"]
    result = create_vocabulary(sentences)
    print(f"\nTest 4: {sentences}")
    print(f"  Result: {result}")
    print(f"  (Note: 'Hello', 'hello', 'HELLO' are different words here!)")
    print(f"  (You might want to lowercase first in real applications)")
    
    # Test Case 5: Empty sentences
    sentences = []
    result = create_vocabulary(sentences)
    expected = {}
    print(f"\nTest 5: {sentences} (empty)")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  ✓ PASS" if result == expected else "  ✗ FAIL")
    
    # Test Case 6: Verify alphabetical order
    sentences = ["zebra apple mango banana"]
    result = create_vocabulary(sentences)
    print(f"\nTest 6: {sentences}")
    print(f"  Result: {result}")
    print(f"  Order check: apple=0, banana=1, mango=2, zebra=3")
    is_ordered = (result['apple'] < result['banana'] < result['mango'] < result['zebra'])
    print(f"  ✓ Alphabetically ordered" if is_ordered else "  ✗ Not ordered correctly")
    
    print("\n" + "=" * 60)
    print("BAG OF WORDS (BoW) - COMPLETE EXAMPLE")
    print("=" * 60)
    
    sentences = ["I love NLP", "NLP is fun", "I learn NLP"]
    vocab = create_vocabulary(sentences)
    print(f"\nSentences: {sentences}")
    print(f"Vocabulary: {vocab}")
    print(f"\nBoW Vectors (each position = word count):")
    print(f"{'Word':>8}: {list(vocab.keys())}")
    
    for s in sentences:
        vec = sentence_to_vector(s, vocab)
        print(f"'{s:12}': {vec}")
    
    print("\n" + "=" * 60)
