"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we run various tests from the test.py module in order test_suite. compare the string matching algorithms given
in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import test
import timeit
import strgenerator as sg


# ------------------------------------------------------------------------------------------------------------------- #
# TODO: add description and code test_suite. this segment
# ------------------------------------------------------------------------------------------------------------------- #

def run_test():         # should I...???
    pass


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
naive = dict()
naive['times'] = dict()
naive['offsets'] = dict()
kmp = dict()
kmp['times'] = dict()
kmp['offsets'] = dict()

# ------------------------------------------------------------------------------------------------------------------- #
# This is the first test case: we consider a sequence of 'a' with increasing length in range "start - stop" with
# the given "step" as the queried pattern. The text is a longer sequence of 'a'.
# It instantiates a test and it computes the times for both the naive and kmp algorithms, storing them into a dict.
# ------------------------------------------------------------------------------------------------------------------- #

for n in range(start, stop+1, step):
    pattern = sg.regex_str_generator(f'(a)^{n}')
    test_suite[n] = test.Test("res/regex_a.txt", pattern)
    naive['times'][n] = min(timeit.repeat(test_suite[n].run_naive_sm, repeat=test_rep, number=1))
    kmp['times'][n] = min(timeit.repeat(test_suite[n].run_kmp_sm, repeat=test_rep, number=1))
    kmp['offsets'][n] = test_suite[n].kmp_offsets
    naive['offsets'][n] = test_suite[n].naive_offsets

print(f'naive times: ' + str([f"{naive['times'][i]: .6f}" for i in naive['times']]))
print(f'\nkmp times: ' + str([f"{kmp['times'][i]: .6f}" for i in kmp['times']]))

test_suite = dict()
naive['times'] = dict()
kmp['times'] = dict()

for n in range(start, stop+1, step):
    pattern = sg.regex_str_generator(f'(abc)^{n//3}(c)(ba)^{n//3}(c)^{n//4}')
    test_suite[n] = test.Test("res/regex_abc.txt", pattern)
    naive['times'][n] = min(timeit.repeat(test_suite[n].run_naive_sm, repeat=test_rep, number=1))
    kmp['times'][n] = min(timeit.repeat(test_suite[n].run_kmp_sm, repeat=test_rep, number=1))
    kmp['offsets'][n] = test_suite[n].kmp_offsets
    naive['offsets'][n] = test_suite[n].naive_offsets

print(f'\nnaive times: ' + str([f"{naive['times'][i]: .6f}" for i in naive['times']]))
print(f'\nkmp times: ' + str([f"{kmp['times'][i]: .6f}" for i in kmp['times']]))

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
