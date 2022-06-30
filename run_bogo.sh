#!/bin/bash
#compile with gcc bogo.c -o bogo -lm 

for run in {1..10}; do ./bogo 42 3 4 2 3 4 2 7 5 4 5 3 4 ; done
