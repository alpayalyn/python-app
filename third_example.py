# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

x = range(2000, 3200)
list_of_numbers = []

for n in x:
    if n % 7 == 0 and n % 5 != 0:
        list_of_numbers.append(n)
print(list_of_numbers)
print(','.join(list_of_numbers))
