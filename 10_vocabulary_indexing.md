# 10. Vocabulary Indexing (Bag of Words) 📚

## 🎯 Problem Summary
Create a vocabulary dictionary mapping each unique word to a unique integer index (sorted alphabetically, starting from 0).

## 📚 Theory
**Bag of Words (BoW)**: Represent text as word counts, ignoring order.
First step: Build a **vocabulary** (word → index mapping).

## 🧠 Memory Trick: "CSS"
1. **C**ollect all words
2. **S**ort alphabetically
3. **S**et indices (0, 1, 2...)

## 🔧 Complete Solution

```python
def create_vocab(sentences):
    # Collect all unique words
    all_words = set()
    for sentence in sentences:
        words = sentence.lower().split()
        all_words.update(words)
    
    # Sort alphabetically and assign indices
    sorted_words = sorted(all_words)
    vocab = {word: idx for idx, word in enumerate(sorted_words)}
    
    return vocab

# Example
sentences = ["i love nlp", "nlp is fun"]
vocab = create_vocab(sentences)
print(vocab)
# {'fun': 0, 'i': 1, 'is': 2, 'love': 3, 'nlp': 4}
```

## 💡 Extended: Text to Vector

```python
def text_to_bow(sentence, vocab):
    vector = [0] * len(vocab)
    for word in sentence.lower().split():
        if word in vocab:
            vector[vocab[word]] += 1
    return vector

# "nlp is fun" → [1, 0, 1, 0, 1]
#                fun=1, i=0, is=1, love=0, nlp=1
```

## 🎓 NLP Context
- Foundation for TF-IDF, BoW models
- Needed before any vectorization
- Limitation: Fixed vocabulary (OOV problem)

## ⚠️ Common Mistakes
- Forgetting to lowercase
- Not sorting alphabetically
- Starting indices from 1 instead of 0
