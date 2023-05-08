"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this module we run various tests from the test.py module in order to compare the string matching algorithms given
in the strmatch.py module.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import test
import timeit
import strgenerator as sg


# ----------------------------------------------------------------------------------------------------------- #
# Here we can initialize some variables which will define the tests.
# ----------------------------------------------------------------------------------------------------------- #

test_rep = 10
pattern = sg.regex_str_generator('(ab)^1000(b)')
t1 = test.Test("res/regex_ab.txt", pattern)


# ----------------------------------------------------------------------------------------------------------- #
# Here it computes the times spent by the 2 algorithms. It only considers the best times as it's explained to
# be the best way to produce meaningful results in the "timeit" module documentation.
# ----------------------------------------------------------------------------------------------------------- #

naive_time = min(timeit.repeat(t1.run_naive_sm, repeat=test_rep, number=1))
kmp_time = min(timeit.repeat(t1.run_kmp_sm, repeat=test_rep, number=1))
print(f'kmp time: {kmp_time : .5f}\t naive time: {naive_time : .5f}')

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
