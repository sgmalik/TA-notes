import subprocess
import re
from pathlib import Path
import unittest
from proc import run_flake8
from gradescope_utils.autograder_utils.decorators import partial_credit


# TIMEOUT = 30 # seconds, not used yet
ENCODING = "UTF8"

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
    target_file = None
    target_file_present = False
    passing = True
    messages = []
    mode = None  # python or C

    @classmethod
    def setUpClass(cls):
        """run by autograder"""
        if Path("ripple.py").is_file():
            cls.mode = "py"
            cls.target_file = "ripple.py"
            cls.target_file_present = True
        elif Path("ripple.c").is_file():
            cls.mode = "c"
            cls.target_file = "ripple.c"
            cls.target_file_present = True
        else:
            cls.passing = False
            cls.messages.append(
                "Expected either ripple.py or ripple.c but found neither"
            )
            return
        if cls.mode == "c":
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
                    cls.ok = False
                    cls.messages.append("C compilation failed:")
                    cls.messages.append(result.stderr.strip())
            except Exception as e:
                cls.ok = False
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

    # Ignoring parse output functionality, should be able to assert based on constant
    @staticmethod
    def parse_output(data):
        chunks = re.split(r"\:\s|\n", data)
        return [chunk for chunk in chunks if chunk != ""]

    @partial_credit(12)
    def test_full_adder(self, set_score):
        """Testing Full_adder(a, b, c_in) functionality"""
        score = 0

        if self.mode == "py":
            import ripple

            for _, test in enumerate(FULL_ADDER_TESTS):
                arguments, expected = test
                actual = ripple.full_adder(*arguments)
                if expected == actual:
                    score += 1
                else:
                    print(
                        f"On input {arguments}, expected: {expected} Actual: {actual}"
                    )
        elif self.mode == "c":
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
                            score += 1
                    except ValueError:
                        continue

        set_score(score)

    @partial_credit(12)
    def test_ripple_carry(self, set_score):
        score = 0
        weight = 12
        num_tests = len(RIPPLE_CARRY_TESTS)

        if self.mode == "py":
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

        elif self.mode == "c":
            for args, expected in RIPPLE_CARRY_TESTS:
                result = subprocess.run(
                    ["./ripple", str(args[0]), str(args[1])],
                    capture_output=True,
                    text=True,
                    timeout=2,
                )
                lines = result.stdout.strip().splitlines()
                try:
                    for line in lines:
                        if "carry" in line and "Decimal" in line:
                            parts = line.split("=")[-1].split("carry")
                            sum_bits = int(parts[0].strip())
                            carry_out = int(parts[1].strip().replace(".", ""))
                            expected_sum = int("".join(str(b) for b in expected[1]), 2)
                            if sum_bits == expected_sum and carry_out == expected[0]:
                                score += weight / num_tests
                except Exception:
                    continue

        if score > weight:
            score = weight
        set_score(round(score, 2))

    @partial_credit(-10)
    def test_styling(self, set_score):
        score = 0
        if self.mode == "py":
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
        elif self.mode == "c":
            try:
                output = subprocess.run(
                    [
                        "clang-format",
                        "--dry-run",
                        "--Werror",
                        "-style=file",
                        "-assume-filename=autograder/.clang-format",
                        "ripple.c",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=5,
                )
                if output.returncode != 0:
                    violations = output.stderr.count("error:")
                    print(f"Violations with Clang detected:\n {output.stderr}")
                    score = -min(10, violations * 0.5)

                # Check linting with clang-tidy
                tidy_output = subprocess.run(
                    [
                        "clang-tidy",
                        "ripple.c",
                        "--quiet",
                        "--",
                        "-std=c99",
                        "-Wall",
                        "-Wextra",
                        "-pedantic",
                        "-isysroot",
                        subprocess.check_output(["xcrun", "--show-sdk-path"])
                        .decode()
                        .strip(),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10,
                )

                if tidy_output.returncode != 0:
                    warn_cnt = tidy_output.stdout.count("warning:")
                    err_cnt = tidy_output.stdout.count("error:")
                    print(f"clang-tidy diagnostics:\n{tidy_output.stdout}")
                    score += -min(10, (warn_cnt + err_cnt) * 0.5)

            except Exception as e:
                print(f"Clang formatting check failed: {e}")
                score -= 10
        else:
            print("Unrecognized language")
            score -= 10
        set_score(round(score, 2))
