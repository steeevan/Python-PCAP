class InvalidOperationError(Exception):
    ''' Custom Exception for invalid math operations
    '''


class MathProblem:
    def __init__(self, operand1, operand2, operator) -> None:
        self._operand1 = operand1
        self._operand2 = operand2
        self._operator = operator
        self._solution = None  # Encapsulation attribute for solution

    def get_opearnds(self):
        return self._operand1, self._operand2
    
    def get_operation(self):
        return self._operator
    
    def set_solution(self,solution):
        self._solution = solution
    
    def get_solution(self):
        if self._solution is None:
            raise InvalidOperationError("Solution has not been calculated yet.")
        return self._solution
    
    def solve(self):
        '''To be implemented by subclass'''
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self) -> str:
        return f"{self._operand1} {self._operator} {self._operand2}"
