"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module I give an implementation of the Naive and KMP string matching algorithms.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""


# ------------------------------------------------------------------------------------------------------------------- #
# This function implements the Naive algorithm.
# The searched pattern is compared with every substring of the text starting from the first character and stepping one
# char at a time. It receives in input the searched pattern and the text, both in the form of a string, and returns the
# list of all matching offsets found.
# ------------------------------------------------------------------------------------------------------------------- #

def naive_sm(pattern, text):
    offsets = list()
    n = len(text)
    m = len(pattern)
    for i in range(0, n - m):
        j = 0
        while j != m and text[i + j] == pattern[j]:
            if j == m - 1:
                offsets.append(i)
            j += 1
    return offsets


# ------------------------------------------------------------------------------------------------------------------- #
# These functions implement the Knuth-Morris-Pratt (KMP) algorithm.
# The searched pattern is pre-elaborated with the compute_pi_function() method. It takes the pattern as an input and
# returns a list (pi) which is equal in length to the pattern. Every index stores the length of the greatest prefix
# equal to the suffix of the pattern cut to the length specified by the index.
# In this way the algorithm may notice the absence of the pattern in the already matched chars in order to skip them,
# gaining time.
# ------------------------------------------------------------------------------------------------------------------- #

def compute_pi_function(word):
    m = len(word)
    pi = list()
    pi.append(0)
    k = 0
    for q in range(1, m):
        while k > 0 and word[k] != word[q]:
            k = pi[k - 1]
        if word[k] == word[q]:
            k = k + 1
        pi.append(k)
    return pi


def kmp_sm(pattern, text):
    offsets = list()
    n = len(text)
    m = len(pattern)
    pi = compute_pi_function(pattern)
    q = 0
    for i in range(0, n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            offsets.append(i - q + 1)
            q = pi[q - 1]
    return offsets
