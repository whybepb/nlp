# 5. Positional Encoding 📍

## 🎯 Problem Summary
Add sinusoidal positional embeddings to input embeddings so Transformers understand sequence order.

---

## 📚 Theory & Concepts

### Why Do We Need This?
Transformers have **no inherent sense of order**! Unlike RNNs that process sequentially, Transformers see all tokens at once. Without positional encoding:
- "The cat sat" = "sat cat The" (same to the model!)

### The Sinusoidal Formula

For position `pos` and dimension `i`:

```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))    # Even dimensions
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))    # Odd dimensions
```

Where:
- `pos`: Position in sequence (0, 1, 2, ...)
- `i`: Dimension index (0, 1, 2, ..., d_model/2)
- `d_model`: Total embedding dimension

### Visual Pattern

```
Position →  0    1    2    3    4
          ┌────┬────┬────┬────┬────┐
dim 0 sin │ 0  │.84 │.91 │.14 │-.76│  ← Fast oscillation
dim 1 cos │ 1  │.54 │-.42│-.99│-.65│
dim 2 sin │ 0  │.01 │.02 │.03 │.04 │  ← Slow oscillation
dim 3 cos │ 1  │.99 │.99 │.99 │.99 │
          └────┴────┴────┴────┴────┘

Result: Each position has a UNIQUE pattern!
```

---

## 🧠 Memory Tricks

### 1. **"SPEC" Pattern**
- **S**in for even (0, 2, 4...)
- **C**os for odd (1, 3, 5...)
- **P**osition varies
- **E**xponent decreases frequency for higher dims

### 2. **Think of Radio Waves** 📻
- Low dimensions (0, 1) = High frequency (fast changes)
- High dimensions = Low frequency (slow changes)
- Together they create a unique "fingerprint" for each position

### 3. **The 10000 Magic Number**
- 10000^(2i/d) controls the wavelength
- When i=0: wavelength = 2π
- When i=d/2: wavelength = 20000π
- Gives a wide range of frequencies

### 4. **Why Sin AND Cos?**
- They're 90° out of phase
- PE(pos + k) can be expressed as linear combination of PE(pos)
- Helps model learn relative positions!

---

## 💡 Key Insights

### Key Properties:
1. **Deterministic**: No learning needed - computed mathematically
2. **Unique per Position**: Each pos has distinct encoding
3. **Bounded Values**: Always in [-1, 1] range
4. **Relative Position**: Model can learn offsets easily

### The Dimension Breakdown:
```
d_model = 4 example:

dim 0 (i=0): sin(pos / 10000^0) = sin(pos)       ← Fastest
dim 1 (i=0): cos(pos / 10000^0) = cos(pos)
dim 2 (i=1): sin(pos / 10000^0.5) = sin(pos/100) ← Slower
dim 3 (i=1): cos(pos / 10000^0.5) = cos(pos/100)
```

---

## 🔧 Complete Solution

```python
import numpy as np

def get_positional_encoding(seq_len, d_model):
    """
    Generate sinusoidal positional encodings.
    
    Args:
        seq_len: Length of sequence
        d_model: Embedding dimension
    
    Returns:
        (seq_len, d_model) positional encoding matrix
    """
    # Create position indices: [0, 1, 2, ..., seq_len-1]
    positions = np.arange(seq_len)[:, np.newaxis]  # Shape: (seq_len, 1)
    
    # Create dimension indices: [0, 1, 2, ..., d_model-1]
    dims = np.arange(d_model)[np.newaxis, :]  # Shape: (1, d_model)
    
    # Compute the angle rates
    # For dimension i: 1 / (10000^(2*(i//2)/d_model))
    i = dims // 2  # Integer division: 0,0,1,1,2,2,...
    angle_rates = 1 / np.power(10000, (2 * i) / d_model)
    
    # Compute angles
    angles = positions * angle_rates  # Broadcasting: (seq_len, d_model)
    
    # Apply sin to even indices, cos to odd indices
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angles[:, 0::2])  # Even: 0, 2, 4, ...
    pe[:, 1::2] = np.cos(angles[:, 1::2])  # Odd: 1, 3, 5, ...
    
    return pe


def add_positional_encoding(X):
    """
    Add positional encoding to input embeddings.
    
    Args:
        X: Input embeddings (seq_len, d_model)
    
    Returns:
        X + positional encoding
    """
    X = np.array(X)
    seq_len, d_model = X.shape
    pe = get_positional_encoding(seq_len, d_model)
    return np.round(X + pe, 4)


# Example
X = np.array([
    [0.1, -0.2, 0.3, 0.4],
    [0.0, 0.5, -0.1, 0.2],
    [0.7, -0.3, 0.2, -0.4]
])

result = add_positional_encoding(X)
for row in result:
    print(' '.join(f'{val:.4f}' for val in row))
```

### Output:
```
0.1000 0.8000 0.3000 1.4000
0.8415 1.0403 -0.0900 1.2000
1.6093 -0.7161 0.2200 0.5998
```

---

## 🔍 Step-by-Step Calculation

For position 0, d_model=4:
```python
# Dimension 0 (i=0, even → sin)
angle = 0 / 10000^(0/4) = 0 / 1 = 0
PE[0,0] = sin(0) = 0

# Dimension 1 (i=0, odd → cos)
angle = 0 / 10000^(0/4) = 0
PE[0,1] = cos(0) = 1

# Dimension 2 (i=1, even → sin)
angle = 0 / 10000^(2/4) = 0
PE[0,2] = sin(0) = 0

# Dimension 3 (i=1, odd → cos)
angle = 0 / 10000^(2/4) = 0
PE[0,3] = cos(0) = 1

# Result: PE[0] = [0, 1, 0, 1]
# Add to input [0.1, -0.2, 0.3, 0.4]:
# [0.1+0, -0.2+1, 0.3+0, 0.4+1] = [0.1, 0.8, 0.3, 1.4] ✓
```

---

## 🎓 Transformer Context

### In the Transformer Architecture:
```
Input → Embedding → + Positional Encoding → Encoder/Decoder
                          ↑
                    (Added, not concatenated!)
```

### Alternatives to Sinusoidal:
1. **Learned Positional Embeddings**: Train them (BERT, GPT)
2. **Relative Positional**: Encode relative distances (T5)
3. **Rotary (RoPE)**: Rotate embeddings (LLaMA)

---

## ⚠️ Common Mistakes

1. **Using `i` vs `i//2`**: The formula uses 2i, so dimension pairs share frequency
2. **Sin/Cos confusion**: Even dims = sin, Odd dims = cos
3. **Forgetting to add**: It's X + PE, not X * PE or concatenation
4. **Rounding too early**: Round only at the end
5. **Wrong broadcasting**: Positions should be column, dims should be row
