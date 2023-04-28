# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also, please include simple test function to test the class methods.


class StringMethods:
    def __init__(self, input_value):
        input_value = ""

    def get_string(self):
        user_input = "testt"
        return user_input

    def print_string(self, input_value):
        if not input_value.isupper():
            print(input_value.upper())


class TestMethods(StringMethods):
    def test_the_methods(self):
        input_value = self.get_string()
        self.print_string(input_value)
