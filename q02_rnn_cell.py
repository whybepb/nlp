"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 2: RNN (Recurrent Neural Network) CELL           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Implement a simple RNN cell to process a sequence of inputs and produce      ║
║ a sequence of outputs. Use fixed weights and biases for deterministic output.║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ An RNN processes sequences one step at a time, maintaining a "hidden state"  ║
║ that carries information from previous steps.                                 ║
║                                                                               ║
║ The formula for a simple RNN cell:                                            ║
║   h_t = tanh(W_h * h_{t-1} + W_x * x_t + b)                                  ║
║   output_t = h_t (or some transformation of h_t)                             ║
║                                                                               ║
║ Where:                                                                        ║
║   - h_t = hidden state at time t                                             ║
║   - h_{t-1} = hidden state at time t-1                                       ║
║   - x_t = input at time t                                                    ║
║   - W_h = weight matrix for hidden state                                     ║
║   - W_x = weight matrix for input                                            ║
║   - b = bias                                                                  ║
║   - tanh = activation function                                                ║
║                                                                               ║
║ INPUT FORMAT:                                                                 ║
║   First line: Two integers n and d (1≤n,d≤100)                               ║
║     - n = length of the sequence                                              ║
║     - d = dimension of each input vector                                      ║
║   Next n lines: d space-separated floats (the input sequence)                ║
║                                                                               ║
║ OUTPUT FORMAT:                                                                ║
║   n lines, each containing a single float (output for each input)            ║
║                                                                               ║
║ SAMPLE:                                                                       ║
║   Input:                                                                      ║
║     3 2                                                                       ║
║     1.0 0.5                                                                   ║
║     0.3 0.7                                                                   ║
║     0.8 0.2                                                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import numpy as np

def simple_rnn_cell(inputs: list, hidden_size: int = 1) -> list:
    """
    Implement a simple RNN cell.
    
    Args:
        inputs: List of input vectors (each is a list of floats)
        hidden_size: Size of hidden state (default 1 for single output)
    
    Returns:
        List of outputs, one for each input in the sequence
    """
    n = len(inputs)  # sequence length
    d = len(inputs[0])  # input dimension
    
    # Fixed weights for deterministic output
    # W_x: Weight matrix for input (hidden_size x d)
    W_x = np.ones((hidden_size, d)) * 0.5
    
    # W_h: Weight matrix for hidden state (hidden_size x hidden_size)
    W_h = np.ones((hidden_size, hidden_size)) * 0.5
    
    # b: Bias (hidden_size,)
    b = np.zeros(hidden_size)
    
    # Initialize hidden state to zeros
    h = np.zeros(hidden_size)
    
    outputs = []
    
    for t in range(n):
        x_t = np.array(inputs[t])  # Current input
        
        # RNN formula: h_t = tanh(W_x @ x_t + W_h @ h_{t-1} + b)
        h = np.tanh(np.dot(W_x, x_t) + np.dot(W_h, h) + b)
        
        # Output is the hidden state (or first element if hidden_size > 1)
        outputs.append(float(h[0]))
    
    return outputs


def rnn_from_input():
    """
    Read input in the specified format and run RNN.
    """
    # Read n and d
    n, d = map(int, input().split())
    
    # Read n input vectors
    inputs = []
    for _ in range(n):
        row = list(map(float, input().split()))
        inputs.append(row)
    
    # Run RNN
    outputs = simple_rnn_cell(inputs)
    
    # Print outputs
    for output in outputs:
        print(f"{output:.6f}")


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_rnn():
    """
    Step-by-step walkthrough of RNN processing.
    """
    print("=" * 60)
    print("RNN CELL - STEP BY STEP EXPLANATION")
    print("=" * 60)
    
    # Sample input
    inputs = [[1.0, 0.5], [0.3, 0.7], [0.8, 0.2]]
    print(f"\nInput sequence (n=3, d=2): {inputs}")
    
    # Weights (fixed for deterministic output)
    W_x = np.array([[0.5, 0.5]])  # (1, 2)
    W_h = np.array([[0.5]])       # (1, 1)
    b = np.array([0.0])           # (1,)
    
    print(f"\nWeights:")
    print(f"  W_x = {W_x} (for input)")
    print(f"  W_h = {W_h} (for hidden state)")
    print(f"  b = {b} (bias)")
    
    h = np.array([0.0])  # Initial hidden state
    print(f"\nInitial hidden state: h_0 = {h}")
    
    print("\n" + "-" * 40)
    print("PROCESSING EACH TIME STEP:")
    print("-" * 40)
    
    for t, x_t in enumerate(inputs):
        x_t = np.array(x_t)
        print(f"\nTime step {t+1}:")
        print(f"  Input x_{t+1} = {x_t}")
        print(f"  Previous hidden h_{t} = {h}")
        
        # Calculate components
        wx = np.dot(W_x, x_t)
        wh = np.dot(W_h, h)
        print(f"  W_x @ x = {W_x} @ {x_t} = {wx}")
        print(f"  W_h @ h = {W_h} @ {h} = {wh}")
        
        # New hidden state
        h_new = np.tanh(wx + wh + b)
        print(f"  h_{t+1} = tanh({wx} + {wh} + {b}) = tanh({wx + wh + b}) = {h_new}")
        
        h = h_new
        print(f"  Output: {float(h[0]):.6f}")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_rnn()
    
    print("\n" + "=" * 60)
    print("RNN CELL - TEST CASES")
    print("=" * 60)
    
    # Test Case 1
    inputs = [[1.0, 0.5], [0.3, 0.7], [0.8, 0.2]]
    outputs = simple_rnn_cell(inputs)
    print(f"\nTest 1: inputs={inputs}")
    print(f"Outputs: {[round(o, 4) for o in outputs]}")
    
    # Test Case 2: Single input
    inputs = [[1.0, 1.0]]
    outputs = simple_rnn_cell(inputs)
    print(f"\nTest 2: inputs={inputs}")
    print(f"Outputs: {[round(o, 4) for o in outputs]}")
    
    print("\n" + "=" * 60)
