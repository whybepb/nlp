# 6. TF-IDF (Term Frequency - Inverse Document Frequency) 📊

## 🎯 Problem Summary
Implement TF-IDF from scratch to convert text documents into numerical vectors that represent word importance.

---

## 📚 Theory & Concepts

### What is TF-IDF?
TF-IDF measures how **important a word is** to a document in a collection. It balances:
- **TF (Term Frequency)**: How often a word appears in a document
- **IDF (Inverse Document Frequency)**: How rare/unique a word is across all documents

### The Intuition 💡
- Words that appear **frequently in ONE document** but **rarely in others** are MORE important
- Common words like "the", "is" get low scores (appear everywhere)
- Unique/specific words get high scores

### Formulas

#### Term Frequency (TF)
```
TF(t, d) = (count of term t in document d) / (total terms in document d)
```

#### Inverse Document Frequency (IDF)
```
IDF(t) = log(total documents / documents containing term t)
       = log(N / df_t)
```

#### TF-IDF
```
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

---

## 🧠 Memory Tricks

### 1. **"Frequency vs Rarity"**
- **TF** = How FREQUENT in THIS doc
- **IDF** = How RARE across ALL docs
- High TF × High IDF = Important word!

### 2. **The Newspaper Analogy** 📰
- "the" appears in EVERY article → Low IDF → Not useful
- "cryptocurrency" appears in few articles → High IDF → Distinctive!

### 3. **IDF is the "Inverse" of popularity**
```
Popular word = Low IDF (punished)
Rare word = High IDF (rewarded)
```

### 4. **Why log?**
- Without log: Rare words would dominate too much
- Log smooths the values
- log(1) = 0, so words in all docs have IDF = 0

---

## 💡 Key Insights

### Step-by-Step Process:
```
Documents → Tokenize → Build Vocab → Compute TF → Compute IDF → TF × IDF
```

### Example Walkthrough:

```
doc1: "good product"
doc2: "bad product quality"

Vocab (sorted): ['bad', 'good', 'product', 'quality']

TF Matrix:
              bad    good   product  quality
doc1    [    0     0.5     0.5       0     ]  ← 2 words total
doc2    [   0.33    0     0.33     0.33   ]  ← 3 words total

IDF:
- 'bad':     log(2/1) = log(2) ≈ 0.693
- 'good':    log(2/1) = log(2) ≈ 0.693
- 'product': log(2/2) = log(1) = 0      ← In all docs!
- 'quality': log(2/1) = log(2) ≈ 0.693

TF-IDF = TF × IDF:
              bad       good     product   quality
doc1    [    0       0.346574   0          0      ]
doc2    [ 0.231049    0        0        0.231049 ]
```

---

## 🔧 Complete Solution

```python
import pandas as pd
import numpy as np

def tokenize_reviews(reviews):
    """Split each review into list of words."""
    return [review.split() for review in reviews]

def build_vocab(token_lists):
    """Build sorted vocabulary from all tokens."""
    all_words = set()
    for tokens in token_lists:
        all_words.update(tokens)
    return sorted(list(all_words))

def compute_tf(token_lists, vocab):
    """
    Compute Term Frequency for each document.
    TF = count(word in doc) / total words in doc
    """
    n_docs = len(token_lists)
    n_vocab = len(vocab)
    
    tf_matrix = np.zeros((n_docs, n_vocab))
    
    for doc_idx, tokens in enumerate(token_lists):
        total_words = len(tokens)
        for token in tokens:
            if token in vocab:
                word_idx = vocab.index(token)
                tf_matrix[doc_idx, word_idx] += 1
        # Normalize by total words
        if total_words > 0:
            tf_matrix[doc_idx] /= total_words
    
    return pd.DataFrame(tf_matrix, columns=vocab)

def compute_idf(token_lists, vocab):
    """
    Compute Inverse Document Frequency.
    IDF = log(total docs / docs containing word)
    """
    n_docs = len(token_lists)
    idf_values = []
    
    for word in vocab:
        # Count documents containing this word
        doc_count = sum(1 for tokens in token_lists if word in tokens)
        # Compute IDF
        idf = np.log(n_docs / doc_count) if doc_count > 0 else 0
        idf_values.append(idf)
    
    return np.array(idf_values)

def compute_tfidf(tf_df, idf):
    """
    Compute TF-IDF = TF × IDF
    """
    tfidf_matrix = tf_df.values * idf  # Broadcasting
    return pd.DataFrame(tfidf_matrix, columns=tf_df.columns)


# Main processing
def process_reviews(df):
    reviews = df['review'].tolist()
    
    # Step 1: Tokenize
    token_lists = tokenize_reviews(reviews)
    
    # Step 2: Build vocabulary
    vocab = build_vocab(token_lists)
    
    # Step 3: Compute TF
    tf_df = compute_tf(token_lists, vocab)
    
    # Step 4: Compute IDF
    idf = compute_idf(token_lists, vocab)
    
    # Step 5: Compute TF-IDF
    tfidf_df = compute_tfidf(tf_df, idf)
    
    return tfidf_df


# Example usage
df = pd.DataFrame({
    'review': ['good product', 'bad product quality']
})

result = process_reviews(df)
print(result)
```

### Output:
```
        bad      good   product   quality
0  0.000000  0.346574  0.000000  0.000000
1  0.231049  0.000000  0.000000  0.231049
```

---

## 🎓 NLP Context

### Where TF-IDF is Used:
1. **Document Search/Retrieval**: Find relevant documents
2. **Text Classification**: Feature extraction
3. **Keyword Extraction**: Find important terms
4. **Content-Based Recommendation**: Similar articles

### Limitations:
- Ignores word order and context
- Doesn't capture synonyms
- Fixed vocabulary (can't handle new words)

### Modern Alternatives:
- Word2Vec, GloVe (word embeddings)
- BERT, Transformers (contextual embeddings)

---

## 🔍 Quick Reference

```python
# TF: Normalize by document length
TF = word_count / total_words_in_doc

# IDF: Log of inverse document frequency
IDF = log(N / docs_with_word)

# Combined
TF_IDF = TF × IDF

# Interpretation:
# High TF + High IDF = Important (unique to this doc)
# High TF + Low IDF = Common word (not distinctive)
# Low TF + High IDF = Rare word (but not in this doc)
# Low TF + Low IDF = Common + infrequent (not useful)
```

---

## ⚠️ Common Mistakes

1. **Forgetting to sort vocabulary**: Problem requires alphabetical order
2. **Using log base 10 vs natural log**: Usually natural log (np.log)
3. **Division by zero**: Check for empty documents
4. **Wrong IDF formula**: log(N/df), not log(N/(1+df)) or log(1+N/df)
5. **Not normalizing TF**: Must divide by document length
