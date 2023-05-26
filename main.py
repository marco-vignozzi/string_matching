"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we run various tests from the test.py module in order to compare the string matching algorithms given
in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import numpy as np
import os

import strgenerator as sg
import matplotlib.pyplot as plt
import test


# ------------------------------------------------------------------------------------------------------------------- #
# TODO: add description and code for create_docs()
# Here is the definition of 2 utility function that we will use to build our test's documentation:
#
# ***create_docs()***
#
# ***create_plot()***
# This function takes 3 arguments:
# - test: the test object referring the test of which you want to create the plot.
# - title: the title of the plot.
# - yscale: the scaling value of the y-axis as a float (it refers to the time values)
# It will create a plot comparing naive vs KMP times (y-axis) for the current test.
# ------------------------------------------------------------------------------------------------------------------- #

def create_docs(test, dir_name):
    if 'docs' not in os.listdir():
        os.mkdir('docs')
    if dir_name not in os.listdir('docs/'):
        os.mkdir(f'docs/{dir_name}')

    with open(f'docs/{dir_name}/offsets.txt', "w") as o:
        o.write('\nOFFSETS\n\n' +
                'Here is a list of the offsets found for this test case.\n\n' +
                '-----------------------------------------------\n')
        for n in test.pattern:
            o.write('-----------------------------------------------\n' +
                    f'PATTERN for n={n}: "{test.pattern[n]}"\n' +
                    '-----------------------------------------------\n' +
                    '-----------------------------------------------\n')
            o.write('NAIVE offsets found:\n')
            [o.write(f'match with offset: {i}\n') for i in test.naive['offsets'][n]]
            o.write(f'total matches: {len(test.naive["offsets"][n])}\n' +
                    '-----------------------------------------------\n')
            o.write('KMP offsets found:\n')
            [o.write(f'match with offset: {i}\n') for i in test.kmp['offsets'][n]]
            o.write(f'total matches: {len(test.kmp["offsets"][n])}\n' +
                    '-----------------------------------------------\n')

    with open(f'docs/{dir_name}/times.txt', "w") as t:
        t.write('\nTIMES\n\n' +
                'Here is a list of the execution times for this test case.\n\n' +
                '-----------------------------------------------\n')
        for n in test.pattern:
            t.write('-----------------------------------------------\n' +
                    f'PATTERN for n={n}: "{test.pattern[n]}"\n' +
                    '-----------------------------------------------\n' +
                    '-----------------------------------------------\n')
            t.write(f'NAIVE execution time: {test.naive["times"][n]}\n')
            t.write('-----------------------------------------------\n')
            t.write(f'KMP execution time: {test.kmp["times"][n]}\n')
            t.write('-----------------------------------------------\n')

    with open(f'docs/{dir_name}/texts.txt', "w") as txt:
        txt.write('\nTEXTS\n\n' +
                  'Here is a list of the texts used for this test case.\n\n' +
                  '---------------------------------------------\n')
        if test.text[0] != test.text[-1]:                   # FIXME: fix the KeyError
            t.write(f'TEXT for n={n}: "{test.text[n]}"\n' +
                    '-----------------------------------------------\n')
        else:
            t.write(f'SINGLE TEXT USED: "{test.text[n]}"\n' +
                    '-----------------------------------------------\n')

    return


def create_plot(test, title, yscale):
    naive_t = np.array([test.naive['times'][i] for i in test.naive['times']])
    kmp_t = np.array([test.kmp['times'][i] for i in test.kmp['times']])
    n_values = np.array([i for i in test.naive['times']])
    plt.plot(n_values, naive_t, 'r-', n_values, kmp_t, 'b-')
    plt.legend(['Naive', 'KMP'])
    plt.axis([min(n_values), 1.02 * max(n_values), 0, yscale * max(naive_t[-1], kmp_t[-1])])

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
# test_suite = dict()
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
# Test's data will be stored in a "Test" object, as for the others tests.
# ------------------------------------------------------------------------------------------------------------------- #

t1 = test.Test()
for n in range(start, stop + 1, step):
    pattern = sg.regex_str_generator(f'(a)^{n}')
    t1.run_test(pattern, text1, n=n, test_rep=test_rep, r=5)

print("TEST 1 RESULTS")
print(f'naive times: ' + f"{t1.naive['times']}\n")
print(f'kmp times: ' + f"{t1.kmp['times']}\n")

# create_plot(t1, 'Test 1', yscale=1.2)
create_docs(t1, 'TEST1')

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 2
# Here we compare the algorithms with a text of increasing length, searching for the same, short, and averagely
# frequent pattern.
# ------------------------------------------------------------------------------------------------------------------- #

t2 = test.Test()
pattern = 'And'
for n in range(text_div, 0, -1):
    text = text2[0: len(text2) // n]
    t2.run_test(pattern, text, n=abs(text_div - n + 1), test_rep=test_rep, r=5)

print("TEST 2 RESULTS")
print(f'naive times: ' + f"{t2.naive['times']}\n")
print(f'kmp times: ' + f"{t2.kmp['times']}\n")

# create_plot(t2, 'Test 2', yscale=1.2)
create_docs(t2, 'TEST2')

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 3
# Here the algorithms are compared with a text of 1 million chars. It is a repetition of a sequence composed by 99 "a"
# followed by 1 "b".
# The searched pattern is a sequence of "a" with increasing length in the usual (start - stop) range.
# In this scenario we search for a pattern with a long prefix matching the text, but it never matches completely.
# The intent is to force the KMP algorithm to repeat his inner while cycle the maximum amount of times.
# ------------------------------------------------------------------------------------------------------------------- #

t3 = test.Test()
pattern = sg.regex_str_generator(f'(a)^{100}')
for n in range(text_div, 0, -1):
    text = text3[0: len(text3) // n]
    t3.run_test(pattern, text, n=abs(text_div - n + 1), test_rep=test_rep, r=5)

print("TEST 3 RESULTS")
print(f'naive times: ' + f"{t3.naive['times']}\n")
print(f'kmp times: ' + f"{t3.kmp['times']}\n")

create_plot(t3, 'Test 3', yscale=1.2)
create_docs(t3, 'TEST3')

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
