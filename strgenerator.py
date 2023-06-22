"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This module offers some utility functions for string and text files creation.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import random


# ------------------------------------------------------------------------------------------------------------------- #
# This function returns a string which matches the queried parameters.
# It takes in input a list of symbols (alphabet) and the range of the lengths of the strings you want to generate,as
# well as the number. If you only want words of fixed length the "max_l" and "min_l" attributes must be equal.
# If the "file_path" is specified it also creates a file at that path storing the returned string.
# ------------------------------------------------------------------------------------------------------------------- #

def rand_str_generator(alphabet, min_l, max_l, text_l, file_path=None):
    final_str = ''
    for i in range(0, text_l):
        new_str = ''
        rand_str_size = random.randrange(0, 1001) % (max_l - min_l + 1) + min_l
        for j in range(0, rand_str_size):
            new_str += alphabet[random.randrange(0, 1001) % len(alphabet)]
        final_str += f'{new_str} '
    final_str = final_str[0: len(final_str)-1]
    if file_path:
        with open(file_path, "w") as file:
            file.write(final_str)
    return final_str


# ------------------------------------------------------------------------------------------------------------------- #
# Here I define some alphabets to use with the functions defined above. I also ran some test...
# ------------------------------------------------------------------------------------------------------------------- #

bin_alpha = list(['0', '1'])
ab_alpha = list(['a', 'b'])
hex_alpha = list(['A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
n = 100
m = 1000
reps = 1
expr = f'(abc)^{n//3}(c)(ba)^{n//3}(c)^{n//4}(ab)^{m//2}(ca)^{m}'
text_words = 100000

if __name__ == '__main__':
    rand_str_generator(hex_alpha, 100000, 100000, 1, "res/rand_hex.txt")
