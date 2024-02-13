#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    company, salary = line.split('\t')

    # Emit the company name as the key and the salary as the value
    print(f'{company}\t{salary}')
