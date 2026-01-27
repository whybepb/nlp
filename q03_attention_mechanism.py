"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 3: ATTENTION MECHANISM                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Implement a simple attention mechanism for a sequence of vectors.             ║
║ Given a query vector and a set of key-value pairs, compute the               ║
║ attention-weighted sum of the values.                                         ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ Attention allows a model to focus on relevant parts of the input.            ║
║                                                                               ║
║ Steps:                                                                        ║
║ 1. Compute similarity scores: score_i = query · key_i (dot product)         ║
║ 2. Apply softmax: weights = softmax(scores)                                   ║
║ 3. Weighted sum: output = Σ(weight_i × value_i)                              ║
║                                                                               ║
║ SOFTMAX Formula:                                                              ║
║   softmax(x_i) = exp(x_i) / Σexp(x_j)                                        ║
║                                                                               ║
║ VISUAL EXAMPLE:                                                               ║
║   Query: "What is the color?"                                                 ║
║   Keys:  ["color", "size", "shape"]                                           ║
║   Values: [red_embedding, large_embedding, round_embedding]                   ║
║                                                                               ║
║   The query will have high attention on "color", so the output will be       ║
║   mostly the red_embedding.                                                   ║
║                                                                               ║
║ INPUT:                                                                        ║
║   query: list[float] - Query vector                                           ║
║   keys: list[list[float]] - List of key vectors                              ║
║   values: list[list[float]] - List of value vectors                          ║
║                                                                               ║
║ OUTPUT:                                                                       ║
║   list[float] - Attention-weighted sum of values                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import numpy as np

def softmax(x):
    """
    Compute softmax values for each element in x.
    
    Formula: softmax(x_i) = exp(x_i) / sum(exp(x_j))
    
    We subtract max(x) for numerical stability (prevents overflow).
    """
    # Subtract max for numerical stability
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum()


def attention_mechanism(query, keys, values):
    """
    Implement simple attention mechanism.
    
    Args:
        query: Query vector (list or array)
        keys: List of key vectors
        values: List of value vectors
    
    Returns:
        Attention-weighted sum of values (as Python list)
    """
    # Step 1: Convert inputs to numpy arrays if needed
    query = np.array(query)
    keys = np.array(keys)
    values = np.array(values)
    
    # Step 2: Compute similarity scores between query and each key
    # Using dot product: score_i = query · key_i
    scores = np.dot(keys, query)  # Shape: (num_keys,)
    
    # Step 3: Apply softmax to obtain attention weights
    attention_weights = softmax(scores)  # Shape: (num_keys,)
    
    # Step 4: Compute weighted sum of values
    # output = Σ(weight_i × value_i)
    output = np.zeros_like(values[0])
    for i in range(len(values)):
        output = output + attention_weights[i] * values[i]
    
    # Alternative (more compact): output = np.dot(attention_weights, values)
    
    # Step 5: Return result as Python list
    return output.tolist()


def attention_mechanism_v2(query, keys, values):
    """Alternative compact implementation"""
    query = np.array(query)
    keys = np.array(keys)
    values = np.array(values)
    
    # Compute attention scores and weights
    scores = np.dot(keys, query)
    weights = softmax(scores)
    
    # Weighted sum using matrix multiplication
    output = np.dot(weights, values)
    
    return output.tolist()


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_attention():
    """Visual step-by-step walkthrough of attention mechanism."""
    print("=" * 60)
    print("ATTENTION MECHANISM - STEP BY STEP")
    print("=" * 60)
    
    # Example data
    query = [1.0, 0.5, 0.2]
    keys = [
        [1.0, 0.0, 0.0],   # Key 1 (similar to query in first dim)
        [0.0, 1.0, 0.0],   # Key 2
        [0.0, 0.0, 1.0],   # Key 3
    ]
    values = [
        [10.0, 0.0],   # Value 1
        [0.0, 10.0],   # Value 2
        [5.0, 5.0],    # Value 3
    ]
    
    print(f"\nQuery: {query}")
    print(f"Keys:  {keys}")
    print(f"Values: {values}")
    
    # Step 1: Compute scores
    print("\n" + "-" * 40)
    print("STEP 1: Compute Similarity Scores (Dot Product)")
    print("-" * 40)
    query = np.array(query)
    keys = np.array(keys)
    values = np.array(values)
    
    scores = []
    for i, key in enumerate(keys):
        score = np.dot(query, key)
        scores.append(score)
        print(f"  score[{i}] = query · key[{i}] = {query} · {key} = {score}")
    
    scores = np.array(scores)
    print(f"\nScores: {scores}")
    
    # Step 2: Apply softmax
    print("\n" + "-" * 40)
    print("STEP 2: Apply Softmax")
    print("-" * 40)
    print("  softmax(x_i) = exp(x_i) / Σexp(x_j)")
    
    exp_scores = np.exp(scores - np.max(scores))
    print(f"  exp(scores) = {exp_scores}")
    print(f"  sum(exp(scores)) = {exp_scores.sum()}")
    
    weights = softmax(scores)
    print(f"\nAttention Weights: {weights}")
    print(f"  (Notice: Key 0 has highest weight because it's most similar to query)")
    
    # Step 3: Weighted sum
    print("\n" + "-" * 40)
    print("STEP 3: Compute Weighted Sum of Values")
    print("-" * 40)
    
    output = np.zeros_like(values[0])
    for i in range(len(values)):
        contribution = weights[i] * values[i]
        print(f"  weight[{i}] × value[{i}] = {weights[i]:.4f} × {values[i]} = {contribution}")
        output = output + contribution
    
    print(f"\nFinal Output (sum): {output}")
    print(f"  (Notice: Output is closer to Value 0 because Key 0 had highest attention)")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_attention()
    
    print("\n" + "=" * 60)
    print("ATTENTION MECHANISM - TEST CASES")
    print("=" * 60)
    
    # Test Case 1
    query = [1.0, 0.0]
    keys = [[1.0, 0.0], [0.0, 1.0]]
    values = [[10.0], [20.0]]
    result = attention_mechanism(query, keys, values)
    print(f"\nTest 1:")
    print(f"  Query: {query}")
    print(f"  Keys: {keys}")
    print(f"  Values: {values}")
    print(f"  Result: {result}")
    print(f"  (Query is identical to Key0, so output ≈ Value0)")
    
    # Test Case 2: Equal attention
    query = [1.0, 1.0]
    keys = [[1.0, 0.0], [0.0, 1.0]]
    values = [[10.0], [20.0]]
    result = attention_mechanism(query, keys, values)
    print(f"\nTest 2:")
    print(f"  Query: {query}")
    print(f"  Keys: {keys}")
    print(f"  Values: {values}")
    print(f"  Result: {result}")
    print(f"  (Query is equally similar to both keys, so output ≈ average)")
    
    print("\n" + "=" * 60)
