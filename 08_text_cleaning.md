# 8. Text Normalization and Cleaning 🧹

## 🎯 Problem Summary
Clean text by: lowercase, remove punctuation, remove digits, tokenize into words.

## 📚 Theory
Text cleaning is the **first step** in any NLP pipeline. Raw text contains noise!

## 🧠 Memory Trick: "LPST"
1. **L**owercase
2. **P**unctuation remove
3. **S**trip digits
4. **T**okenize (split)

## 🔧 Complete Solution

```python
import string

def clean_text(text):
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 3. Remove digits
    text = ''.join(char for char in text if not char.isdigit())
    
    # 4. Split into tokens (words)
    tokens = text.split()
    
    return tokens

# Example
text = "Hello World! This is NLP 101: Let's code."
print(clean_text(text))
# ['hello', 'world', 'this', 'is', 'nlp', 'lets', 'code']
```

## 💡 Key Functions
- `str.lower()` - Lowercase
- `str.translate(str.maketrans('', '', string.punctuation))` - Remove punctuation
- `char.isdigit()` - Check if digit
- `str.split()` - Tokenize by whitespace

## ⚠️ Common Mistakes
- Forgetting `import string`
- Using `isalpha()` instead of `isdigit()` (would remove too much)
- Not handling contractions (let's → lets after removing ')
