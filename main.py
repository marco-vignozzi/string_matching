"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we run various tests with the test.py module in order to compare the string matching algorithms given
in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import numpy as np
import os

import strgenerator as sg
import matplotlib.pyplot as plt
import test


# ------------------------------------------------------------------------------------------------------------------- #
# The methods below are utility functions that we will use to build our test's documentation.
#
# ***create_docs()***
#
# This function takes the following arguments:
# - test: the test object referring the test of which you want to create the documentation.
# - dir_name: the directory name to which it saves the documentation. If it doesn't exist, it will be created in a
#             subdirectory of the project named docs (if it doesn't exist, it will be created as well).
# - plot_title: the title of the plot that will be created in the file "plot.png".
# - xlabel: the label for the x-axis of the plot.
# - mono_txt: it specifies if the test has been conducted on a unique test.
#
# It will create 3 text files and a plot:
######################### "offsets.txt": it will store the matching offsets found by the algorithms.
# "times.txt": it will store their execution times.
# "texts.txt": it will store the texts on which the test has been conducted.
# "plot.png": it will store a plot comparing Naive vs KMP times for the current test.
# TODO: add create_plot() description
#
# ***create_plot()***
#
# This function creates a plot with 2 different value pairs.
# ------------------------------------------------------------------------------------------------------------------- #

def create_docs(test, dir_name, plot_title, xlabel, mono_txt=False):
    if 'docs' not in os.listdir():
        os.mkdir('docs')
    if dir_name not in os.listdir('docs/'):
        os.mkdir(f'docs/{dir_name}')

    separator_str = '-----------------------------------------------\n'

    with open(f'docs/{dir_name}/matches.txt', "w") as o:
        o.write('\nMATCHES\n\n' +
                'Here is a list of the number of matches for this test case.\n\n')
        for n in test.pattern:
            o.write(separator_str +
                    f'PATTERN for n={n}: "{test.pattern[n]}"\n' + separator_str)
            o.write(f"NAIVE matches: {test.naive['offsets'][n]}\n")
            o.write(f"KMP matches: {test.kmp['offsets'][n]}\n")

    # with open(f'docs/{dir_name}/offsets.txt', "w") as o:
        # o.write('\nOFFSETS\n\n' +
        #         'Here is a list of the offsets found for this test case.\n\n')
        # for n in test.pattern:
        #     o.write(separator_str +
        #             f'PATTERN for n={n}: "{test.pattern[n]}"\n' + separator_str)
        #     o.write('NAIVE offsets found:\n')
        #     [o.write(f'match with offset: {i}\n') for i in test.naive['offsets'][n]]
        #     o.write(f'total matches: {len(test.naive["offsets"][n])}\n' + separator_str)
        #     o.write('KMP offsets found:\n')
        #     [o.write(f'match with offset: {i}\n') for i in test.kmp['offsets'][n]]
        #     o.write(f'total matches: {len(test.kmp["offsets"][n])}\n' + separator_str)

    with open(f'docs/{dir_name}/times.txt', "w") as t:
        t.write('\nTIMES\n\n' +
                'Here is a list of the execution times for this test case.\n\n')
        for n in test.pattern:
            t.write(separator_str +
                    f'PATTERN for n={n}: "{test.pattern[n]}"\n' + separator_str)
            t.write(f'NAIVE execution time: {test.naive["times"][n]}\n' + separator_str)
            t.write(f'KMP execution time: {test.kmp["times"][n]}\n' + separator_str)

    with open(f'docs/{dir_name}/texts.txt', "w") as txt:
        txt.write('\nTEXTS\n\n' +
                  'Here is a list of the texts used for this test case.\n\n')
        if mono_txt:
            txt.write(separator_str + f'UNIQUE TEXT USED: "{test.text[n]}"\n')
        else:
            for n in test.text:
                txt.write(separator_str + f'TEXT for n={n}: "{test.text[n]}"\n')

    naive_t = np.array([test.naive['times'][i] for i in test.naive['times']])
    kmp_t = np.array([test.kmp['times'][i] for i in test.kmp['times']])
    n_values = np.array([i for i in test.naive['times']])
    create_plot(n_values, naive_t, kmp_t, ['Naive', 'KMP'], xlabel, plot_title, f'docs/{dir_name}/plot.png')
    return


def create_plot(arr_x, arr_y1, arr_y2, legend, xlabel, title, path):
    plt.plot(arr_x, arr_y1, 'r-', arr_x, arr_y2, 'b-')
    plt.legend(legend)
    plt.xlim([min(arr_x), 1.02 * max(arr_x)])
    plt.ylim([0, 1.2 * max(arr_y1[-1], arr_y2[-1])])
    plt.xlabel(xlabel)
    plt.ylabel('Execution time')
    plt.title(title)
    plt.savefig(path)
    plt.clf()
    return


# ------------------------------------------------------------------------------------------------------------------- #
# Here we can initialize some variables which will define the tests.
# ------------------------------------------------------------------------------------------------------------------- #

test_rep = 5
start = 100
stop = 500
step = 20
text_div = 20

