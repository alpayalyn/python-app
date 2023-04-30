# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

list_of_numbers = list(range(1000, 3001))
end_list = []

for numbers in list_of_numbers:
    # splitted an index of the list to its' characters.
    number = [*str(numbers)]

    if int(number[0]) % 2 == 0 and int(number[1]) % 2 == 0 and int(number[2]) % 2 == 0 and int(number[3]) % 2 == 0:
        end_list.append(numbers)
    else:
        pass

# İkinci çözüm

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)