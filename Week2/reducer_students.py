# reducer.py
import sys

for line in sys.stdin:
    line = line.strip()
    name, data = line.split('\t', 1)

    # Output the data (already sorted by the Unix sort command)
    print(f'{name},{data}')

