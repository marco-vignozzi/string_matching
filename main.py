"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we can run various tests from the test.py module in order to compare the string matching algorithms
given in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import test
import random


# ------------------------------------------------------------------------------------------------------------------- #
# This function name stands for "random strings file generator", as it creates a .txt file with random strings.
# It takes in input a list of symbols (alphabet) and the range of the lengths of the strings you want to generate,as
# well as the number. It returns a file with the number of strings requested.
# ------------------------------------------------------------------------------------------------------------------- #

def rs_file_generator(alphabet, min_l, max_l, text_l, file_path):
    with open(file_path, "w") as file:
        for i in range(0, text_l):
            new_str = ''
            rand_str_size = random.randrange(0, 1001) % (max_l - min_l + 1) + min_l
            for j in range(0, rand_str_size):
                new_str += alphabet[random.randrange(0, 1001) % len(alphabet)]
            file.write(f'{new_str} ')
    return


# ------------------------------------------------------------------------------------------------------------------- #
# Here it generates a .txt file with "text_length" random hexadecimal values of length 8.
# ------------------------------------------------------------------------------------------------------------------- #

text_length = 1000000
hex_alpha = list(['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
rs_file_generator(hex_alpha, 8, 8, text_length, "res/rand_hex.txt")

# ----------------------------------------------------------------------------------------------------------- #
# Then it writes the results in 2 distinct files.
# # ----------------------------------------------------------------------------------------------------------- #
#
# with open("docs/naive.txt", "w") as naive:
#     naive.write('NAIVE ALGORITHM\n' +
#                 '---------------------------------\n' +
#                 f'searching for pattern "{pattern}"\n' +
#                 '---------------------------------\n')
#     [naive.write(f'match with offset: {i}\n') for i in naive_offsets]
#     naive.write('---------------------------------\n' +
#                 f'total matches: {len(naive_offsets)}')
#
# with open("docs/kmp.txt", "w") as kmp:
#     kmp.write('KMP ALGORITHM\n' +
#               '---------------------------------\n' +
#               f'searching for pattern "{pattern}"\n' +
#               '---------------------------------\n')
#     [kmp.write(f'match with offset: {i}\n') for i in kmp_offsets]
#     kmp.write('---------------------------------\n' +
#               f'total matches: {len(kmp_offsets)}')
#
