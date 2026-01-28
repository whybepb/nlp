# 4. Causal Masking 🎭

## 🎯 Problem Summary
Create an n×n matrix where position i can only attend to positions ≤ i (no cheating by looking at future!).

---

## 📚 Theory & Concepts

### What is Causal Masking?
Causal masking (also called **autoregressive masking**) ensures that when predicting a token, the model can only "see" previous tokens - NOT future ones!

### Why "Causal"?
In time series, **cause comes before effect**. When generating text:
- To predict word 3, you can only use words 1 and 2
- You can't "cheat" by looking at word 4!

### Visual Representation

```
For sequence: [The, cat, sat, on]
              pos 0  1    2   3

Attention allowed (0 = allowed, -1e9 = blocked):

         The   cat   sat   on
         [0]   [1]   [2]   [3]
The [0]   ✓     ✗     ✗     ✗
cat [1]   ✓     ✓     ✗     ✗
sat [2]   ✓     ✓     ✓     ✗
on  [3]   ✓     ✓     ✓     ✓

Mask Matrix (n=4):
         j→    0     1     2     3
i↓
0          [  0   -1e9  -1e9  -1e9 ]
1          [  0     0   -1e9  -1e9 ]
2          [  0     0     0   -1e9 ]
3          [  0     0     0     0  ]
```

### The Rule
```
M[i][j] = 0      if j ≤ i    (can attend: past or self)
M[i][j] = -1e9   if j > i    (blocked: future)
```

---

## 🧠 Memory Tricks

### 1. **Lower Triangle = Free** 🔺
- The mask is essentially a **lower triangular matrix**
- Lower triangle (including diagonal) = 0 (allowed)
- Upper triangle = -∞ (blocked)

### 2. **"No Spoilers" Rule** 📖
Like reading a book - you can't look ahead!
- Current position (diagonal) = OK
- Past (below diagonal) = OK
- Future (above diagonal) = BLOCKED

### 3. **Column vs Row Thinking**
- Row i = what position i can attend TO
- Row i sees: positions 0, 1, 2, ..., i ✓
- Row i can't see: positions i+1, i+2, ... ✗

### 4. **Why -1e9?**
- When added to attention scores and passed through softmax
- exp(-1e9) ≈ 0 (essentially zero probability)
- Acts as "negative infinity" in practice

---

## 💡 Key Insights

### Matrix Pattern:
```python
# n = 3
[[ 0  -inf -inf ]    # Position 0: sees only itself
 [ 0   0   -inf ]    # Position 1: sees 0, 1
 [ 0   0    0  ]]    # Position 2: sees 0, 1, 2
```

### Properties:
1. **Diagonal is always 0**: Each position can attend to itself
2. **First column is always 0**: Everyone can see position 0
3. **Last row is all 0s**: Last position sees everything before it
4. **Upper triangle = -1e9**: Future is always blocked

---

## 🔧 Complete Solution

```python
import numpy as np

def causal_mask(n):
    """
    Generate n×n causal mask matrix.
    
    M[i][j] = 0 if j <= i (allowed)
    M[i][j] = -1e9 if j > i (masked)
    
    Args:
        n: Sequence length
    
    Returns:
        n×n numpy array
    """
    # Create matrix filled with -1e9
    mask = np.full((n, n), -1e9)
    
    # Fill lower triangle (including diagonal) with 0
    for i in range(n):
        for j in range(i + 1):  # j goes from 0 to i (inclusive)
            mask[i][j] = 0
    
    return mask

# Alternative using numpy's tril (lower triangle)
def causal_mask_numpy(n):
    # Create matrix of -1e9
    mask = np.full((n, n), -1e9)
    # Get lower triangular indices (including diagonal)
    tril_indices = np.tril_indices(n)
    mask[tril_indices] = 0
    return mask

# Even simpler one-liner!
def causal_mask_oneliner(n):
    return np.triu(np.full((n, n), -1e9), k=1)
    # triu = upper triangle, k=1 means above diagonal

# Print with scientific notation
def print_mask(mask):
    for row in mask:
        print(' '.join(f'{val:.4e}' for val in row))

# Example
n = 3
mask = causal_mask(n)
print_mask(mask)
```

### Output for n=3:
```
0.0000e+00 -1.0000e+09 -1.0000e+09
0.0000e+00 0.0000e+00 -1.0000e+09
0.0000e+00 0.0000e+00 0.0000e+00
```

---

## 🎓 Transformer Context

### Where is This Used?
1. **GPT-style models**: Decoder-only, always use causal masking
2. **Decoder in Encoder-Decoder**: Like in original Transformer
3. **Language Modeling**: Predicting next word

### How It Works with Attention:
```python
# In transformer attention:
attention_scores = Q @ K.T / sqrt(d_k)
attention_scores += causal_mask  # Add the mask!
attention_weights = softmax(attention_scores)
# Now future positions have ~0 weight
```

### Comparison with Other Masks:
| Mask Type | Used In | Pattern |
|-----------|---------|---------|
| Causal | GPT, Decoder | Lower triangle |
| Padding | All | Mask padding tokens |
| Full | BERT Encoder | No masking (see all) |

---

## 🔍 Quick Reference

```python
# Different ways to create causal mask:

# Method 1: Loop
mask = np.full((n, n), -1e9)
for i in range(n):
    for j in range(i + 1):
        mask[i][j] = 0

# Method 2: np.triu (upper triangle)
mask = np.triu(np.full((n, n), -1e9), k=1)

# Method 3: np.tril (lower triangle)
mask = np.where(np.tril(np.ones((n, n))), 0, -1e9)

# Method 4: Pure numpy
mask = np.full((n, n), -1e9)
mask[np.tril_indices(n)] = 0
```

---

## ⚠️ Common Mistakes

1. **Confusing row/column indices**: i is row (current pos), j is column (attending to)
2. **Using wrong inequality**: j ≤ i (not j < i) - diagonal is included!
3. **Using 0 and 1 instead of 0 and -1e9**: Mask is ADDITIVE, not multiplicative
4. **Wrong scientific notation format**: Use `.4e` not `.2e` as per problem
5. **Off-by-one in loop**: `range(i+1)` not `range(i)`
