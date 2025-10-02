export GS_LOCAL='true'

cp ./autograder/submission/ripple.py ./autograder/source/ripple.py

cd ./autograder/source

python3 run_tests.py

cd .. && cat results/results.json

