"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This module offers some utility functions for string and text files creation.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import random
import re


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
    if file_path:
        with open(file_path, "w") as file:
            file.write(final_str)
    return final_str


# ------------------------------------------------------------------------------------------------------------------- #
# This function returns a string which matches the syntax of the "expr" passed as a parameter.
# The syntax should be given in a simil regular expression form (using BNF notation):
#
# <syntax> ::= <sequence>[^<number>][<syntax>]
# <sequence> ::= (<string>)
# <string> ::= char | char<string>
# <number> ::= positive_number
#
# by specifying every "positive_number" value as well as every "char" between parenthesis.
# It's also possible to specify a "file_path" in which case the behavior is the same as above.
# It doesn't support values choice i.e. (a + b) or (a)* .
# ------------------------------------------------------------------------------------------------------------------- #

def regex_str_generator(expr, file_path=None, reps=1):
    elements = list()
    elements = [x for x in re.split("[() +]", expr) if x]
    final_str = ''
    for r in range(0, reps+1):
        for i in range(0, len(elements)):
            if elements[i][0] == '^':
                pass
            elif i != len(elements)-1 and elements[i+1][0] == '^':
                final_str += elements[i] * int(elements[i + 1].replace('^', ''))
            else:
                final_str += elements[i]
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
reps = 10000
expr = f'(abc)^{n//3}(c)(ba)^{n//3}(c)^{n//4}(ab)^{m//2}(ca)^{m}'
text_words = 1000000


if __name__ == '__main__':
    regex_str_generator(f'(a)^{n}(b)', file_path='res/regex_ab.txt', reps=reps)
    # print(regex_str_generator(expr, "res/regex_abc.txt"))
    # regex_str_generator(f'(a)^{n}', 'res/regex_a.txt')
# rand_str_generator(bin_alpha, 8, 8, text_words, "res/rand_bin.txt")
