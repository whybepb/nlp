"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 4: CAUSAL MASKING                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ In Transformers, a causal mask ensures position i can only attend to itself  ║
║ and previous positions, NOT future positions.                                 ║
║                                                                               ║
║ For sequence length n, generate an n×n matrix M where:                       ║
║   M[i][j] = 0      if j ≤ i  (allowed attention)                             ║
║   M[i][j] = -1e9   if j > i  (masked - very large negative number)           ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ In models like GPT, when predicting the next word, we shouldn't "see"        ║
║ future words. The causal mask achieves this by adding a large negative       ║
║ number to future positions before softmax, making their attention weight ≈ 0 ║
║                                                                               ║
║ VISUAL EXAMPLE (n=4):                                                         ║
║                                                                               ║
║   Position:    0      1      2      3                                         ║
║          ┌─────────────────────────────┐                                      ║
║   0      │   0    -1e9   -1e9   -1e9  │  ← Position 0 can only see itself    ║
║   1      │   0     0     -1e9   -1e9  │  ← Position 1 can see 0 and 1        ║
║   2      │   0     0      0     -1e9  │  ← Position 2 can see 0, 1, 2        ║
║   3      │   0     0      0      0    │  ← Position 3 can see all (0-3)      ║
║          └─────────────────────────────┘                                      ║
║                                                                               ║
║ This is also called a "lower triangular" mask with -1e9 in upper triangle.   ║
║                                                                               ║
║ INPUT:  n (integer) - sequence length                                         ║
║ OUTPUT: n×n matrix as described above                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import numpy as np

def causal_mask(n: int) -> list:
    """
    Generate a causal mask for sequence of length n.
    
    Args:
        n: Sequence length
    
    Returns:
        n×n matrix where M[i][j] = 0 if j <= i, else -1e9
    """
    mask = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if j <= i:
                row.append(0)       # Allowed attention
            else:
                row.append(-1e9)    # Masked (future position)
        mask.append(row)
    
    return mask


def causal_mask_numpy(n: int) -> np.ndarray:
    """Generate causal mask using NumPy (more efficient)."""
    # Create an n×n matrix of zeros
    mask = np.zeros((n, n))
    
    # Set upper triangular part (excluding diagonal) to -1e9
    # np.triu returns upper triangular matrix
    # k=1 means start from first diagonal above main diagonal
    mask = np.triu(np.ones((n, n)) * (-1e9), k=1)
    
    return mask


def causal_mask_v2(n: int) -> np.ndarray:
    """Alternative using np.where"""
    # Create indices
    i = np.arange(n).reshape(-1, 1)  # Column vector [0, 1, 2, ...]
    j = np.arange(n).reshape(1, -1)  # Row vector [0, 1, 2, ...]
    
    # Create mask: 0 where j <= i, -1e9 where j > i
    mask = np.where(j <= i, 0, -1e9)
    
    return mask


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_causal_mask():
    """Visual explanation of causal masking."""
    print("=" * 60)
    print("CAUSAL MASKING - STEP BY STEP")
    print("=" * 60)
    
    n = 4
    print(f"\nSequence length n = {n}")
    print("\nBuilding the mask row by row:")
    print("-" * 40)
    
    for i in range(n):
        print(f"\nRow {i} (Position {i} attending to all positions):")
        row = []
        for j in range(n):
            if j <= i:
                row.append("  0  ")
                status = "✓ CAN see"
            else:
                row.append("-1e9 ")
                status = "✗ CANNOT see"
            print(f"  [{i}][{j}]: {status} position {j}")
        print(f"  Row {i}: [{' '.join(row)}]")
    
    print("\n" + "-" * 40)
    print("COMPLETE MASK:")
    print("-" * 40)
    mask = causal_mask(n)
    
    # Print header
    print("\n         ", end="")
    for j in range(n):
        print(f"j={j}     ", end="")
    print()
    
    for i, row in enumerate(mask):
        print(f"  i={i}  [", end="")
        for j, val in enumerate(row):
            if val == 0:
                print("   0   ", end="")
            else:
                print(" -1e9  ", end="")
        print("]")
    
    print("\nWHY THIS WORKS:")
    print("─" * 40)
    print("1. Before softmax, attention scores are added to this mask")
    print("2. Adding -1e9 (≈ negative infinity) makes exp(score) ≈ 0")
    print("3. After softmax, masked positions have ~0 attention weight")
    print("4. Result: Future tokens are effectively invisible!")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_causal_mask()
    
    print("\n" + "=" * 60)
    print("CAUSAL MASKING - TEST CASES")
    print("=" * 60)
    
    # Test Case 1: n=3
    n = 3
    mask = causal_mask(n)
    print(f"\nTest 1: n={n}")
    print("Mask:")
    for row in mask:
        print(f"  {row}")
    
    # Verify with numpy version
    mask_np = causal_mask_numpy(n)
    print(f"\nNumPy version (same result):")
    print(mask_np)
    
    # Test Case 2: n=5
    n = 5
    mask = causal_mask_numpy(n)
    print(f"\nTest 2: n={n}")
    print("Mask (using NumPy):")
    print(mask)
    
    # Demonstrate the masking effect
    print("\n" + "-" * 40)
    print("DEMONSTRATION: Effect of Masking on Softmax")
    print("-" * 40)
    
    # Raw attention scores (before mask)
    scores = np.array([0.5, 0.3, 0.8, 0.2])
    print(f"\nRaw scores for position 1: {scores}")
    
    # Add causal mask (position 1 can only see 0 and 1)
    mask_row = np.array([0, 0, -1e9, -1e9])
    masked_scores = scores + mask_row
    print(f"Causal mask row:           {mask_row}")
    print(f"After masking:             {masked_scores}")
    
    # Apply softmax
    def softmax(x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()
    
    weights = softmax(masked_scores)
    print(f"After softmax (weights):   {weights}")
    print(f"\nNotice: Positions 2 and 3 have ~0 attention weight!")
    
    print("\n" + "=" * 60)
