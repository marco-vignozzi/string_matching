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
######################### - "offsets.txt": it will store the matching offsets found by the algorithms.
# - "matches.txt": it will store the number of matches for each algorithm.
# - "times.txt": it will store their execution times.
# - "texts.txt": it will store the texts on which the test has been conducted.
# - "plot.png": it will store a plot comparing Naive vs KMP times for the current test.
#
# ***create_plot()***
#
# This function creates a plot with 2 or 3 different functions. It takes 3 or 4 lists as an input, containing the values
# of the functions to plot (x-axis values of 'arr_x' will be the same for all of them), a 'legend' (list of strings
# identifying the functions), a 'title' for the plot and the 'path' where you want to save the resulting plot.
# ------------------------------------------------------------------------------------------------------------------- #

def create_docs(test, dir_name, plot_title, mono_txt=False):
    if 'docs' not in os.listdir():
        os.mkdir('docs')
    if dir_name not in os.listdir('docs/'):
        os.mkdir(f'docs/{dir_name}')

    separator_str = '-----------------------------------------------\n'

    with open(f'docs/{dir_name}/matches.txt', "w") as o:
        o.write('\nMATCHES\n\n' +
                'Here is a list of the number of matches for this test case.\n\n')
        for n in test.text:
            o.write(separator_str +
                    f'PATTERN for n={n}: "{test.pattern}"\n' + separator_str)
            o.write(f"NAIVE matches: {test.naive['offsets'][n]}\n")
            o.write(f"KMP matches: {test.kmp['offsets'][n]}\n")

    # with open(f'docs/{dir_name}/offsets.txt', "w") as o:
        # o.write('\nOFFSETS\n\n' +
        #         'Here is a list of the offsets found for this test case.\n\n')
        # for n in test.text:
        #     o.write(separator_str +
        #             f'PATTERN for n={n}: "{test.pattern}"\n' + separator_str)
        #     o.write('NAIVE offsets found:\n')
        #     [o.write(f'match with offset: {i}\n') for i in test.naive['offsets'][n]]
        #     o.write(f'total matches: {len(test.naive["offsets"][n])}\n' + separator_str)
        #     o.write('KMP offsets found:\n')
        #     [o.write(f'match with offset: {i}\n') for i in test.kmp['offsets'][n]]
        #     o.write(f'total matches: {len(test.kmp["offsets"][n])}\n' + separator_str)

    with open(f'docs/{dir_name}/times.txt', "w") as t:
        t.write('\nTIMES\n\n' +
                'Here is a list of the execution times for this test case.\n\n')
        for n in test.text:
            t.write(separator_str +
                    f'PATTERN for n={n}: "{test.pattern}"\n' + separator_str)
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
    create_plot(n_values, naive_t, kmp_t, None, ['Naive', 'KMP'], plot_title, f'docs/{dir_name}/plot.png')
    return


def create_plot(arr_x, arr_y1, arr_y2, arr_y3, legend, title, path, xlabel=''):
    if arr_y3 is not None:
        plt.plot(arr_x, arr_y1, 'r-', arr_x, arr_y2, 'b-', arr_x, arr_y3, 'g-')
        plt.legend(legend)
        plt.xlim([min(arr_x), 1.02 * max(arr_x)])
        plt.ylim([0, 1.2 * max(arr_y1[-1], arr_y2[-1], arr_y3[-1])])
    else:
        plt.plot(arr_x, arr_y1, 'r-', arr_x, arr_y2, 'b-')
        plt.legend(legend)
        plt.xlim([min(arr_x), 1.02 * max(arr_x)])
        plt.ylim([0, 1.2 * max(arr_y1[-1], arr_y2[-1])])
    if xlabel == '':
        plt.xlabel('Lunghezza testo')
    else:
        plt.xlabel(xlabel)
    plt.ylabel('Tempo di esecuzione')
    plt.title(title)
    plt.savefig(path)
    plt.clf()
    return


# ------------------------------------------------------------------------------------------------------------------- #
# Here we can initialize some variables which will define the tests:
# - test_rep: number of times each execution is repeated. It will afflict the precision of the execution times.
# - text_div: number of parts in which the text is divided in each test.
# - src1,src3: the paths to the .txt files used as text.
# ------------------------------------------------------------------------------------------------------------------- #

test_rep = 5
text_div = 20

src1 = 'res/regex_a.txt'
src3 = 'res/regex_ab.txt'

