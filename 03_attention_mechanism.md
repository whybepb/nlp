# 3. Attention Mechanism 🎯

## 🎯 Problem Summary
Implement attention: Given a query and key-value pairs, compute attention-weighted sum of values.

---

## 📚 Theory & Concepts

### What is Attention?
Attention allows a model to **focus on relevant parts** of the input. Think of it like a spotlight that highlights what's important!

### The Analogy 🔦
Imagine you're in a library:
- **Query (Q)**: What you're looking for ("books about Python")
- **Keys (K)**: Book titles (help you find relevant books)
- **Values (V)**: Book contents (what you actually want to read)

### The Three-Step Process

```
Step 1: COMPARE      Step 2: NORMALIZE     Step 3: COMBINE
   Q                    Scores                Weights
   ↓                      ↓                     ↓
┌─────┐               ┌─────┐              ┌─────┐
│Q·K₁ │→ score₁  →    │ w₁  │  ────────→   │w₁V₁│
├─────┤               ├─────┤              ├─────┤
│Q·K₂ │→ score₂  →    │ w₂  │  ────────→   │w₂V₂│ → SUM → Output
├─────┤   softmax     ├─────┤              ├─────┤
│Q·K₃ │→ score₃  →    │ w₃  │  ────────→   │w₃V₃│
└─────┘               └─────┘              └─────┘
```

### Core Formulas

1. **Similarity Scores**: `scores = Q · Kᵀ` (dot product)
2. **Attention Weights**: `weights = softmax(scores)`
3. **Output**: `output = weights · V` (weighted sum)

---

## 🧠 Memory Tricks

### 1. **"QKV" = "Question, Keywords, Values"**
- **Q**uery = Your question
- **K**eys = Keywords to match
- **V**alues = The actual answers

### 2. **"Score → Soft → Sum"**
1. **Score**: Compute similarity (dot product)
2. **Soft**max: Normalize to probabilities
3. **Sum**: Weighted combination

### 3. **The Restaurant Analogy** 🍽️
- Q = "I want spicy food"
- K = Menu item names (match against your preference)
- V = Actual dishes
- Attention = How much you consider each dish based on "spicy" keyword

---

## 💡 Key Insights

### Why Dot Product for Similarity?
- If vectors point in same direction → HIGH score
- If perpendicular → ZERO score
- If opposite → NEGATIVE score

### Why Softmax?
- Converts scores to probabilities (sum to 1)
- Makes the math differentiable
- Formula: `softmax(xᵢ) = exp(xᵢ) / Σexp(xⱼ)`

### Attention Properties:
1. **Weighted Average**: Output is a blend of all values
2. **Differentiable**: Can backpropagate through it
3. **Dynamic**: Weights change based on query

---

## 🔧 Complete Solution

```python
import numpy as np

def attention(query, keys, values):
    """
    Compute attention-weighted sum of values.
    
    Args:
        query: Query vector (d,)
        keys: Key vectors (n, d)
        values: Value vectors (n, d)
    
    Returns:
        Weighted sum of values (d,)
    """
    # Convert to numpy arrays
    query = np.array(query)
    keys = np.array(keys)
    values = np.array(values)
    
    # Step 1: Compute similarity scores (dot product)
    # query (d,) dot keys (n, d) → scores (n,)
    scores = np.dot(keys, query)
    
    # Step 2: Apply softmax to get attention weights
    # Subtract max for numerical stability
    exp_scores = np.exp(scores - np.max(scores))
    weights = exp_scores / np.sum(exp_scores)
    
    # Step 3: Compute weighted sum of values
    # weights (n,) × values (n, d) → output (d,)
    output = np.dot(weights, values)
    
    return output.tolist()


# Example walkthrough
query = [0.5, 0.5]
keys = [[0.1, 0.2], [0.2, 0.3]]
values = [[0.6, 0.8], [0.7, 0.9]]

result = attention(query, keys, values)
print(result)  # [0.6524979187478941, 0.852497918747894]
```

### Step-by-Step Example:

```python
# Given:
query = [0.5, 0.5]
keys = [[0.1, 0.2], [0.2, 0.3]]
values = [[0.6, 0.8], [0.7, 0.9]]

# Step 1: Scores
score_1 = 0.5*0.1 + 0.5*0.2 = 0.05 + 0.10 = 0.15
score_2 = 0.5*0.2 + 0.5*0.3 = 0.10 + 0.15 = 0.25
scores = [0.15, 0.25]

# Step 2: Softmax
exp_scores = [exp(0.15), exp(0.25)] = [1.1618, 1.2840]
sum_exp = 2.4458
weights = [0.4752, 0.5248]  # sums to 1!

# Step 3: Weighted Sum
output_dim1 = 0.4752*0.6 + 0.5248*0.7 = 0.6525
output_dim2 = 0.4752*0.8 + 0.5248*0.9 = 0.8525
output = [0.6525, 0.8525]
```

---

## 🎓 NLP/Transformer Context

### In Transformers:
- **Self-Attention**: Q, K, V all come from same input
- **Cross-Attention**: Q from one source, K/V from another
- **Multi-Head**: Multiple attention computations in parallel

### Scaled Dot-Product Attention:
In Transformers, we scale by √d to prevent extreme softmax values:
```
Attention(Q,K,V) = softmax(QKᵀ/√d) · V
```

### Types of Attention:
1. **Dot-Product**: Our implementation (fastest)
2. **Additive (Bahdanau)**: Uses neural network
3. **Multiplicative (Luong)**: With learnable matrix

---

## 🔍 Dimension Cheat Sheet

```
query:   (d,)           - d = dimension
keys:    (n, d)         - n = number of key-value pairs
values:  (n, d)

Computation:
keys · query    → (n, d) × (d,) = (n,)  → scores
softmax(scores) → (n,)                  → weights
weights · values→ (n,) × (n, d) = (d,)  → output
```

---

## ⚠️ Common Mistakes

1. **Numerical Instability**: Always subtract max before softmax
2. **Dimension Confusion**: Keys go on left in dot product with query
3. **Forgetting Softmax**: Without it, weights don't sum to 1
4. **Not Converting to List**: Remember to return Python list, not numpy array
