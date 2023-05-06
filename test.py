"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we can run various tests in order to compare the string matching algorithms given
in the 'match.py' module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import match as m
import random as r
import timeit as time


# This function generates a .txt file with random strings. It takes in input a list of symbols (alphabet)
# and the range of the lengths of the strings you want to generate, as well as the number. It returns a
# file with the number of strings requested.

def rand_str_file(alphabet, min_l, max_l, text_l, file_path):
    with open(file_path, "w") as file:
        for i in range(0, text_l):
            new_str = ''
            rand_str_size = r.randrange(0, 1001) % (max_l - min_l + 1) + min_l
            for j in range(0, rand_str_size):
                new_str += alphabet[r.randrange(0,1001) % len(alphabet)]
            file.write(f'{new_str} ')
    return


# Here we select the file to open (file_in) and the word to match (pattern). We can also create a file with
# the previous function.
# text_length = 1000000
# hex_alpha = list(['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
# rand_str_file(hex_alpha, 8, 8, text_length, "res/rand_hex.txt")
file_in = open("res/rand_hex.txt", "r", encoding='utf-8')
# file_in = open("res/freedom.txt", "r", encoding='utf-8')
# file_in = open("res/bible.txt", "r", encoding='utf-8')
pattern = "1111"


# It reads the file and it calls the methods which implement the algorithms storing the offsets result
# in the *_ofst variables.

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
