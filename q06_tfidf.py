"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    QUESTION 6: TF-IDF IMPLEMENTATION                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ TASK:                                                                         ║
║ Implement your own version of TF-IDF for a small corpus of text reviews.     ║
║                                                                               ║
║ Requirements:                                                                 ║
║ 1. Tokenize each review (split by spaces)                                    ║
║ 2. Compute Term Frequency (TF) for each document                             ║
║ 3. Compute Inverse Document Frequency (IDF) for all unique words             ║
║ 4. Combine them to form a TF-IDF matrix as a Pandas DataFrame                ║
║                                                                               ║
║ CONCEPT:                                                                      ║
║ TF-IDF helps identify important words in a document relative to a corpus.    ║
║                                                                               ║
║ FORMULAS:                                                                     ║
║                                                                               ║
║ TF (Term Frequency) - How often a word appears in a document                 ║
║   TF(t, d) = (Number of times term t appears in document d)                  ║
║              ────────────────────────────────────────────────                ║
║              (Total number of terms in document d)                            ║
║                                                                               ║
║ IDF (Inverse Document Frequency) - How rare a word is across all documents  ║
║   IDF(t) = log(N / df(t))                                                    ║
║   Where:                                                                      ║
║     N = Total number of documents                                             ║
║     df(t) = Number of documents containing term t                            ║
║                                                                               ║
║ TF-IDF combines both:                                                         ║
║   TF-IDF(t, d) = TF(t, d) × IDF(t)                                           ║
║                                                                               ║
║ High TF-IDF = Word is frequent in this doc but rare in other docs (important)║
║ Low TF-IDF = Word is common everywhere (less distinctive)                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import pandas as pd
import numpy as np
import math

def compute_tf(document: str) -> dict:
    """
    Compute Term Frequency for a single document.
    
    TF(t, d) = count(t in d) / total_words(d)
    
    Args:
        document: A string (the document text)
    
    Returns:
        Dictionary mapping each word to its TF value
    """
    # Tokenize: split by spaces
    words = document.split()
    total_words = len(words)
    
    # Count frequency of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Calculate TF
    tf = {}
    for word, count in word_counts.items():
        tf[word] = count / total_words
    
    return tf


def compute_idf(documents: list) -> dict:
    """
    Compute Inverse Document Frequency for all unique words.
    
    IDF(t) = log(N / df(t))
    
    Args:
        documents: List of document strings
    
    Returns:
        Dictionary mapping each unique word to its IDF value
    """
    N = len(documents)  # Total number of documents
    
    # Get all unique words
    all_words = set()
    for doc in documents:
        words = doc.split()
        all_words.update(words)
    
    # Calculate df (document frequency) for each word
    df = {}
    for word in all_words:
        df[word] = sum(1 for doc in documents if word in doc.split())
    
    # Calculate IDF
    idf = {}
    for word in all_words:
        idf[word] = math.log(N / df[word])
    
    return idf


def compute_tfidf(documents: list) -> pd.DataFrame:
    """
    Compute TF-IDF matrix for a list of documents.
    
    Args:
        documents: List of document strings
    
    Returns:
        Pandas DataFrame with documents as rows and words as columns
    """
    # Step 1: Compute IDF for all words
    idf = compute_idf(documents)
    
    # Step 2: Get all unique words (sorted for consistent column order)
    all_words = sorted(idf.keys())
    
    # Step 3: Compute TF-IDF for each document
    tfidf_matrix = []
    
    for doc in documents:
        tf = compute_tf(doc)
        
        # Calculate TF-IDF for each word
        tfidf_row = []
        for word in all_words:
            if word in tf:
                tfidf_value = tf[word] * idf[word]
            else:
                tfidf_value = 0.0
            tfidf_row.append(tfidf_value)
        
        tfidf_matrix.append(tfidf_row)
    
    # Create DataFrame
    df = pd.DataFrame(tfidf_matrix, columns=all_words)
    df.index = [f"doc_{i}" for i in range(len(documents))]
    
    return df


