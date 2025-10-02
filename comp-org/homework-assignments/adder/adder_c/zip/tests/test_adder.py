import subprocess
import re
from pathlib import Path
import unittest
from gradescope_utils.autograder_utils.decorators import partial_credit


TIMEOUT = 30 # seconds, not used yet
ENCODING = "UTF8"
TARGET_FILE = "ripple.c"

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
        try:
            result = subprocess.run(
                [
                    "gcc",
                    "-O0",
                    "-Wall",
                    "-Wextra",
                    "-Wpedantic",
                    "-std=c99",
                    "-o",
                    "ripple",
                    "ripple.c",
                ],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if result.returncode != 0:
                cls.passing = False
                cls.messages.append("C compilation failed:")
                cls.messages.append(result.stderr.strip())
        except Exception as e:
            cls.passing = False
            cls.messages.append(f"Compilation error: {e}")

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
        """Check Full_adder(a, b, c_in) outputs a correct (sum, carry) tuple."""
        score = 0
        for args, expected in FULL_ADDER_TESTS:
            result = subprocess.run(
                ["./ripple", str(args[0]), str(args[1]), str(args[2])],
                capture_output=True,
                text=True,
                timeout=2,
            )

            output = result.stdout.strip().split()
            if len(output) >= 2:
                try:
                    actual = tuple(map(int, output[:2]))
                    if actual == expected:
                        score += 1.5
                    else:
                        print(f"[FAIL] Inputs: {args} → Output: {actual}, Expected: {expected}")
                except ValueError:
                    pass

        set_score(score)


    @partial_credit(12)
    def test_ripple_carry(self, set_score):
        """Check ripple-carry adder outputs correct carry and 4-bit result."""
        score = 0
        weight = 12
        num_tests = len(RIPPLE_CARRY_TESTS)

        for args, expected in RIPPLE_CARRY_TESTS:
            result = subprocess.run(
                ["./ripple", str(args[0]), str(args[1])],
                capture_output=True,
                text=True,
                timeout=2,
            )

            out = result.stdout.strip().split()
            if len(out) == 2:
                try:
                    carry_out = int(out[0])
                    bits_str = out[1].strip()

                    expected_sum = int("".join(str(b) for b in expected[1]), 2)
                    actual_sum = int(bits_str, 2)

                    if carry_out == expected[0] and actual_sum == expected_sum:
                        score += weight / num_tests
                    else:
                        print(
                            f"[FAIL] Inputs: {args} → Output: carry={carry_out}, sum={actual_sum} "
                            f"(bits={bits_str}), Expected: carry={expected[0]}, sum={expected_sum}"
                        )
                except ValueError:
                    pass

        if score > weight:
            score = weight
        set_score(round(score, 2))
