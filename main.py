"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we run various tests from the test.py module in order to compare the string matching algorithms given
in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import test
import timeit
import strgenerator as sg


# ----------------------------------------------------------------------------------------------------------- #
# TODO: add description and code to this segment
# ----------------------------------------------------------------------------------------------------------- #

def create_docs():
    pass


def create_plots():
    pass


# ----------------------------------------------------------------------------------------------------------- #
# Here we can initialize some variables which will define the tests.
# ----------------------------------------------------------------------------------------------------------- #

test_rep = 10
start = 100
stop = 1000
step = 50
naive_times = list()
kmp_times = list()
naive_offsets = dict()
kmp_offsets = dict()

# ----------------------------------------------------------------------------------------------------------- #
# Here it computes the times spent by the 2 algorithms. It only considers the best times, as it's explained to
# be the best way to produce meaningful results in the "timeit" module documentation.
# ----------------------------------------------------------------------------------------------------------- #

for n in range(start, stop+1, step):
    pattern = sg.regex_str_generator(f'(a)^{n}')
    t = test.Test("res/regex_ab.txt", pattern)
    naive_times.append(min(timeit.repeat(t.run_naive_sm, repeat=test_rep, number=1)))
    kmp_times.append(min(timeit.repeat(t.run_kmp_sm, repeat=test_rep, number=1)))
    kmp_offsets[n] = t.kmp_offsets
    naive_offsets[n] = t.naive_offsets

print(f'naive times: ' + str([f'{i: .6f}' for i in naive_times]))
print(f'\nkmp times: ' + str([f'{i: .6f}' for i in kmp_times]))
# ----------------------------------------------------------------------------------------------------------- #
# Then it writes the results in 2 distinct files.
# ----------------------------------------------------------------------------------------------------------- #
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
