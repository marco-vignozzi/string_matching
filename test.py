"""
In this module we can run various tests in order to compare the string matching algorithms given
in the 'match.py' module.
"""
import match as m

# Here we select the file to open (file_in) and the word to match (pattern).
file_in = open("freedom.txt", "r", encoding='utf-8')
# file_in = open("bible.txt", "r", encoding='utf-8')
pattern = "free"

# Then it reads the file and it calls the methods which implement the algorithms.
# Here it stores the offsets result in the *_ofst variables.
text = file_in.read()
naive_ofst = m.naive_sm(pattern, text)
kmp_ofst = m.kmp_sm(pattern, text)

file_in.close()

# Then it writes the results in 2 separate files.
with open("docs/naive.txt", "w") as naive:
    naive.write('NAIVE ALGORITHM\n' +
                '---------------------------------\n' +
                f'searching for pattern "{pattern}"\n' +
                '---------------------------------\n')
    [naive.write(f'match with offset: {i}\n') for i in naive_ofst]
    naive.write('---------------------------------\n' +
                f'number of matches: {len(naive_ofst)}')

with open("docs/kmp.txt", "w") as kmp:
    kmp.write('KMP ALGORITHM\n' +
              '---------------------------------\n' +
              f'searching for pattern "{pattern}"\n' +
              '---------------------------------\n')
    [kmp.write(f'match with offset: {i}\n') for i in kmp_ofst]
    kmp.write('---------------------------------\n' +
              f'number of matches: {len(kmp_ofst)}')
