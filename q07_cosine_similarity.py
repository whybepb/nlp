"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 7: COSINE SIMILARITY                             ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Given a Pandas DataFrame containing a list of words with their corresponding ║
║ 5-dimensional word embeddings, implement a function that computes the        ║
║ cosine similarity between any two given words.                               ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ Cosine similarity measures the angle between two vectors.                    ║
║ It ranges from -1 (opposite) to 1 (identical direction).                     ║
║                                                                               ║
║ FORMULA:                                                                      ║
║                                                                               ║
║                  A · B           Σ(A_i × B_i)                                ║
║   cos(θ) = ───────────── = ─────────────────────────                         ║
║             ||A|| × ||B||   √Σ(A_i²) × √Σ(B_i²)                              ║
║                                                                               ║
║ Where:                                                                        ║
║   A · B = dot product of vectors A and B                                     ║
║   ||A|| = magnitude (length) of vector A = √(a₁² + a₂² + ... + aₙ²)         ║
║                                                                               ║
║ EXAMPLE:                                                                      ║
║   A = [1, 0, 1]                                                               ║
║   B = [0, 1, 1]                                                               ║
║   A · B = (1×0) + (0×1) + (1×1) = 0 + 0 + 1 = 1                              ║
║   ||A|| = √(1² + 0² + 1²) = √2                                               ║
║   ||B|| = √(0² + 1² + 1²) = √2                                               ║
║   cos(θ) = 1 / (√2 × √2) = 1/2 = 0.5                                         ║
║                                                                               ║
║ INPUT:                                                                        ║
║   DataFrame with columns: 'word', 'dim_0', 'dim_1', 'dim_2', 'dim_3', 'dim_4'║
║   Two word strings to compare                                                 ║
║                                                                               ║
║ OUTPUT:                                                                       ║
║   float: Cosine similarity between the two words                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import pandas as pd
import numpy as np
import math

def cosine_similarity(vec1: list, vec2: list) -> float:
    """
    Compute cosine similarity between two vectors.
    
    Args:
        vec1: First vector (list of floats)
        vec2: Second vector (list of floats)
    
    Returns:
        Cosine similarity (float between -1 and 1)
    """
    # Step 1: Compute dot product (A · B)
    dot_product = 0
    for a, b in zip(vec1, vec2):
        dot_product += a * b
    
    # Step 2: Compute magnitude of vec1 (||A||)
    magnitude1 = 0
    for a in vec1:
        magnitude1 += a ** 2
    magnitude1 = math.sqrt(magnitude1)
    
    # Step 3: Compute magnitude of vec2 (||B||)
    magnitude2 = 0
    for b in vec2:
        magnitude2 += b ** 2
    magnitude2 = math.sqrt(magnitude2)
    
    # Step 4: Compute cosine similarity
    # Handle edge case where magnitude is 0
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)


def cosine_similarity_numpy(vec1: list, vec2: list) -> float:
    """Compute cosine similarity using NumPy."""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    dot_product = np.dot(vec1, vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)


