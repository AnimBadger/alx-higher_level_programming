#!/bin/bash
# use curl to pass parameters
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
