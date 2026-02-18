#!/bin/bash
echo "1 for setup, 2 for installation, 3 for running"
read input

if [ "$input" == "1" ]; then
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        exit
    fi
    exit
fi


if [ "$input" == "3" ]; then
    if [ ! -d ".venv" ]; then
        echo "dir doesnt exist"
        exit
    else
        echo "dir exist, activating enviroment"
        source ".venv/bin/activate"
    fi
fi
