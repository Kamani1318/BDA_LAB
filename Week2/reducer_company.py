#!/usr/bin/env python
import sys

current_company = None
total_salary = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    company, salary = line.split('\t')

    # Convert salary from string to int
    salary = int(salary)

    if current_company == company:
        total_salary += salary
        count += 1
    else:
        if current_company:
            # Print average salary for the previous company
            print(f'{current_company}\t{total_salary / count}')
        current_company = company
        total_salary = salary
        count = 1

# Don't forget to print the average salary for the last company
if current_company == company:
    print(f'{current_company}\t{total_salary / count}')