src1 = 'res/regex_a.txt'
src2 = 'res/bible.txt'
src2r = 'res/rand_hex.txt'
src3 = 'res/regex_ab.txt'

with open(src1, 'r', encoding='utf-8') as file:
    text1 = file.read()

with open(src2r, 'r', encoding='utf-8') as file:
    text2r = file.read()

with open(src2, 'r', encoding='utf-8') as file:
    text2 = file.read()

with open(src3, 'r', encoding='utf-8') as file:
    text3 = file.read()

# t = test.Test('res/freedom.txt', 'freedom')
#
# print(t.naive_offsets)
# print(len(t.naive_offsets))

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 1M
# We consider a sequence of "a" with increasing length in range "start - stop" with the given "step" as the queried
# pattern. The text is a sequence of 10.000 "a" chars.
# This test will consider the scenario where we search for a pattern which is always matched.
# Test's data will be stored in a "Test" object, as for the other tests.
#
# TEST 1N
# The test is almost the same, but this time we consider a text with increasing length. In order to have a meaningful
# comparison we create a 10 times bigger text then the previous one.
# ------------------------------------------------------------------------------------------------------------------- #

t1 = test.Test()
pattern = 'a'*50
for i in range(1, text_div + 1):
    n = len(text1) // text_div * i
    text = text1[0: n]
    t1.run_test(pattern, text, n=n, test_rep=test_rep, r=5)

print("TEST 1 RESULTS")
print(f'naive times: ' + f"{t1.naive['times']}\n")
print(f'kmp times: ' + f"{t1.kmp['times']}\n")

create_docs(t1, 'TEST1', plot_title='Always matching pattern, growing text', xlabel='Text length')

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 2
# Here we compare the algorithms with a text of increasing length, searching for the same, short, and averagely
# frequent pattern.
# ------------------------------------------------------------------------------------------------------------------- #

t2 = test.Test()
pattern = sg.rand_str_generator(sg.hex_alpha, 4, 4, 1)
for i in range(1, text_div + 1):
    text = sg.rand_str_generator(sg.hex_alpha, i*20000, i*20000, 1)
    t2.run_test(pattern, text, n=len(text), test_rep=test_rep, r=5)

print("TEST 2 RESULTS")
print(f'naive times: ' + f"{t2.naive['times']}\n")
print(f'kmp times: ' + f"{t2.kmp['times']}\n")

create_docs(t2, 'TEST2', plot_title='Average matching pattern', xlabel='Text length')

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 3
# Here the algorithms are compared with a text of increasing length between 100.000/text_div and 100.000 chars with step
# text_div. It is a repetition of a sequence composed by 99 "a" followed by 1 "b".
# The searched pattern is a sequence of 100 "a".
# In this scenario we search for a pattern with a long prefix matching the text, but it never matches completely.
# The intent is to force the KMP algorithm to repeat his inner while cycle the maximum amount of times.
# ------------------------------------------------------------------------------------------------------------------- #

t3 = test.Test()
pattern = 'a'*50
for i in range(1, text_div + 1):
    n = len(text3) // text_div * i
    text = text3[0: n]
    t3.run_test(pattern, text, n=n, test_rep=test_rep, r=5)

print("TEST 3 RESULTS")
print(f'naive times: ' + f"{t3.naive['times']}\n")
print(f'kmp times: ' + f"{t3.kmp['times']}\n")

create_docs(t3, 'TEST3', plot_title='Never matching pattern, worst case KMP', xlabel='Text length')

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 4
# TODO: add description
# ------------------------------------------------------------------------------------------------------------------- #

t4 = test.Test()
pattern = 'c'*50
for i in range(1, text_div + 1):
    n = len(text1) // text_div * i
    text = text1[0: n]
    t4.run_test(pattern, text, n=n, test_rep=test_rep, r=5)

print("TEST 4 RESULTS")
print(f'naive times: ' + f"{t4.naive['times']}\n")
print(f'kmp times: ' + f"{t4.kmp['times']}\n")

create_docs(t4, 'TEST4', plot_title='Never matching pattern, growing text', xlabel='Text length')

# ------------------------------------------------------------------------------------------------------------------- #
# COMPARISON
# Here each algorithm is compared by himself according to the results in the TEST1 and TEST3.
# We only create a plot for each comparison.
# ------------------------------------------------------------------------------------------------------------------- #

naive1 = np.array([t1.naive['times'][i] for i in t1.naive['times']])
naive3 = np.array([t3.naive['times'][i] for i in t3.naive['times']])
kmp1 = np.array([t1.kmp['times'][i] for i in t1.kmp['times']])
kmp3 = np.array([t3.kmp['times'][i] for i in t3.kmp['times']])
n_values = np.array([i for i in t1.naive['times']])

create_plot(n_values, naive1, naive3, ['Always matching', 'Never matching'], 'Text length',
            'Naive comparison: Always vs Never matching', 'docs/naive13.png')
create_plot(n_values, kmp1, kmp3, ['Always matching', 'Never matching'], 'Text length',
            'KMP comparison: Always vs Never matching', 'docs/kmp13.png')

