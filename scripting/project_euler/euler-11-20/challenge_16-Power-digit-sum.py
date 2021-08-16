# 2**15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26
# What is the sum of the digits of the number 2**1000

def digit_sum (num):
    num = str(num)
    result = 0
    for i in num: 
        result += int(i)
    return result

print (digit_sum(pow(2, 1000)))
