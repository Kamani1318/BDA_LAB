#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    year, temperature = line.split('\t')

    # Emit the year as the key and the temperature as the value
    print(f'{year}\t{temperature}')