with open(src1, 'r', encoding='utf-8') as file:
    text1 = file.read()

with open(src3, 'r', encoding='utf-8') as file:
    text3 = file.read()

# t = test.Test('res/freedom.txt', 'freedom')
#
# print(t.naive_offsets)
# print(len(t.naive_offsets))

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 1
# We consider a sequence of "a" with increasing length as the text, and we search for the pattern made by 50 "a".
# This test will consider the scenario where we search for a pattern which is always matched.
# Test's data will be stored in a "Test" object, as for the other tests.
# ------------------------------------------------------------------------------------------------------------------- #

t1 = test.Test('a'*50)
for i in range(1, text_div + 1):
    n = len(text1) // text_div * i
    text = text1[0: n]
    t1.run_test(text, n=n, test_rep=test_rep, r=5)

print("TEST 1 RESULTS")
print(f'naive times: ' + f"{t1.naive['times']}\n")
print(f'kmp times: ' + f"{t1.kmp['times']}\n")

create_docs(t1, 'TEST1', plot_title='TEST 1')

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 2
# Here we compare the algorithms searching the same random pattern in a text randomly generated on each iteration with
# increasing length.
# ------------------------------------------------------------------------------------------------------------------- #

t2 = test.Test(sg.rand_str_generator(sg.hex_alpha, 4, 4, 1))
for i in range(1, text_div + 1):
    text = sg.rand_str_generator(sg.hex_alpha, i*20000, i*20000, 1)
    t2.run_test(text, n=len(text), test_rep=test_rep, r=5)

print("TEST 2 RESULTS")
print(f'naive times: ' + f"{t2.naive['times']}\n")
print(f'kmp times: ' + f"{t2.kmp['times']}\n")

create_docs(t2, 'TEST2', plot_title='TEST 2')

# ------------------------------------------------------------------------------------------------------------------- #
# TEST 3
# Here the algorithms are compared with a text of increasing length between 100.000/text_div and 100.000 chars with step
# 100.000/text_div. It is a repetition of a sequence composed by 49 "a" followed by 1 "b".
# The searched pattern is a sequence of 50 "a".
# In this scenario we search for a pattern with a long prefix matching the text, but it never matches completely.
# The intent is to force the KMP algorithm to repeat his inner while cycle the maximum amount of times.
# ------------------------------------------------------------------------------------------------------------------- #

t3 = test.Test('a'*50)
for i in range(1, text_div + 1):
    n = len(text3) // text_div * i
    text = text3[0: n]
    t3.run_test(text, n=n, test_rep=test_rep, r=5)

print("TEST 3 RESULTS")
print(f'naive times: ' + f"{t3.naive['times']}\n")
print(f'kmp times: ' + f"{t3.kmp['times']}\n")

create_docs(t3, 'TEST3', plot_title='TEST 3')

# ------------------------------------------------------------------------------------------------------------------- #
# COMPARISON
# Here each algorithm is compared by himself according to the results in the TEST1 and TEST3.
# We only create a plot for each comparison.
# ------------------------------------------------------------------------------------------------------------------- #

t2c = test.Test(sg.rand_str_generator(sg.hex_alpha, 4, 4, 1))
for i in range(1, text_div + 1):
    text = sg.rand_str_generator(sg.hex_alpha, i*5000, i*5000, 1)
    t2c.run_test(text, n=len(text), test_rep=test_rep, r=5)

create_docs(t2c, 'TEST2C', plot_title='TEST 2C')

naive1 = np.array([t1.naive['times'][i] for i in t1.naive['times']])
naive2c = np.array([t2c.naive['times'][i] for i in t2c.naive['times']])
naive3 = np.array([t3.naive['times'][i] for i in t3.naive['times']])

kmp1 = np.array([t1.kmp['times'][i] for i in t1.kmp['times']])
kmp2c = np.array([t2c.kmp['times'][i] for i in t2c.kmp['times']])
kmp3 = np.array([t3.kmp['times'][i] for i in t3.kmp['times']])

n_values = np.array([i for i in t1.naive['times']])

create_plot(n_values, naive1, naive2c, naive3, ['Test 1', 'Test 2', 'Test 3'],
            'Confronto Naive', 'docs/naive_comp.png', xlabel='Lunghezza testo')
create_plot(n_values, kmp1, kmp2c, kmp3, ['Test 1', 'Test 2', 'Test 3'],
            'Confronto KMP', 'docs/kmp_comp.png', xlabel='Lunghezza testo')

