# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
# they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# 1111,1010,1000

s = input()
digit_list = [digits for digits in s.split(",")]
digit_numbers_list_total = 0

for digits in digit_list:
    digit_numbers = [int(digits[0]) * 1 + int(digits[1]) * 2 + int(digits[2]) * 4 + int(digits[3]) * 8 for digits in
                     digits.split()]

    digit_numbers_list = digit_numbers.pop(digit_numbers[0])
    digit_numbers_list_total = digit_numbers_list_total + digit_numbers_list

# Diğer Çözüm

value = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        value.append(p)
