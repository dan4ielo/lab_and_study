# If the numbers 1 to 5 are written out in words: one, two, three, four, five
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?

# NOTE Do not count spaces or hyphens. Ex. 342 (Three hundred and dourty-two) contains
# 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 'and'
# when writing out numbers is in complience with the British language

def num_to_letter(num):
    string = ''
    while num > 0:
        #===================================#
        # num = 1000
        #===================================#
        if num == 1000:
            string += 'one thousand'
            num -= 1000
        if num >= 900 and num < 1000:
            string += 'nine hundred and '
            num -= (num // 100) * 100
        if num >= 800 and num < 900:
            string += 'eight hundred and '
            num -= (num // 100) * 100
        if num >= 700 and num < 800:
            string += 'seven hundred and '
            num -= (num // 100) * 100
        if num >= 600 and num < 700:
            string += 'six hundred and '
            num -= (num // 100) * 100
        if num >= 500 and num < 600:
            string += 'five hundred and '
            num -= (num // 100) * 100
        if num >= 400 and num < 500:
            string += 'four hundred and '
            num -= (num // 100) * 100
        if num >= 300 and num < 400:
            string += 'three hundred and '
            num -= (num // 100) * 100
        if num >= 200 and num < 300:
            string += 'two hundred and '
            num -= (num // 100) * 100
        if num >= 100 and num < 200:
            string += 'one hundred and '
            num -= (num // 100) * 100
        #===================================#
        # num between 10 and 100
        #===================================#
        if num >= 90 and num < 100:
            string += 'ninety-'
            num -= (num // 10) * 10
        if num >= 80 and num < 90:
            string += 'eighty-'
            num -= (num // 10) * 10
        if num >= 70 and num < 90:
            string += 'seventy-'
            num -= (num // 10) * 10
        if num >= 60 and num < 90:
            string += 'sixty-'
            num -= (num // 10) * 10
        if num >= 50 and num < 90:
            string += 'fifty-'
            num -= (num // 10) * 10
        if num >= 40 and num < 90:
            string += 'forty-'
            num -= (num // 10) * 10
        if num >= 30 and num < 90:
            string += 'thirty-'
            num -= (num // 10) * 10
        if num >= 20 and num < 90:
            string += 'twenty-'
            num -= (num // 10) * 10
        if num == 19:
            string += 'nineteen'
            num -= num
        if num == 18:
            string += 'eighteen'
            num -= num
        if num == 17:
            string += 'seventeen'
            num -= num
        if num == 16:
            string += 'sixteen'
            num -= num
        if num == 15:
            string += 'fifteen'
            num -= num
        if num == 14:
            string += 'fourteen'
            num -= num
        if num == 13:
            string += 'thirteen'
            num -= num
        if num == 12:
            string += 'twelve'
            num -= num
        if num == 11:
            string += 'eleven'
            num -= num
        #===================================#
        # num between 1 and 10
        #===================================#
        if num == 10:
            string += 'ten'
            num -= num
        if num == 9:
            string += 'nine'
            num -= num
        if num == 8:
            string += 'eight'
            num -= num
        if num == 7:
            string += 'seven'
            num -= num
        if num == 6:
            string += 'six'
            num -= num
        if num == 5:
            string += 'five'
            num -= num
        if num == 4:
            string += 'four'
            num -= num
        if num == 3:
            string += 'three'
            num -= num
        if num == 2:
            string += 'two'
            num -= num
        if num == 1:
            string += 'one'
            num -= num
    return string

def letter_count(string):
    string = string.replace(' ', '')
    string = string.replace('-', '')
    # print(string)
    return len(string)

# test = input('> ')

# print (num_to_letter(int(test)))
# print (letter_count(num_to_letter(int(test))))

i = 1
result = 0
while i <= 1000:
    # print (num_to_letter(i))
    # print (letter_count(num_to_letter(i)))
    result += letter_count(num_to_letter(i))
    i += 1
print (result)
