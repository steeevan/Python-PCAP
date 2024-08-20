import math
from math_rand_package.math_problem import InvalidOperationError

class Calculator:
    def calculate_square_root(self, number):
        if number < 0:
            raise InvalidOperationError("Cannot calculate the suqare root of negative number")
        return math.sqrt(number)
    
    def calculate_pow(self, base, exponent):
        return math.pow(base,exponent)
    def calculate_log(self,number, base = math.e):
        if number <= 0:
            raise InvalidOperationError("Cannot calculate logarith of a non-positive number")
        return math.log(number,base)

    def calculate_factorial(self,number):
        if number < 0:
            raise InvalidOperationError("Cannot calculate factorial of a negative-number")
        return math.factorial(number)
    def calculate_triogonometry(self, angle, function ='sin'):
        functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan
        }

        if function not in functions:
            raise InvalidOperationError(f"Invalid trigonometric Function {function}")
        return functions[function](math.radians(angle))
    