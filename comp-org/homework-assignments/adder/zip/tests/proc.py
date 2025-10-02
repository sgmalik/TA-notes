"""
Runners for submitted program and Flake8
"""
import subprocess
import sys

TIMEOUT = 15  # seconds
ENCODING = 'UTF8'

def run_flake8(submission, *, args: list[str], timeout=60, **kwargs):
    """Run Flake8 for checking conformance with PEP 8.
    Anything you print here, winds up in JSON output. """
    p = subprocess.run(
        ['flake8', *args, submission],
        capture_output=True,   # capture stdout, stderr
        timeout=timeout,
        encoding=ENCODING,
        **kwargs
    )

    if p.returncode == 1:
        print(f'Deviations from PEP 8: \n{p.stdout}\n',
              file=sys.stderr)
    else:
        print('Submission conforms to PEP 8.')

    return p

