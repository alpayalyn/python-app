# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1.., Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0],
# [0, 1, 2, 3, 4],
# [0, 2, 4, 6, 8]]

# print("x verisini gireniz:")
# x = int(input())
# print("y verisini gireniz:")
# y = int(input())
# range(0, x)
# range(0, y)
# i = 0
# j = 0
# listing = [[],[]]
#
# for a in range(x):
#     m = i * j
#     listing[i][j] = m
#     j = j + 1
#     for b in range(y):
#         n = i * j
#         listing[i][j] = n
#         i = i + 1
# # #
# # #
# # #

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [y for x in fruits if "a" in x]

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# # #
# # #
# # #


# n = 4
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             a[i][j] = 0
#         elif i > j:
#             a[i][j] = 2
#         else:
#             a[i][j] = 1
# for row in a:
#     print(' '.join([str(elem) for elem in row]))