def get_word_similarity(df: pd.DataFrame, word1: str, word2: str) -> float:
    """
    Compute cosine similarity between two words from a DataFrame.
    
    Args:
        df: DataFrame with 'word' and embedding columns ('dim_0', 'dim_1', etc.)
        word1: First word
        word2: Second word
    
    Returns:
        Cosine similarity between the two word embeddings
    """
    # Get embedding for word1
    vec1_row = df[df['word'] == word1]
    if len(vec1_row) == 0:
        raise ValueError(f"Word '{word1}' not found in DataFrame")
    
    # Get embedding columns (all except 'word')
    embedding_cols = [col for col in df.columns if col != 'word']
    vec1 = vec1_row[embedding_cols].values[0].tolist()
    
    # Get embedding for word2
    vec2_row = df[df['word'] == word2]
    if len(vec2_row) == 0:
        raise ValueError(f"Word '{word2}' not found in DataFrame")
    
    vec2 = vec2_row[embedding_cols].values[0].tolist()
    
    # Compute and return cosine similarity
    return cosine_similarity(vec1, vec2)


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_cosine_similarity():
    """Visual explanation of cosine similarity."""
    print("=" * 60)
    print("COSINE SIMILARITY - STEP BY STEP")
    print("=" * 60)
    
    # Example vectors
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    
    print(f"\nVectors:")
    print(f"  A = {vec1}")
    print(f"  B = {vec2}")
    
    print("\n" + "-" * 40)
    print("STEP 1: Compute Dot Product (A · B)")
    print("-" * 40)
    
    dot_product = 0
    for i, (a, b) in enumerate(zip(vec1, vec2)):
        product = a * b
        dot_product += product
        print(f"  A[{i}] × B[{i}] = {a} × {b} = {product}")
    print(f"\n  A · B = {dot_product}")
    
    print("\n" + "-" * 40)
    print("STEP 2: Compute Magnitude of A (||A||)")
    print("-" * 40)
    
    sum_sq_a = 0
    for i, a in enumerate(vec1):
        sum_sq_a += a ** 2
        print(f"  A[{i}]² = {a}² = {a**2}")
    magnitude1 = math.sqrt(sum_sq_a)
    print(f"\n  ||A|| = √{sum_sq_a} = {magnitude1:.4f}")
    
    print("\n" + "-" * 40)
    print("STEP 3: Compute Magnitude of B (||B||)")
    print("-" * 40)
    
    sum_sq_b = 0
    for i, b in enumerate(vec2):
        sum_sq_b += b ** 2
        print(f"  B[{i}]² = {b}² = {b**2}")
    magnitude2 = math.sqrt(sum_sq_b)
    print(f"\n  ||B|| = √{sum_sq_b} = {magnitude2:.4f}")
    
    print("\n" + "-" * 40)
    print("STEP 4: Compute Cosine Similarity")
    print("-" * 40)
    
    similarity = dot_product / (magnitude1 * magnitude2)
    print(f"\n  cos(θ) = (A · B) / (||A|| × ||B||)")
    print(f"         = {dot_product} / ({magnitude1:.4f} × {magnitude2:.4f})")
    print(f"         = {dot_product} / {magnitude1 * magnitude2:.4f}")
    print(f"         = {similarity:.4f}")
    
    print("\nINTERPRETATION:")
    print("─" * 40)
    print("• cos = 1.0  → Vectors point in same direction (identical)")
    print("• cos = 0.0  → Vectors are perpendicular (unrelated)")
    print("• cos = -1.0 → Vectors point in opposite directions")
    print(f"\n• Our result ({similarity:.4f}) → Vectors are very similar!")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_cosine_similarity()
    
    print("\n" + "=" * 60)
    print("COSINE SIMILARITY - TEST CASES")
    print("=" * 60)
    
    # Create sample DataFrame with word embeddings
    data = {
        'word': ['king', 'queen', 'man', 'woman', 'apple'],
        'dim_0': [0.5, 0.4, 0.3, 0.2, 0.8],
        'dim_1': [0.8, 0.9, 0.2, 0.3, 0.1],
        'dim_2': [0.3, 0.4, 0.7, 0.8, 0.2],
        'dim_3': [0.6, 0.5, 0.4, 0.3, 0.9],
        'dim_4': [0.2, 0.3, 0.6, 0.7, 0.1],
    }
    df = pd.DataFrame(data)
    
    print("\nWord Embeddings DataFrame:")
    print(df.to_string(index=False))
    
    # Test Case 1: Similar words
    sim = get_word_similarity(df, 'king', 'queen')
    print(f"\nTest 1: similarity('king', 'queen') = {sim:.4f}")
    print("  (Expected: High similarity - both are royalty)")
    
    # Test Case 2: Related words
    sim = get_word_similarity(df, 'man', 'woman')
    print(f"\nTest 2: similarity('man', 'woman') = {sim:.4f}")
    print("  (Expected: High similarity - both are people)")
    
    # Test Case 3: Unrelated words
    sim = get_word_similarity(df, 'king', 'apple')
    print(f"\nTest 3: similarity('king', 'apple') = {sim:.4f}")
    print("  (Expected: Lower similarity - less related)")
    
    # Test Case 4: Identical vectors
    vec = [1, 2, 3]
    sim = cosine_similarity(vec, vec)
    print(f"\nTest 4: similarity([1,2,3], [1,2,3]) = {sim:.4f}")
    print("  (Expected: 1.0 - identical vectors)")
    
    # Test Case 5: Opposite vectors
    vec1 = [1, 0]
    vec2 = [-1, 0]
    sim = cosine_similarity(vec1, vec2)
    print(f"\nTest 5: similarity([1,0], [-1,0]) = {sim:.4f}")
    print("  (Expected: -1.0 - opposite directions)")
    
    # Test Case 6: Perpendicular vectors
    vec1 = [1, 0]
    vec2 = [0, 1]
    sim = cosine_similarity(vec1, vec2)
    print(f"\nTest 6: similarity([1,0], [0,1]) = {sim:.4f}")
    print("  (Expected: 0.0 - perpendicular vectors)")
    
    print("\n" + "=" * 60)
