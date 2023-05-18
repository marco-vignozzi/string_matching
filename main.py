"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we run various tests from the test.py module in order to compare the string matching algorithms given
in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import numpy as np

import strgenerator as sg
import matplotlib.pyplot as plt
import test


# ------------------------------------------------------------------------------------------------------------------- #
# TODO: add description and code to this segment
# ------------------------------------------------------------------------------------------------------------------- #

def create_docs():
    pass


def create_plots(test, title, yscale):
    naive_t = np.array([test.naive['times'][i] for i in test.naive['times']])
    kmp_t = np.array([test.kmp['times'][i] for i in test.kmp['times']])
    n_values = np.array([i for i in test.naive['times']])
    plt.plot(n_values, naive_t, 'r-', n_values, kmp_t, 'b-')
    plt.legend(['Naive', 'KMP'])
    plt.axis([min(n_values), 1.02*max(n_values), 0, yscale*max(naive_t[-1], kmp_t[-1])])

    plt.title(title)
    plt.show()
    return


# ------------------------------------------------------------------------------------------------------------------- #
# Here we can initialize some variables which will define the tests.
# ------------------------------------------------------------------------------------------------------------------- #

test_rep = 5
start = 100
stop = 500
step = 20
text_div = 20
test_suite = dict()
src1 = 'res/regex_a.txt'
src2 = 'res/bible.txt'
src3 = 'res/regex_ab.txt'

with open(src1, 'r', encoding='utf-8') as file:
    text1 = file.read()

with open(src2, 'r', encoding='utf-8') as file:
    text2 = file.read()

with open(src3, 'r', encoding='utf-8') as file:
    text3 = file.read()


# t = test.Test('res/freedom.txt', 'freedom')
#
# print(t.naive_offsets)
# print(len(t.naive_offsets))

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 1
# We consider a sequence of "a" with increasing length in range "start - stop" with the given "step" as the queried
# pattern. The text is a sequence of 1 million of "a".
# This test will consider the scenario where we search for a pattern which is always matched.
# Test's data will be stored in a "Test" object, as for the others.
# ------------------------------------------------------------------------------------------------------------------- #
# TODO: add description to this test cases

t1 = test.Test()
for n in range(start, stop+1, step):
    pattern = sg.regex_str_generator(f'(a)^{n}')
    t1.run_test(pattern, text1, n=n, test_rep=test_rep, r=5)

print("TEST 1 RESULTS")
print(f'naive times: ' + f"{t1.naive['times']}\n")
print(f'kmp times: ' + f"{t1.kmp['times']}\n")

# create_plots(t1, 'Test 1', yscale=1.2)

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 2
# Here we compare the algorithms with a text of increasing length, always searching for the same, short, and averagely
# frequent pattern.
# ------------------------------------------------------------------------------------------------------------------- #

t2 = test.Test()
for n in range(text_div, 0, -1):
    text = text2[0: len(text2) // n]
    t2.run_test('And', text, n=abs(text_div-n-1), test_rep=test_rep, r=5)

print("TEST 2 RESULTS")
print(f'naive times: ' + f"{t2.naive['times']}\n")
print(f'kmp times: ' + f"{t2.kmp['times']}\n")

# create_plots(t2, 'Test 2', yscale=1.2)
# ------------------------------------------------------------------------------------------------------------------- #
# TEST 3
# Here the algorithms are compared with a text of 1 million chars. It is a repetition of a sequence composed by 100 "a"
# followed by 1 "b".
# The searched pattern is a sequence of "a" with increasing length in the usual (start - stop) range.
# In this scenario we search for a pattern with a long prefix which matches the text, but it never matches completely.
# ------------------------------------------------------------------------------------------------------------------- #

t3 = test.Test()
for n in range(start, stop+1, step):
    pattern = sg.regex_str_generator(f'a^{n}')
    t3.run_test(pattern, text3, n=n, test_rep=test_rep, r=5)

print("TEST 3 RESULTS")
print(f'naive times: ' + f"{t3.naive['times']}\n")
print(f'kmp times: ' + f"{t3.kmp['times']}\n")

create_plots(t3, 'Test 3', yscale=1.8)




# t3 = test.Test()
# for n in range(start, stop+1, step):
#     pattern = sg.regex_str_generator(f'(abc)^{n//3}(c)(ba)^{n//3}(c)^{n//4}')
#     t3.run_test(pattern, text3, n=n, test_rep=test_rep, r=5)
# test_suite = dict()
# naive['times'] = dict()
# kmp['times'] = dict()
#
# for n in range(start, stop+1, step):
#     pattern = sg.regex_str_generator(f'(abc)^{n//3}(c)(ba)^{n//3}(c)^{n//4}')
#     test_suite[n] = test.Test("res/regex_abc.txt", pattern)
#     naive['times'][n] = min(timeit.repeat(test_suite[n].run_naive_sm, repeat=test_rep, number=1))
#     kmp['times'][n] = min(timeit.repeat(test_suite[n].run_kmp_sm, repeat=test_rep, number=1))
#     kmp['offsets'][n] = test_suite[n].kmp_offsets
#     naive['offsets'][n] = test_suite[n].naive_offsets
#
# print(f'\nnaive times: ' + str([f"{naive['times'][i]: .6f}" for i in naive['times']]))
# print(f'\nkmp times: ' + str([f"{kmp['times'][i]: .6f}" for i in kmp['times']]))

# ------------------------------------------------------------------------------------------------------------------- #
# Then it writes the results in 2 distinct files.
# ------------------------------------------------------------------------------------------------------------------- #
#
# with open("docs/naive.txt", "w") as naive:
#     naive.write('NAIVE ALGORITHM\n' +
#                 '---------------------------------\n' +
#                 f'searching for pattern "{pattern}"\n' +
#                 '---------------------------------\n')
#     [naive.write(f'match with offset: {i}\n') for i in naive['offsets']]
#     naive.write('---------------------------------\n' +
#                 f'total matches: {len(naive['offsets'])}')
#
# with open("docs/kmp.txt", "w") as kmp:
#     kmp.write('KMP ALGORITHM\n' +
#               '---------------------------------\n' +
#               f'searching for pattern "{pattern}"\n' +
#               '---------------------------------\n')
#     [kmp.write(f'match with offset: {i}\n') for i in kmp['offsets']]
#     kmp.write('---------------------------------\n' +
#               f'total matches: {len(kmp['offsets'])}')
#
#
