# The prime factors of 13 195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143

from math import sqrt

def smallest_divisors(num):
    # Let's say each num can represented by only 2 multipliers : -> num is prime
    # num = dev_1 * dev_2, but let's take dev_1 < dev_2: -> dev_1: small and dev_2: big

    small = 2 # the smallest possible devisor is 2
    i = 0
    while i < num // 2:         # No point in checking after the half point - basically after this point
                                # you cannot multiply by even the smallest prime to get num

        big = int(num / small)  # We define it here, because we want it to change value based on small
                                # based on small, which we change in the same loop
        if small * big == num:
            return small        # We check if small is a divisor essentially, because if small*big != num
                                # then num % small != 0
        i += 1
        small +=1
    
    return num                  # If we haven't found a divisor this means that num is prime 

# A more optimized version
def smallest_divisors(N):
    if N % 2 == 0:              # Removes the need for us to check with even divisors
        return 2
    small = 3
    while small <= int(N/small):
        if small * int(N/small) == N:
            return small
        
        small += 2              # We can now increment 2x faster
    return N

def smallest_divisors(n):
    if n % 2 == 0:
        return 2
    small = 3
    while small <= sqrt(n):      # small < N/small -> small*small < N -> small < sqrt(N)
        if small * int(n/small) == n:
            return small
        small += 2
    return n

def all_divisors(num):
    all_divisors = []
    
    while num > 1:
        all_divisors.append(smallest_divisors(num))
        num = num / smallest_divisors(num)

    return all_divisors

print (smallest_divisors(13195))
print (all_divisors(13195))
print (max(all_divisors(13195)))
print (max(all_divisors(600851475143)))


