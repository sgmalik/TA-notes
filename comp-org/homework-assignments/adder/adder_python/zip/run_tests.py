"""
"This python script loads and runs the tests using the JSONTestRunner class
from gradescope-utils. This produces the JSON formatted output to stdout,
which is then captured and uploaded by the autograder harness."

See: https://github.com/gradescope/autograder_samples/blob/master/python/src/run_tests.py

When running, working directory will be *autograder*
"""

import os
import unittest

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


results_path = '/autograder/results/results.json'
if os.environ.get('GS_LOCAL') == 'true':
    print("Running locally...")
    results_path = '../results/results.json'
else:
    results_path = '/autograder/results/results.json'

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open(results_path, 'w') as fh:
        JSONTestRunner(visibility='visible', stream=fh).run(suite)
