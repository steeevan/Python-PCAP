import random
from math_rand_package.math_problem import MathProblem
from math_rand_package.math_problem import InvalidOperationError

class AdditionProblem(MathProblem):
    def solve(self):
        self.set_solution(self._operand1 + self._operand2)
        return self.get_solution()
    
class SubtractionProblem(MathProblem):
    def solve(self):
        self.set_solution(self._operand1 - self._operand2)
        return self.get_solution()
 
class MultiplicationProblem(MathProblem):
    def solve(self):
        self.set_solution(self._operand1 * self._operand2)
        return self.get_solution()

class DivisionProblem(MathProblem):
    def solve(self):
        if self._operand2 == 0:
            raise InvalidOperationError("Division by zero is undefined")
        self.set_solution(self._operand1 / self._operand2)
        return self.get_solution()
    
class ProblemGenerator:
    def __init__(self,min = 1, max = 100) -> None:
        self.min = min
        self.max = max
    def generate_operands(self):
        a = random.randint(self.min,self.max)
        b = random.randint(self.min,self.max)
        return a,b
    def generate_addition_problem(self):
        a,b = self.generate_operands()
        return AdditionProblem(a,b,'+')
    
    def generate_subtraction_problem(self):
        a, b = self.generate_operands()
        return SubtractionProblem(a, b, '-')

    def generate_multiplication_problem(self):
        a, b = self.generate_operands()
        return MultiplicationProblem(a, b, '*')

    def generate_division_problem(self):
        a, b = self.generate_operands()
        return DivisionProblem(a, b, '/')