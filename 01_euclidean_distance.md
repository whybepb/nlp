# 1. Euclidean Distance 📏

## 🎯 Problem Summary
Calculate the straight-line distance between two points in n-dimensional space, rounded to 2 decimal places.

---

## 📚 Theory & Concepts

### What is Euclidean Distance?
Euclidean distance is the **"ordinary" straight-line distance** between two points in Euclidean space. Think of it as the length of a ruler placed between two points.

### Formula
For two points P = (p₁, p₂, ..., pₙ) and Q = (q₁, q₂, ..., qₙ):

```
d(P, Q) = √[(p₁-q₁)² + (p₂-q₂)² + ... + (pₙ-qₙ)²]
```

### In 2D (Simple case):
```
d = √[(x₂-x₁)² + (y₂-y₁)²]
```

### In 3D:
```
d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]
```

---

## 🧠 Memory Tricks

### 1. **"SSD" Method** - Sum of Squared Differences
1. **S**ubtract corresponding coordinates
2. **S**quare each difference  
3. **D**istance = Square root of sum

### 2. **Pythagorean Theorem Extension**
- In 2D: It's literally the Pythagorean theorem (a² + b² = c²)
- In higher dimensions: Just keep adding more squared terms!

### 3. **Visual Memory**
```
Point A ●───────────────● Point B
        └──────d────────┘
```
The line connecting them is the Euclidean distance.

---

## 💡 Key Insights

1. **Dimension Matching**: Points MUST have the same number of dimensions
2. **Always Positive**: Distance is always ≥ 0
3. **Symmetric**: d(A,B) = d(B,A)
4. **Zero means same point**: d(A,B) = 0 if and only if A = B

---

## 🔧 Complete Solution

```python
import math

def euclidean_distance(point1, point2):
    # Check dimensions match
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensions")
    
    # Calculate squared differences and sum them
    squared_distance = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    
    # Take square root
    distance = math.sqrt(squared_distance)
    
    return round(distance, 2)

# Example
point1 = [1, 2, 3]
point2 = [3, 4, 5]
print(euclidean_distance(point1, point2))  # Output: 3.46
```

### Step-by-step for [1,2,3] and [3,4,5]:
```
(3-1)² + (4-2)² + (5-3)² 
= 2² + 2² + 2²
= 4 + 4 + 4
= 12
√12 ≈ 3.46
```

---

## 🎓 NLP/ML Context

Euclidean distance is used in:
- **K-Nearest Neighbors (KNN)** - Finding similar data points
- **Word Embeddings** - Measuring word similarity (though cosine is preferred)
- **Clustering (K-Means)** - Grouping similar items
- **Recommendation Systems** - Finding similar users/items

---

## ⚠️ Common Mistakes
1. Forgetting to check dimension equality
2. Not squaring the differences
3. Forgetting the square root
4. Rounding at wrong step (always round at the END)
