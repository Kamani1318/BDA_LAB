#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    year, temperature = line.split('\t', 1)

    # Output the year and temperature
    print(f'{year}\t{temperature}')

