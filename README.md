# 🐍 Python NLP Coding Practice - Endterm Preparation

Welcome! This folder contains **10 practice questions** for your NLP coding round. Each file is designed to **teach you the concept first**, then test your understanding.

---

## 📚 How to Use These Files

1. **Run each file** to see the explanation and test cases:
   ```bash
   python q01_euclidean_distance.py
   ```

2. **Read the top of each file** for:
   - Task description
   - Concept explanation
   - Formula breakdown
   - Input/Output format
   - Sample examples

3. **Study the `explain_*()` function** - it walks through each step visually

4. **Try modifying values** in test cases to deepen your understanding

---

## 📋 Question List

| # | File | Topic | Difficulty |
|---|------|-------|------------|
| 1 | `q01_euclidean_distance.py` | Euclidean Distance | ⭐ Easy |
| 2 | `q02_rnn_cell.py` | RNN (Recurrent Neural Network) Cell | ⭐⭐ Medium |
| 3 | `q03_attention_mechanism.py` | Attention Mechanism | ⭐⭐ Medium |
| 4 | `q04_causal_masking.py` | Causal Masking (Transformers) | ⭐⭐ Medium |
| 5 | `q05_positional_encoding.py` | Positional Encoding | ⭐⭐ Medium |
| 6 | `q06_tfidf.py` | TF-IDF Implementation | ⭐⭐ Medium |
| 7 | `q07_cosine_similarity.py` | Cosine Similarity | ⭐ Easy |
| 8 | `q08_text_normalization.py` | Text Normalization & Cleaning | ⭐ Easy |
| 9 | `q09_character_ngrams.py` | Character N-grams (Bigrams) | ⭐ Easy |
| 10 | `q10_vocabulary_indexing.py` | Vocabulary Indexing (Bag of Words) | ⭐ Easy |

---

## 🔑 Key Formulas Cheat Sheet

### 1. Euclidean Distance
```
Distance = √[Σ(point1[i] - point2[i])²]
```

### 2. RNN Cell
```
h_t = tanh(W_x @ x_t + W_h @ h_{t-1} + b)
```

### 3. Attention Mechanism
```
scores = query · keys
weights = softmax(scores)
output = Σ(weight_i × value_i)
```

### 4. Causal Mask
```
M[i][j] = 0    if j ≤ i  (allowed)
M[i][j] = -1e9 if j > i  (masked)
```

### 5. Positional Encoding
```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

### 6. TF-IDF
```
TF(t,d) = count(t in d) / total_words(d)
IDF(t)  = log(N / df(t))
TF-IDF  = TF × IDF
```

### 7. Cosine Similarity
```
cos(θ) = (A · B) / (||A|| × ||B||)
```

### 8. Softmax
```
softmax(x_i) = exp(x_i) / Σexp(x_j)
```

---

## 🚀 Quick Start

```bash
# Navigate to the folder
cd "/Users/prathmeshbhardwaj/Desktop/PYTHON ENDTERM"

# Run all files to see explanations
for f in q*.py; do echo "=== $f ==="; python "$f"; done

# Or run individually
python q01_euclidean_distance.py
```

---

## 📦 Required Libraries

```bash
pip install numpy pandas
```

---

## 💡 Tips for the Coding Round

1. **Understand the formula** before coding
2. **Start with a simple loop approach** - optimize later if needed
3. **Handle edge cases**: empty inputs, zero vectors, etc.
4. **Test with the given examples** first
5. **Use NumPy** for matrix operations when allowed

---

Good luck with your coding round! 🎯
