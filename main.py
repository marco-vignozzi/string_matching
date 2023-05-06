
"""
This function implements the naive string matching algorithm.
The searched pattern is compared with every substring of the text starting from the first character
and stepping one char at a time. It receives in input the searched pattern and the text, both
in the form of a string, and returns the list of all matching offsets found.
"""


def naive_sm(pattern, text):
    print('---------------------------------')
    print(f'searching for pattern "{pattern}"')
    print('---------------------------------')
    offsets = list()
    n = len(text)
    m = len(pattern)
    for i in range(0, n - m):
        j = 0
        while j != m and text[i+j] == pattern[j]:
            if j == m-1:
                offsets.append(i)
                print(f'match with offset: {i}')
            j += 1
    print('---------------------------------')
    print('END OF FILE')
    print('---------------------------------')
    print(f'number of matches: {len(offsets)}')
    return offsets


# TODO: add description


def compute_pi_function(word):
    m = len(word)
    pi = list()
    pi.append(0)
    k = 0
    for q in range(1, m):
        while k > 0 and word[k] != word[q]:
            k = pi[k-1]
        if word[k] == word[q]:
            k = k + 1
        pi.append(k)
    return pi


def kmp_sm(pattern, text):
    print('---------------------------------')
    print(f'searching for pattern "{pattern}"')
    print('---------------------------------')
    offsets = list()
    n = len(text)
    m = len(pattern)
    pi = compute_pi_function(pattern)
    q = 0
    for i in range(0, n):
        while q > 0 and pattern[q] == text[i]:
            q = pi[q-1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:                                  # FIXME: something's not working here...
            print(f'match with offset: {i}')
            q = pi[q]
            offsets.append(i)
    print('---------------------------------')
    print('END OF FILE')
    print('---------------------------------')
    print(f'number of matches: {len(offsets)}')
    return offsets


f = open("text.txt", "r", encoding='utf-8')
# print(f.read())
# naive_sm("And", f.read())
kmp_sm("freedom", f.read())

# print(compute_pi_function("santo sia san Gennaro santo sia san Paolo"))
