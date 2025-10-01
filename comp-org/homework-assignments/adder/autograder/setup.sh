#!/usr/bin/env bash

# "This script installs Python and the pip package manager. Then it uses
# pip to install our two external dependencies."
#
# See: https://github.com/gradescope/autograder_samples/blob/master/python/src/setup.sh

apt-get install -y python3 python3-pip python3-dev

pip3 install -r /autograder/source/requirements.txt

sudo apt-get install -y clang-format
sudo apt-get install -y clang-tidy
