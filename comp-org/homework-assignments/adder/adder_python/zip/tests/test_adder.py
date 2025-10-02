import subprocess
import os
import re
from pathlib import Path
import unittest
from proc import run_flake8
from gradescope_utils.autograder_utils.decorators import partial_credit


TIMEOUT = 30 # seconds, not used yet
ENCODING = "UTF8"
TARGET_FILE = "ripple.py"

FULL_ADDER_TESTS = [
    ((0, 0, 0), (0, 0)),
    ((0, 0, 1), (1, 0)),
    ((0, 1, 0), (1, 0)),
    ((0, 1, 1), (0, 1)),
    ((1, 0, 0), (1, 0)),
    ((1, 0, 1), (0, 1)),
    ((1, 1, 0), (0, 1)),
    ((1, 1, 1), (1, 1)),
]

RIPPLE_CARRY_TESTS = [
    ((0b0000, 0b0000), (0, [0, 0, 0, 0])),
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
    ((0b1111, 0b1111), (1, [1, 1, 1, 0])),
]


class TestAdder(unittest.TestCase):
    target_file = TARGET_FILE
    target_file_present = False
    passing = True
    messages = []

    @classmethod
    def setUpClass(cls):
        """run by autograder"""
        cls.target_file_present = Path(cls.target_file).is_file()

    def setUp(self):
        """This is run before each test."""
        if not self.target_file_present:
            self.fail(
                f"Target file {self.target_file} not found! "
                f"File should be named {self.target_file}."
            )
        if not self.passing:
            s = " ".join(self.messages)
            self.fail(f"Aborting tests. {s}")

    @partial_credit(12)
    def test_full_adder(self, set_score):
        """Testing Full_adder(a, b, c_in) functionality"""
        score = 0

        import ripple

        for _, test in enumerate(FULL_ADDER_TESTS):
            arguments, expected = test
            actual = ripple.full_adder(*arguments)
            if expected == actual:
                score += 1.5
            else:
                print(
                    f"On input {arguments}, expected: {expected} Actual: {actual}"
                )
        set_score(score)

    @partial_credit(12)
    def test_ripple_carry(self, set_score):
        score = 0
        weight = 12
        num_tests = len(RIPPLE_CARRY_TESTS)

        import ripple

        for i, test in enumerate(RIPPLE_CARRY_TESTS):
            arguments, expected = test
            actual = ripple.ripple_carry_adder(*arguments)
            if actual == expected:
                score += weight / num_tests
            else:
                print(
                    f"On input {arguments}, "
                    f"expected: {expected} "
                    f"Actual: {actual} (test {i})"
                )

        if score > weight:
            score = weight
        set_score(round(score, 2))

    @partial_credit(-10)
    def test_styling(self, set_score):
        score = 0
        output = run_flake8(
            self.target_file, args=["--config", "flake8.cfg"]
        )

        # print(output.stdout)
        e211 = -output.stdout.count("E211")
        e225 = -output.stdout.count("E225")
        e262 = -output.stdout.count("E262")
        e301 = -output.stdout.count("E301")
        e501 = -output.stdout.count("E501")
        e111 = -output.stdout.count("E111")
        e117 = -output.stdout.count("E117")
        total = e211 + e225 + e262 + e301 + e501 + e111 + e117
        # print(f'***** {total} *****')
        if total != 0:
            print(
                "Deducting points for E211, E225, E262, E301, E501, E111, and E117 only."
            )
        score = total * 0.5
        # print(f'***** {score} *****')
        # E211 whitespace before '('
        # E225 missing whitespace around operator
        # E262 inline comment should start with '# '
        # E301 expected 1 blank line, found 0
        # E501 (^) line too long (82 > 79 characters)
        set_score(round(score, 2))
