# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

class SquareRoot:
    def __init__(self, C: int = 50, H: int = 30, D: list = [1, 2, 3]):
        self.C = C
        self.H = H
        self.D = D

    def take_square_root(self, C, H, D):
        list_output = []
        for x in D:
            q = float((2 * self.C * x) / H)
            list_output.append(q)
        return list_output


input_value = [200, 400, 500]
square_root = SquareRoot(C=50, D=[80, 90, 100], H=100)
print(square_root.take_square_root())
