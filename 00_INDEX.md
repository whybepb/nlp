# NLP Contest Practice - Quick Reference Guide 🚀

## 📋 Topics Overview

| # | Topic | Difficulty | Key Formula/Concept |
|---|-------|------------|---------------------|
| 1 | [Euclidean Distance](./01_euclidean_distance.md) | Easy | `√Σ(p-q)²` |
| 2 | [RNN Cell](./02_rnn_cell.md) | Medium | `h = tanh(Wx + Uh + b)` |
| 3 | [Attention](./03_attention_mechanism.md) | Medium | `softmax(QK^T) × V` |
| 4 | [Causal Masking](./04_causal_masking.md) | Easy | Lower triangle = 0, Upper = -1e9 |
| 5 | [Positional Encoding](./05_positional_encoding.md) | Medium | `sin/cos(pos/10000^(2i/d))` |
| 6 | [TF-IDF](./06_tf_idf.md) | Medium | `TF × IDF = TF × log(N/df)` |
| 7 | [Cosine Similarity](./07_cosine_similarity.md) | Easy | `(A·B)/(||A||×||B||)` |
| 8 | [Text Cleaning](./08_text_cleaning.md) | Easy | lowercase → remove punct → tokenize |
| 9 | [Character N-grams](./09_character_ngrams.md) | Easy | Adjacent character pairs |
| 10 | [Vocabulary Index](./10_vocabulary_indexing.md) | Easy | word → sorted index |

---

## 🧠 Super Quick Memory Tricks

### Math-Based
- **Euclidean**: "SSD" = Subtract, Square, Distance(sqrt)
- **Cosine**: "DOT over NORMS"
- **TF-IDF**: Frequent × Rare = Important

### Neural Network
- **RNN**: "WUB + tanh" (W×input + U×hidden + Bias)
- **Attention**: "QKV" = Question, Keywords, Values
- **Causal Mask**: Lower triangle only (no future peeking!)
- **Positional**: Sin(even), Cos(odd), frequency decreases

### Text Processing
- **Cleaning**: "LPST" = Lowercase, Punctuation, Strips digits, Tokenize
- **N-grams**: L chars → L-1 bigrams
- **Vocab**: "CSS" = Collect, Sort, Set indices

---

## 🔥 Common Gotchas

1. **Dimension mismatches** - Always check shapes
2. **Division by zero** - Check norms, denominators
3. **Rounding** - Do it at the END, not during calculation
4. **Off-by-one errors** - In loops, ranges
5. **Forgetting softmax** - For attention/normalization
6. **Natural log vs log10** - Usually `np.log` (natural)

---

## 📦 Common Imports

```python
import numpy as np
import pandas as pd
import math
import string
```

---

## 🎯 Exam Strategy

1. **Read carefully** - Check input/output format
2. **Write helper functions** - More modular, easier to debug
3. **Test with examples** - Use given sample inputs
4. **Round at the end** - Don't lose precision mid-calculation
5. **Check edge cases** - Empty inputs, zero vectors

Good luck! 🍀
