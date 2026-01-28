# 2. RNN (Recurrent Neural Network) Cell 🔄

## 🎯 Problem Summary
Implement a simple RNN cell that processes a sequence of inputs and produces outputs using fixed weights and biases.

---

## 📚 Theory & Concepts

### What is an RNN?
RNN (Recurrent Neural Network) is a neural network designed for **sequential data**. Unlike regular neural networks, RNNs have **memory** - they remember what they've seen before!

### The Magic of RNNs
```
      ┌──────────────────────────────┐
      │                              │
      ▼                              │
   ┌─────┐    ┌─────┐    ┌─────┐    │
x₁→│ RNN │→x₂→│ RNN │→x₃→│ RNN │────┘
   └──┬──┘    └──┬──┘    └──┬──┘
      │          │          │
      ▼          ▼          ▼
      h₁         h₂         h₃
      (outputs that carry memory)
```

### The Core Formula
```
h_next = tanh(W·x + U·h_prev + b)
```

Where:
- **h_next**: New hidden state (output)
- **x**: Current input
- **h_prev**: Previous hidden state (memory from past)
- **W**: Weight matrix for input
- **U**: Weight matrix for hidden state
- **b**: Bias vector
- **tanh**: Activation function (squashes to [-1, 1])

---

## 🧠 Memory Tricks

### 1. **"WUB" Formula**
- **W** × input
- **U** × hidden
- **B**ias added
- Then apply **tanh**

### 2. **The Memory Analogy**
Think of RNN as a person reading a book:
- **Current word (x)**: What you're reading NOW
- **Previous thoughts (h_prev)**: What you remember from before
- **New understanding (h_next)**: Your updated comprehension

### 3. **Recurrence = Recursion with Memory**
```
h₀ = 0 (or random)
h₁ = f(x₁, h₀)
h₂ = f(x₂, h₁)  ← Uses h₁!
h₃ = f(x₃, h₂)  ← Uses h₂!
```

---

## 💡 Key Insights

1. **Sequential Processing**: RNNs process one input at a time, carrying forward information
2. **Shared Weights**: Same W, U, b used for all time steps
3. **Hidden State = Memory**: h carries information from past inputs
4. **tanh Activation**: Keeps values between -1 and 1, preventing explosion

### Why tanh?
- Output range: [-1, 1]
- Zero-centered (unlike sigmoid)
- Helps with vanishing gradient (somewhat)

---

## 🔧 Complete Solution

```python
import numpy as np

def rnn_cell(inputs, W, U, b, h_prev):
    """
    Single RNN cell computation
    
    Args:
        inputs: Current input vector (d-dimensional)
        W: Weight matrix for input (hidden_size × input_size)
        U: Weight matrix for hidden state (hidden_size × hidden_size)
        b: Bias vector (hidden_size,)
        h_prev: Previous hidden state (hidden_size,)
    
    Returns:
        h_next: New hidden state
    """
    # Core RNN formula
    h_next = np.tanh(np.dot(W, inputs) + np.dot(U, h_prev) + b)
    return h_next

# Full RNN processing sequence
def process_sequence(inputs, hidden_size):
    """
    Process entire sequence through RNN
    """
    n, d = inputs.shape  # n = sequence length, d = input dimension
    
    # Initialize weights (fixed for deterministic output)
    np.random.seed(42)  # For reproducibility
    W = np.random.randn(hidden_size, d) * 0.1
    U = np.random.randn(hidden_size, hidden_size) * 0.1
    b = np.zeros(hidden_size)
    
    # Initial hidden state
    h_prev = np.zeros(hidden_size)
    
    outputs = []
    for i in range(n):
        h_prev = rnn_cell(inputs[i], W, U, b, h_prev)
        outputs.append(h_prev[0])  # First element as output
    
    return outputs

# Example
inputs = np.array([
    [0.5, 0.5],
    [0.1, 0.2],
    [0.3, 0.4]
])
outputs = process_sequence(inputs, hidden_size=2)
for out in outputs:
    print(round(out, 1))
```

---

## 🎓 NLP Context

### Where RNNs shine:
- **Text Generation**: Character-by-character or word-by-word
- **Sentiment Analysis**: Understanding context in sentences
- **Machine Translation**: (with encoder-decoder architecture)
- **Speech Recognition**: Processing audio sequences

### RNN Variants:
1. **Vanilla RNN**: Basic (our implementation)
2. **LSTM**: Long Short-Term Memory (solves vanishing gradient)
3. **GRU**: Gated Recurrent Unit (simpler than LSTM)

---

## 🔍 Matrix Dimensions Cheat Sheet

```
Input x:      (d,)           - d = input dimension
W:            (h, d)         - h = hidden size
U:            (h, h)
b:            (h,)
h_prev:       (h,)
h_next:       (h,)

Computation:
W·x   →  (h,d) × (d,) = (h,)
U·h   →  (h,h) × (h,) = (h,)
Sum + b → (h,) + (h,) + (h,) = (h,)
tanh  →  (h,) → (h,)
```

---

## ⚠️ Common Mistakes

1. **Dimension Mismatch**: Ensure matrix dimensions align for dot product
2. **Forgetting h_prev initialization**: Should be zeros initially
3. **Not applying tanh**: Without activation, gradients explode/vanish
4. **Confusing n×d vs d×n**: Check your matrix orientation!
