import math
from math_rand_package.math_problem import InvalidOperationError

class SolutionChecker:
    def check_solution(self,problem,user_solution):
        try:
            correct_solution = problem.solve()
            if isinstance(correct_solution, float):
                if math.isclose(user_solution, correct_solution, rel_tol=1e-5):
                    return f"Correct The solution to {problem} is approx {correct_solution}"
                else:
                    return f"Incorrect! The correct solution to {problem} is approx {correct_solution}"
            else:
                if user_solution == correct_solution:
                    return f"Correct! The solution to {problem} is approx {correct_solution}"
                else:
                    return f"Incorrect! The solution to {problem} is approx {correct_solution}"
        except InvalidOperationError as e:
            return f"Error: {str(e)}"
        