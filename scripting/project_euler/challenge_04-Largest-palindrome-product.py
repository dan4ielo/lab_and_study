# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2 digit numbers is 9009 = 91 * 90.
# Find the largest palindrome made from the produc of two 3 difit numbers.

def is_palindrome(num):
    num = list(str(num))
    if len(num) % 2 == 0:
        for i in range(int(len(num) / 2)):
            if num[i] != num[-i - 1]:
                return False
        return True
    else:
        return False

# generate list of numbers from 800 to 999
mul_one = [_ for _ in range(800, 1000)]
mul_two = [_ for _ in range(800, 1000)]

big_palindromes = []

for m1 in mul_one:
    for m2 in mul_two:
        num = m1 * m2
        if is_palindrome(num):
            big_palindromes.append(num)
        else:
            continue

print (big_palindromes)
print (max(big_palindromes))

# print (max(big_palindromes = [m1*m2 for m1 in mul_one for m2 in mul_two if is_palindrome(m1*m2)])) # welp worth a try :D
