# 9. Character N-grams (Bigrams) 📝

## 🎯 Problem Summary
Generate character bigrams (N=2) for a word - sequences of 2 adjacent characters.

## 📚 Theory
N-grams capture **local patterns**:
- Unigrams (N=1): Single characters
- Bigrams (N=2): Character pairs
- Trigrams (N=3): Character triplets

## 🧠 Memory Trick
For word of length L: **L-1 bigrams**
```
"PYTHON" (L=6) → 5 bigrams
P-Y, Y-T, T-H, H-O, O-N
```

## 🔧 Complete Solution

```python
def get_character_bigrams(word):
    bigrams = []
    for i in range(len(word) - 1):
        bigram = word[i] + word[i + 1]
        bigrams.append(bigram)
    return bigrams

# One-liner version
def get_character_bigrams_v2(word):
    return [word[i:i+2] for i in range(len(word) - 1)]

# Example
print(get_character_bigrams("PYTHON"))
# ['PY', 'YT', 'TH', 'HO', 'ON']
```

## 💡 Generalized N-gram Function

```python
def get_ngrams(word, n):
    return [word[i:i+n] for i in range(len(word) - n + 1)]

# Usage
get_ngrams("PYTHON", 2)  # Bigrams
get_ngrams("PYTHON", 3)  # Trigrams: ['PYT', 'YTH', 'THO', 'HON']
```

## 🎓 NLP Uses
- Spelling correction
- Language detection
- Subword tokenization (BPE uses similar idea)

## ⚠️ Common Mistakes
- Off-by-one: `range(len(word) - 1)` not `range(len(word))`
- Empty string handling (returns [])
