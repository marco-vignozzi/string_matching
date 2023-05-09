"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This module define the "Test" class.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import timeit
import strmatch


# ------------------------------------------------------------------------------------------------------------------- #
# TODO: add description of the class
# ------------------------------------------------------------------------------------------------------------------- #
class Test:
    def __init__(self):
        self.text = dict()
        self.pattern = dict()

        self.naive = dict()
        self.naive['times'] = dict()
        self.naive['offsets'] = dict()

        self.kmp = dict()
        self.kmp['times'] = dict()
        self.kmp['offsets'] = dict()

    def run_test(self, pattern, text, n=0, test_rep=5, r=6):
        def run_naive_sm():
            strmatch.naive_sm(pattern, text)
            return

        def run_kmp_sm():
            strmatch.kmp_sm(pattern, text)
            return
        self.pattern[n] = pattern
        self.text[n] = text
        self.naive['times'][n] = round(min(timeit.repeat(run_naive_sm, repeat=test_rep, number=1)), r)
        self.kmp['times'][n] = round(min(timeit.repeat(run_kmp_sm, repeat=test_rep, number=1)), r)
        self.kmp['offsets'][n] = strmatch.kmp_sm(pattern, text)
        self.naive['offsets'][n] = strmatch.naive_sm(pattern, text)