def tfidf_from_dataframe(reviews_df: pd.DataFrame, column: str = "review") -> pd.DataFrame:
    """
    Compute TF-IDF from a Pandas DataFrame with a 'review' column.
    
    Args:
        reviews_df: DataFrame with text reviews
        column: Name of the column containing reviews
    
    Returns:
        TF-IDF DataFrame
    """
    documents = reviews_df[column].tolist()
    return compute_tfidf(documents)


# ═══════════════════════════════════════════════════════════════════════════════
# STEP-BY-STEP EXPLANATION
# ═══════════════════════════════════════════════════════════════════════════════
def explain_tfidf():
    """Visual explanation of TF-IDF computation."""
    print("=" * 60)
    print("TF-IDF - STEP BY STEP")
    print("=" * 60)
    
    # Sample documents
    documents = [
        "the cat sat on the mat",
        "the dog sat on the log",
        "cats and dogs are pets"
    ]
    
    print("\nSAMPLE DOCUMENTS:")
    for i, doc in enumerate(documents):
        print(f"  Doc {i}: '{doc}'")
    
    print("\n" + "-" * 40)
    print("STEP 1: TERM FREQUENCY (TF)")
    print("-" * 40)
    
    for i, doc in enumerate(documents):
        print(f"\nDoc {i}: '{doc}'")
        words = doc.split()
        total = len(words)
        print(f"  Total words: {total}")
        
        tf = compute_tf(doc)
        for word, value in sorted(tf.items()):
            count = words.count(word)
            print(f"  TF('{word}') = {count}/{total} = {value:.4f}")
    
    print("\n" + "-" * 40)
    print("STEP 2: INVERSE DOCUMENT FREQUENCY (IDF)")
    print("-" * 40)
    print(f"\nN (total documents) = {len(documents)}")
    
    idf = compute_idf(documents)
    
    # Calculate df for display
    for word in sorted(idf.keys()):
        df_count = sum(1 for doc in documents if word in doc.split())
        print(f"  '{word}':")
        print(f"    df = {df_count} documents contain this word")
        print(f"    IDF = log({len(documents)}/{df_count}) = {idf[word]:.4f}")
    
    print("\n" + "-" * 40)
    print("STEP 3: TF-IDF = TF × IDF")
    print("-" * 40)
    
    print("\nFor Doc 0:")
    tf = compute_tf(documents[0])
    for word in sorted(tf.keys()):
        tfidf = tf[word] * idf[word]
        print(f"  TFIDF('{word}') = {tf[word]:.4f} × {idf[word]:.4f} = {tfidf:.4f}")
    
    print("\n" + "-" * 40)
    print("FINAL TF-IDF MATRIX:")
    print("-" * 40)
    
    tfidf_df = compute_tfidf(documents)
    print(tfidf_df.round(4).to_string())
    
    print("\nINTERPRETATION:")
    print("─" * 40)
    print("• 'the' has low TF-IDF (appears in many docs)")
    print("• 'cat' has higher TF-IDF (rare, only in doc 0)")
    print("• Words unique to a doc have higher TF-IDF scores")


# ═══════════════════════════════════════════════════════════════════════════════
# TEST YOUR UNDERSTANDING
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # First explain the concept
    explain_tfidf()
    
    print("\n" + "=" * 60)
    print("TF-IDF - TEST CASES")
    print("=" * 60)
    
    # Test Case 1: From DataFrame
    data = {
        "review": [
            "great product love it",
            "terrible product hate it",
            "good product recommend it"
        ]
    }
    df = pd.DataFrame(data)
    
    print("\nTest 1: From Pandas DataFrame")
    print("Input DataFrame:")
    print(df)
    
    tfidf_result = tfidf_from_dataframe(df, "review")
    print("\nTF-IDF Matrix:")
    print(tfidf_result.round(4).to_string())
    
    # Test Case 2: Simple documents
    docs = ["a a b", "a b b"]
    print("\nTest 2: Simple documents")
    print(f"Documents: {docs}")
    
    tfidf_result = compute_tfidf(docs)
    print("TF-IDF Matrix:")
    print(tfidf_result.round(4).to_string())
    
    print("\n" + "=" * 60)
