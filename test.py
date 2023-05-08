"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This module define the "Test" class.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
import strmatch


# ------------------------------------------------------------------------------------------------------------------- #
# TODO: add description of the class
# ------------------------------------------------------------------------------------------------------------------- #
class Test:
    def __init__(self, text_file, pattern):
        with open(text_file, "r", encoding='utf-8') as file:
            self.text = file.read()
        self.pattern = pattern

        self.naive_offsets = strmatch.naive_sm(self.pattern, self.text)
        self.kmp_offsets = strmatch.kmp_sm(self.pattern, self.text)

        self.naive_time = 0
        self.kmp_time = 0

    def run_naive_sm(self):
        strmatch.naive_sm(self.pattern, self.text)
        return

    def run_kmp_sm(self):
        strmatch.kmp_sm(self.pattern, self.text)
        return
