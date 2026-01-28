# 7. Cosine Similarity 📐

## 🎯 Problem Summary
Calculate how similar two word vectors are by measuring the cosine of the angle between them.

## 📚 Formula
```
cosine_sim(A, B) = (A · B) / (||A|| × ||B||)
```

## 🧠 Memory Tricks
- **"DOT over NORMS"**: Dot product divided by product of magnitudes
- Range: [-1, 1] where 1 = identical, 0 = perpendicular, -1 = opposite

## 🔧 Complete Solution

```python
import pandas as pd
import numpy as np

def get_vector(word, df):
    row = df[df['word'] == word]
    vector = row[['dim1', 'dim2', 'dim3', 'dim4', 'dim5']].values[0]
    return np.array(vector)

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    return dot_product / (norm1 * norm2)
```

## ⚠️ Common Mistakes
- Division by zero with empty vectors
- Confusing similarity (higher=similar) vs distance (lower=similar)
