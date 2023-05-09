"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we run various tests from the test.py module in order to compare the string matching algorithms given
in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import test
import strgenerator as sg


# ------------------------------------------------------------------------------------------------------------------- #
# TODO: add description and code to this segment
# ------------------------------------------------------------------------------------------------------------------- #

def create_docs():
    pass


def create_plots():
    pass


# ------------------------------------------------------------------------------------------------------------------- #
# Here we can initialize some variables which will define the tests.
# ------------------------------------------------------------------------------------------------------------------- #

test_rep = 10
start = 10
stop = 100
step = 10
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


# ------------------------------------------------------------------------------------------------------------------- #
# This is the first test case: we consider a sequence of 'a' with increasing length in range "start - stop" with
# the given "step" as the queried pattern. The text is a longer sequence of 'a'.
# It instantiates a test and it computes the times for both the naive and kmp algorithms, storing them into a dict.
# ------------------------------------------------------------------------------------------------------------------- #

t1 = test.Test()
for n in range(start, stop+1, step):
    pattern = sg.regex_str_generator(f'(a)^{n}')
    t1.run_test(pattern, text1, n=n, test_rep=test_rep, r=5)

print("TEST 1 RESULTS")
print(f'naive times: ' + f"{t1.naive['times']}\n")
print(f'kmp times: ' + f"{t1.kmp['times']}\n")


t2 = test.Test()
for n in range(10, 0, -1):
    text = text2[0: len(text2) // n]
    t2.run_test('And', text, n=n, test_rep=test_rep, r=5)

print("TEST 2 RESULTS")
print(f'naive times: ' + f"{t2.naive['times']}\n")
print(f'kmp times: ' + f"{t2.kmp['times']}\n")


t3 = test.Test()
for n in range(start, stop+1, step):
    pattern = sg.regex_str_generator(f'a^{n}')
    t3.run_test(pattern, text3, n=n, test_rep=test_rep, r=5)

print("TEST 3 RESULTS")
print(f'naive times: ' + f"{t3.naive['times']}\n")
print(f'kmp times: ' + f"{t3.kmp['times']}\n")


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
