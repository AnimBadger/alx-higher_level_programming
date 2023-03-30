#!/bin/bash
#use curl to fetch methods from header

curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev