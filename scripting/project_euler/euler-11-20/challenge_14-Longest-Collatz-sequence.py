# The following iterative sequence is defined for the set of positive integers:
        # n -> n/2 (n is even)
        # n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence
        # 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. ALthough it has been proved yet (Collatz Problem), it is thought that
# all starting numbers finish at 1

# Which starting number, under 1 mil, prodices the longest chain?

# NOTE Once the chain starts the terms are allowed to go above 1 million

LIMIT = 1 * 1000 * 1000 # 1 Mil

def collatz(n):
    while True:
        if n % 2 == 0:
            n = n/2
            yield n
        else:
            n = 3*n + 1
            yield n
i = 1
longest = 0
start = 0
while i < LIMIT:
    sequence = []
    gen = collatz(i)
    n = next(gen)
    sequence.append(n)
    while n > 1:
        n = next(gen)
        sequence.append(n)
    if len(sequence) > longest:
        longest = len(sequence)
        start = i
    # print('Start: {}, Sequence: {}, Lenght: {}'.format(i, sequence, len(sequence)))
    i += 1
print ('Longest lenght: {}, Started from: {}'.format(longest, start))
