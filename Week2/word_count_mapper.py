import sys
for line in sys.stdin:
        #remove the leading and trailing whitespaces
        line = line.strip()
        #split the line into words
        words = line.split()
        #increase counters
        for word in words:
                print('%s\t%s' % (word,1))
