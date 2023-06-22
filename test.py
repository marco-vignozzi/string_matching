"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This module define the "Test" class.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import timeit
import strmatch


# ------------------------------------------------------------------------------------------------------------------- #
# This class defines a 'Test' object which stores the result of the algorithms executions.
# It has the following attributes:
# - pattern: stores the pattern used in the test
# - text: a dict containing the text used in a certain execution identified by the key, which is the length of the text
#         used in that execution.
# - naive: a dict of dict. The sub-dicts are addressed with the key 'offsets' and 'times' and stores the value of the
#         execution times and the number of the matches for the naive algorithm, identified as above.
# - kmp: a dict of dict, same as naive.
# The class initialize the pattern via constructor.
# The 'run_test' method executes both algorithms and stores the results in the dictionaries.
# ------------------------------------------------------------------------------------------------------------------- #

class Test:
    def __init__(self, pattern):
        self.text = dict()
        self.pattern = pattern

        self.naive = dict()
        self.naive['times'] = dict()
        self.naive['offsets'] = dict()

        self.kmp = dict()
        self.kmp['times'] = dict()
        self.kmp['offsets'] = dict()

    def run_test(self, text, n, test_rep=5, r=6):
        def run_naive_sm():
            strmatch.naive_sm(self.pattern, text)
            return

        def run_kmp_sm():
            strmatch.kmp_sm(self.pattern, text)
            return

        self.text[n] = text
        self.naive['times'][n] = round(min(timeit.repeat(run_naive_sm, repeat=test_rep, number=1)), r)
        self.kmp['times'][n] = round(min(timeit.repeat(run_kmp_sm, repeat=test_rep, number=1)), r)
        self.kmp['offsets'][n] = strmatch.kmp_sm(self.pattern, text)
        self.naive['offsets'][n] = strmatch.naive_sm(self.pattern, text)
