# mapper.py
import sys

for line in sys.stdin:
    line = line.strip()
    reg_no, name, age, gender = line.split(',')

    # Emit the name as the key and the rest of the data as the value
    print(f'{name}\t{reg_no},{age},{gender}')

