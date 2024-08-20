from math_rand_package.problem_generator import ProblemGenerator
from math_rand_package.calculator import Calculator
from math_rand_package.solution_checker import SolutionChecker
from math_rand_package.math_problem import InvalidOperationError

def main():
    # Initialize objects
    generator = ProblemGenerator()
    calculator = Calculator()
    checker = SolutionChecker()

    # Demonstrate various math problems
    problems = [
        generator.generate_addition_problem(),
        generator.generate_subtraction_problem(),
        generator.generate_multiplication_problem(),
        generator.generate_division_problem()
    ]

    for problem in problems:
        print(f"Problem {problem}")

        try: 
            user_solution = float(input("Enter your solution: "))
            result = checker.check_solution(problem,user_solution)
            print(result)
        except InvalidOperationError as e:
            print(f"Error: {str(e)}")
        except NotImplementedError as y:
            print(f"Error: {str(y)}")

        except Exception as x:
            print(f"Caught an exception: {x}")
            print(f"Exception type: {type(x).__name__}")
        


main()