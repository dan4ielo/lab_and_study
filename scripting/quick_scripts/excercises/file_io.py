import sys

#f = open(sys.argv[1], mode = 'rt', encoding = 'utf-8')
#for line in f:
#    print (line)
#for line in f:
#    sys.stdout.write(line)
#f.close()

from itertools import count, islice

#def sequence():
#    '''Generate Recaman's sequendce'''
#    seen = set()
#    a = 0
#    for n in count(1):
#        yield a
#        seen.add(a)
#        c = a - n
#        if c < 0 or c in seen:
#            c = a + n
#        a = c
#
#def write_sequence(filename, num):
#    '''Write Recaman's sequence to a text file.'''
#    try:
#        f = open(filename, mode = 'wt', encoding = 'utf-8')
#        f.writelines(f"{r}\n" for r in islice (sequence(), num +1))
#    finally:
#        f.close()
#
#def read_series(filename):
#    try:
#        f = open(filename, mode = 'rt', encoding='utf-8')
#        return [int(line.strip()) for line in f]
#    finally:
#        f.close()

# The write_sequence function utilizing the with-block
#def write_sequence(filename, num):
#    with open(filename, mode = 'wt', encoding = 'utf-8') as f:
#        f.writelines(f"{r}\n" for r in islice(sequence(), num + 1))
#
## The read_series function but usint the with-block
#def read_series(filename):
#    with open(filename, mode = 'rt', encoding = 'utf-8') as f:
#        return [int(line.strip()) for line in f]
#
#def main(filename):
#    series = read_series(filename)
#    print (series)
#
#if __name__ == '__main__':
#    #write_sequence(filename = sys.argv[1],
#                   #num = int(sys.argv[2]))
#    main(sys.argv[1])

# Demonstrating Binary File handling
# Look at BMP Writer 
