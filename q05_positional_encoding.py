"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 5: POSITIONAL ENCODING                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Transformers cannot understand sequence order by themselves. To solve this,  ║
║ we add positional embeddings to input embeddings.                             ║
║                                                                               ║
║ Generate sinusoidal positional embeddings defined as:                         ║
║   PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))                              ║
║   PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))                              ║
║                                                                               ║
║ Where:                                                                        ║
║   - pos = position in the sequence (0, 1, 2, ...)                            ║
║   - i = dimension index (0, 1, 2, ...)                                        ║
║   - d_model = total embedding dimension                                       ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ Unlike RNNs that process sequentially, Transformers see all positions at     ║
║ once. We need to "tell" them the order using positional encodings.           ║
║                                                                               ║
║ Why sinusoidal?                                                               ║
║ 1. Each position gets a unique encoding                                       ║
║ 2. The model can learn to attend to relative positions                       ║
║ 3. Works for sequences longer than those seen during training                ║
║                                                                               ║
║ PATTERN:                                                                      ║
║   Even dimensions (0, 2, 4, ...) use sin                                      ║
║   Odd dimensions (1, 3, 5, ...)  use cos                                      ║
║                                                                               ║
║ INPUT:                                                                        ║
║   seq_len: Length of sequence                                                 ║
║   d_model: Embedding dimension                                                ║
║                                                                               ║
║ OUTPUT:                                                                       ║
║   Matrix of shape (seq_len, d_model) containing positional encodings         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import numpy as np

def positional_encoding(seq_len: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encoding.
    
    Args:
        seq_len: Number of positions in the sequence
        d_model: Dimension of the embedding
    
    Returns:
        Array of shape (seq_len, d_model) with positional encodings
    """
    # Initialize the positional encoding matrix
    PE = np.zeros((seq_len, d_model))
    
    # For each position in the sequence
    for pos in range(seq_len):
        # For each dimension
        for i in range(d_model):
            # Calculate the angle
            # Note: we use i//2 because formula uses 2i
            angle = pos / (10000 ** ((2 * (i // 2)) / d_model))
            
            if i % 2 == 0:
                # Even dimension: use sin
                PE[pos, i] = np.sin(angle)
            else:
                # Odd dimension: use cos
                PE[pos, i] = np.cos(angle)
    
    return PE


def positional_encoding_vectorized(seq_len: int, d_model: int) -> np.ndarray:
    """Vectorized version (more efficient)."""
    # Create position indices: [0, 1, 2, ..., seq_len-1]
    position = np.arange(seq_len).reshape(-1, 1)  # Shape: (seq_len, 1)
    
    # Create dimension indices for even dimensions: [0, 2, 4, ...]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
    # This is equivalent to: 1 / 10000^(2i/d_model)
    
    # Initialize PE matrix
    PE = np.zeros((seq_len, d_model))
    
    # Calculate angles
    angles = position * div_term  # Broadcasting: (seq_len, 1) * (d_model/2,) = (seq_len, d_model/2)
    
    # Even dimensions: sin
    PE[:, 0::2] = np.sin(angles)
    
    # Odd dimensions: cos
    PE[:, 1::2] = np.cos(angles)
    
    return PE


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_positional_encoding():
    """Visual explanation of positional encoding."""
    print("=" * 60)
    print("POSITIONAL ENCODING - STEP BY STEP")
    print("=" * 60)
    
    seq_len = 4
    d_model = 6
    
    print(f"\nParameters: seq_len={seq_len}, d_model={d_model}")
    
    print("\nFORMULA BREAKDOWN:")
    print("─" * 40)
    print("PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))")
    print("PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))")
    print()
    print("Even indices (0, 2, 4) → sin")
    print("Odd indices (1, 3, 5)  → cos")
    
    print("\n" + "-" * 40)
    print("CALCULATING STEP BY STEP:")
    print("-" * 40)
    
    PE = np.zeros((seq_len, d_model))
    
    # Show calculation for first few positions and dimensions
    for pos in range(min(2, seq_len)):
        print(f"\n📍 Position {pos}:")
        for i in range(d_model):
            angle_denom = 10000 ** ((2 * (i // 2)) / d_model)
            angle = pos / angle_denom
            
            if i % 2 == 0:
                value = np.sin(angle)
                func = "sin"
            else:
                value = np.cos(angle)
                func = "cos"
            
            PE[pos, i] = value
            
            print(f"  dim {i}: {func}({pos} / 10000^({2*(i//2)}/{d_model})) = {func}({angle:.4f}) = {value:.4f}")
    
    print("\n" + "-" * 40)
    print("COMPLETE ENCODING MATRIX:")
    print("-" * 40)
    
    PE = positional_encoding(seq_len, d_model)
    
    # Print header
    print("\n        ", end="")
    for i in range(d_model):
        print(f"dim{i:02d}  ", end="")
    print()
    
    for pos in range(seq_len):
        print(f"pos {pos}: [", end="")
        for i in range(d_model):
            print(f"{PE[pos, i]:6.3f} ", end="")
        print("]")
    
    print("\nKEY OBSERVATIONS:")
    print("─" * 40)
    print("1. Each position has a unique encoding")
    print("2. Lower dimensions change faster (high frequency)")
    print("3. Higher dimensions change slower (low frequency)")
    print("4. This allows the model to use both absolute and relative positions")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_positional_encoding()
    
    print("\n" + "=" * 60)
    print("POSITIONAL ENCODING - TEST CASES")
    print("=" * 60)
    
    # Test Case 1
    PE = positional_encoding(4, 4)
    print("\nTest 1: seq_len=4, d_model=4")
    print(PE.round(4))
    
    # Test Case 2: Check position 0
    PE = positional_encoding(1, 8)
    print("\nTest 2: Position 0, d_model=8")
    print(f"PE[0] = {PE[0].round(4)}")
    print("Expected: [sin(0), cos(0), sin(0), cos(0), ...] = [0, 1, 0, 1, ...]")
    
    # Test Case 3: Verify both methods give same result
    PE1 = positional_encoding(10, 16)
    PE2 = positional_encoding_vectorized(10, 16)
    print("\nTest 3: Comparing loop vs vectorized implementation")
    print(f"Same result: {np.allclose(PE1, PE2)}")
    
    # Visual: Plot the encoding (text-based)
    print("\n" + "=" * 60)
    print("VISUALIZATION: First 4 dimensions across 10 positions")
    print("=" * 60)
    
    PE = positional_encoding(10, 8)
    for dim in range(4):
        print(f"\nDimension {dim} ({'sin' if dim % 2 == 0 else 'cos'}):")
        for pos in range(10):
            value = PE[pos, dim]
            bar_length = int((value + 1) * 20)  # Scale to 0-40
            print(f"  pos {pos}: {'█' * bar_length}{'░' * (40 - bar_length)} {value:.3f}")
    
    print("\n" + "=" * 60)
