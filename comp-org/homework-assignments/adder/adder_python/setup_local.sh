#!/bin/zsh

mkdir autograder
mkdir autograder/source
mkdir autograder/submission
mkdir autograder/results
touch autograder/results/results.json
mkdir autograder/tests
cp -r zip/* autograder/source/
cp -r zip/tests/* autograder/tests/
cp -r student/* autograder/submission/
