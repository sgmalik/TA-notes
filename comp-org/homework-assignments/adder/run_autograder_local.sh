export GS_LOCAL='true'

set -e 

if [[ -f autograder/submission/ripple.py ]]; then
    echo "Python submission detected: copying ripple.py"
    cp autograder/submission/ripple.py autograder/source/ripple.py
elif [[ -f autograder/submission/ripple.c ]]; then
    echo "C submission detected: copying ripple.c"
    cp autograder/submission/ripple.c autograder/source/ripple.c
else
  exit 1
fi 

cd ./autograder/source

python3 run_tests.py

cd .. && cat results/results.json

