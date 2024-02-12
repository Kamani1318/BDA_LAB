#!/usr/bin/env python

import sys
a={}
b={}
for line in sys.stdin:
	line=line.strip()
	key,value=line.split('\t')
	v=value.split(',')
	if key=='a':
		a[(int(v[1]),int(v[2]))]=int(v[3])
	elif key=='b':
		b[(int(v[1]),int(v[2]))]=int(v[3])

print("The first matix is")
for i in range(0,3):
	for j in range(0,3):
		print("{0} ".format(a[(i,j)]))
	print("\n")

print("The second matix is")
for i in range(0,3):
        for j in range(0,3):
                print("{0} ".format(b[(i,j)]))
        print("\n")


result=0
for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			result=result + a[(i,k)]*b[(k,j)]
		print('({0},{1})\t{2}'.format(i,j,result))
		result=0
