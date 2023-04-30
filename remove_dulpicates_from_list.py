# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all
# duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world


input_written = "alpay onurcan kadir cuneyd cuneyd cuneyd"
list_written = input_written.split(" ")
mylist = list(dict.fromkeys(list_written))
print(mylist)

##############-----############
items = [x for x in input().split(',')]
items.sort()
thing_to_print = ','.join(items)
print(thing_to_print)
##############-----############

# how to create a list by getting an input

s = input()
words = [word for word in s.split(" ")]
thing_to_print = " ".join(sorted(list(set(words))))
print(thing_to_print)
