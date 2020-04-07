#!/bin/bash

if [ "$1" = "compile" ] && [ $# -eq 1 ]
then
    echo "Installing dependencies"
    pip3 install --user -r ./resources/requirements.txt
elif [ "$1" = "start" ] && [ $# -eq 1 ]
then
    echo "Starting C45Bot"
    python3 ./src/__main__.py
elif [ "$1" = "test" ] && [ $# -eq 1 ]
then
    echo "Running tests on C45Bot"
    python3 -m unittest test/*_test.py
else
    echo "Usage: ./c45bot <command>"
    echo "Available commands:"
    echo " - compile"
    echo " - start"
    echo " - test"
fi