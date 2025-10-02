#!/bin/zsh

echo "Setup..."
./setup_local.sh
echo "Autograde..."
./run_autograder_local.sh
echo "Tearing down..."
./teardown_local.sh
