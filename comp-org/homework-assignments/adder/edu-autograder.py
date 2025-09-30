"""
Autograder for ripple-carry adder

EDCI 5004: Computer Organization for Educators

Clayton Cafiero <cbcafier@uvm.edu>

Note: Docstrings on test methods are incorporated into JSON output as
values for key "name", so be careful what you put in these docstrings.
"""
from pathlib import Path
import unittest

from gradescope_utils.autograder_utils.decorators \
    import partial_credit, weight

from proc import run, run_flake8
from util import check_for_prohibited_functions, check_for_prohibited_methods, test_import


TIMEOUT = 30  # seconds
ENCODING = 'UTF8'
TARGET_FILE = 'ripple_adder.py'
MODULE_NAME = 'ripple_adder'


FULL_ADDER_TESTS = [((0, 0, 0), (0, 0)),
                    ((0, 0, 1), (1, 0)),
                    ((0, 1, 0), (1, 0)),
                    ((0, 1, 1), (0, 1)),
                    ((1, 0, 0), (1, 0)),
                    ((1, 0, 1), (0, 1)),
                    ((1, 1, 0), (0, 1)),
                    ((1, 1, 1), (1, 1))]

RIPPLE_CARRY_TESTS = [((0b0000, 0b0000), (0, [0, 0, 0, 0])),
                      ((0b0001, 0b0000), (0, [0, 0, 0, 1])),
                      ((0b0000, 0b0001), (0, [0, 0, 0, 1])),
                      ((0b0001, 0b0001), (0, [0, 0, 1, 0])),
                      ((0b0010, 0b0010), (0, [0, 1, 0, 0])),
                      ((0b0100, 0b0100), (0, [1, 0, 0, 0])),
                      ((0b0011, 0b0011), (0, [0, 1, 1, 0])),
                      ((0b0101, 0b0101), (0, [1, 0, 1, 0])),
                      ((0b0111, 0b0111), (0, [1, 1, 1, 0])),
                      ((0b1000, 0b0111), (0, [1, 1, 1, 1])),
                      ((0b1010, 0b0101), (0, [1, 1, 1, 1])),
                      ((0b0110, 0b0110), (0, [1, 1, 0, 0])),
                      ((0b1111, 0b0001), (1, [0, 0, 0, 0])),
                      ((0b1110, 0b1110), (1, [1, 1, 0, 0])),
                      ((0b0111, 0b1100), (1, [0, 0, 1, 1])),
                      ((0b1001, 0b1001), (1, [0, 0, 1, 0])),
                      ((0b1111, 0b1111), (1, [1, 1, 1, 0]))]

class TestPrime(unittest.TestCase):

    target_file = TARGET_FILE
    module_name = MODULE_NAME
    target_file_present = False
    ok = True
    messages = []

    @classmethod
    def setUpClass(cls):
        """This is run once to initialize class. """
        cls.target_file_present = Path(cls.target_file).is_file()
        if cls.target_file_present:
            if cls.ok:
                cls.ok, cls.messages = test_import(cls.module_name)
            if cls.ok:
                cls.ok, cls.messages = check_for_prohibited_functions(cls.target_file)
            # if cls.ok:
            #     cls.ok, cls.messages = check_for_prohibited_methods(cls.target_file)
        else:
            cls.ok = False
            cls.messages.append(f"Looking for {cls.target_file}, but I've not found it!")

    def setUp(self):
        """This is run before each test. """
        if not self.target_file_present:
            self.fail(f'Target file {self.target_file} not found! '
                      f'File should be named {self.target_file}.')
        if not self.ok:
            s = " ".join(self.messages)
            self.fail(f'Aborting tests. {s}')

    @staticmethod
    def parse_output(data):
        chunks = re.split(r'\:\s|\n', data)
        return [chunk for chunk in chunks if chunk != '']

    @partial_credit(8)
    def test_full_adder(self, set_score):
        """Test full_adder(a, b, c_in) function (ripple_adder.py). """
        # Don't need to extract weight. We know we need 8 tests to test
        # all possible cases.
        score = 0
        import ripple_adder
        for i, test in enumerate(FULL_ADDER_TESTS):
            arguments, expected = test
            actual = ripple_adder.full_adder(*arguments)
            if expected == actual:
                if actual:
                    score += 1
                else:
                    print(f"On input {arguments}, "
                          f"expected: {expected} "
                          f"Actual: {actual}")
        set_score(score)


    @partial_credit(12)
    def test_ripple_carry(self, set_score):
        """Test ripple_carry_adder(a, b) function (ripple_adder.py). """
        weight_ = self.test_ripple_carry.__weight__
        num_tests = len(RIPPLE_CARRY_TESTS)
        score = 0
        import ripple_adder
        for i, test in enumerate(RIPPLE_CARRY_TESTS):
            arguments, expected = test
            actual = ripple_adder.ripple_carry_adder(*arguments)
            if expected == actual:
                if actual:
                    score += weight_ / num_tests
                else:
                    print(f"On input {arguments}, "
                          f"expected: {expected} "
                          f"Actual: {actual} (test {i})")
        if score > weight_:
            score = weight_
        set_score(round(score, 2))


    @partial_credit(-10)
    def test_pep8(self, set_score):
        """Style suggestions / PEP 8 conformance (ripple_adder.py). """
        score = 0

        proc = run_flake8(
            self.target_file,
            args=['--config', 'flake8.cfg']
        )

        # print(proc.stdout)
        e211 = - proc.stdout.count('E211')
        e225 = - proc.stdout.count('E225')
        e262 = - proc.stdout.count('E262')
        e301 = - proc.stdout.count('E301')
        e501 = - proc.stdout.count('E501')
        e111 = - proc.stdout.count('E111')
        e117 = - proc.stdout.count('E117')
        total = e211 + e225 + e262 + e301 + e501 + e111 + e117
        # print(f'***** {total} *****')
        if total != 0:
            print('Deducting points for E211, E225, E262, E301, E501, E111, and E117 only.')
        score = total * 0.5
        # print(f'***** {score} *****')
        # E211 whitespace before '('
        # E225 missing whitespace around operator
        # E262 inline comment should start with '# '
        # E301 expected 1 blank line, found 0
        # E501 (^) line too long (82 > 79 characters)
        set_score(round(score, 3))
