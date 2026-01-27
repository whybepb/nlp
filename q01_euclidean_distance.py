"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 1: EUCLIDEAN DISTANCE                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Complete the euclidean_distance function to return the Euclidean distance    ║
║ between point1 and point2. Return the answer rounded to 2 decimal places.    ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ Euclidean distance is the "straight line" distance between two points.       ║
║ For points (x1, y1, z1) and (x2, y2, z2):                                    ║
║ Distance = √[(x2-x1)² + (y2-y1)² + (z2-z1)²]                                 ║
║                                                                               ║
║ In general for n-dimensional points:                                         ║
║ Distance = √[Σ(point1[i] - point2[i])²]                                      ║
║                                                                               ║
║ INPUT:                                                                        ║
║   point1: list of numbers (e.g., [1, 2, 3])                                  ║
║   point2: list of numbers (e.g., [3, 4, 5])                                  ║
║                                                                               ║
║ OUTPUT:                                                                       ║
║   float: The Euclidean distance rounded to 2 decimal places                  ║
║                                                                               ║
║ SAMPLE:                                                                       ║
║   Input:  point1 = [1, 2, 3], point2 = [3, 4, 5]                             ║
║   Output: 3.46                                                                ║
║                                                                               ║
║   Calculation:                                                                ║
║   √[(3-1)² + (4-2)² + (5-3)²] = √[4 + 4 + 4] = √12 = 3.464... ≈ 3.46        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import math

def euclidean_distance(point1: list, point2: list) -> float:
    """
    Calculate Euclidean distance between two points.
    
    Steps:
    1. For each dimension, find the difference between coordinates
    2. Square each difference
    3. Sum all squared differences
    4. Take the square root
    5. Round to 2 decimal places
    """
    # Method 1: Using a loop
    sum_of_squares = 0
    for i in range(len(point1)):
        diff = point1[i] - point2[i]
        sum_of_squares += diff ** 2
    
    distance = math.sqrt(sum_of_squares)
    return round(distance, 2)


def euclidean_distance_v2(point1: list, point2: list) -> float:
    """Alternative method using list comprehension"""
    sum_of_squares = sum((a - b) ** 2 for a, b in zip(point1, point2))
    return round(math.sqrt(sum_of_squares), 2)


def euclidean_distance_numpy(point1: list, point2: list) -> float:
    """Alternative method using NumPy (if allowed)"""
    import numpy as np
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.linalg.norm(point1 - point2)
    return round(distance, 2)


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("EUCLIDEAN DISTANCE - TEST CASES")
    print("=" * 60)
    
    # Test Case 1: Given example
    p1 = [1, 2, 3]
    p2 = [3, 4, 5]
    result = euclidean_distance(p1, p2)
    print(f"\nTest 1: point1={p1}, point2={p2}")
    print(f"Expected: 3.46, Got: {result}")
    print(f"✓ PASS" if result == 3.46 else "✗ FAIL")
    
    # Test Case 2: 2D points
    p1 = [0, 0]
    p2 = [3, 4]
    result = euclidean_distance(p1, p2)
    print(f"\nTest 2: point1={p1}, point2={p2}")
    print(f"Expected: 5.0, Got: {result}")
    print(f"✓ PASS" if result == 5.0 else "✗ FAIL")
    
    # Test Case 3: Same points
    p1 = [5, 5, 5]
    p2 = [5, 5, 5]
    result = euclidean_distance(p1, p2)
    print(f"\nTest 3: point1={p1}, point2={p2}")
    print(f"Expected: 0.0, Got: {result}")
    print(f"✓ PASS" if result == 0.0 else "✗ FAIL")
    
    # Test Case 4: 1D points
    p1 = [10]
    p2 = [15]
    result = euclidean_distance(p1, p2)
    print(f"\nTest 4: point1={p1}, point2={p2}")
    print(f"Expected: 5.0, Got: {result}")
    print(f"✓ PASS" if result == 5.0 else "✗ FAIL")
    
    print("\n" + "=" * 60)
