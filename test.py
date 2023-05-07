"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This module define the "Test" class.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import timeit as time
import strmatch as sm


# ------------------------------------------------------------------------------------------------------------------- #
# TODO add description of the class
# ------------------------------------------------------------------------------------------------------------------- #
class Test:
    def __init__(self, text_file, pattern, rep):
        # ----------------------------------------------------------------------------------------------------------- #
        # It reads the file and it calls the methods which implement the algorithms storing the offsets result in the
        # self.*_offsets variables. It also computes the times used by the methods to execute.
        # ----------------------------------------------------------------------------------------------------------- #
        with open(text_file, "r", encoding='utf-8') as file:
            self.text = file.read()
        self.pattern = pattern

        self.naive_time = 0
        for i in range(0, rep):
            start = time.timeit()
            self.naive_offsets = sm.naive_sm(pattern, self.text)
            self.naive_time += time.timeit() - start
        self.naive_time /= rep

        self.kmp_time = 0
        for i in range(0, rep):
            start = time.timeit()
            self.kmp_offsets = sm.kmp_sm(pattern, self.text)
            self.kmp_time += time.timeit() - start
        self.kmp_time /= rep

