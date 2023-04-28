# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


_input = 6
t = range(1, _input)
y = []
i = 1
output = 1

for x in t:
    y.append(x)
for x in y:
    output = output * y[i - 1]
    i = i + 1

print(output)

