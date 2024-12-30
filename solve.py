import sys
from fractions import Fraction


def print_simplified(equation):
    """
    Print a simplified version of the equation.
    """
    terms = []
    degree = None
    for power, coeff in sorted(equation.items(), reverse=True):
        if coeff == 0:
            continue
        if degree is None or power > degree:
            degree = power
        if power == 0:
            if coeff > 0:
                terms.append(f"+ {coeff}")
            else:
                terms.append(f"{coeff}")
        elif power == 1:
            if coeff == 1:
                terms.append("X")
            elif coeff == -1:
                terms.append("-X")
            else:
                terms.append(f"+ {coeff} * X")
        else:
            if coeff == 1:
                terms.append(f"X^{power}")
            elif coeff == -1:
                terms.append(f"-X^{power}")
            else:
                terms.append(f"{coeff} * X^{power}")
    simplified_equation = " ".join(f"{term}" if not term.startswith("-") else
                                   term for term in terms)
    if simplified_equation.startswith("+"):
        simplified_equation = simplified_equation[2:]
    print(f"The reduced form is: {simplified_equation} = 0")
    print(f"Degree of the equation: {degree if degree is not None else 0}")


def print_result(result):
    """
    Print the result of the equation.
    """
    if result.is_integer():
        print(int(result))
    else:
        print(f"{result:.2f}")
        print(
            f"solution: {result:.2f} and {Fraction(result).limit_denominator()}"
        )


def solve_degree_1(equation):
    """
    Solve a polynomial equation of degree 1.
    """
    a = equation[1]
    b = equation[0]
    if a == 0:
        print("The solution is:")
        print("0")
    else:
        print("The solution is:")
        result = -b / a
        print_result(result)


def solve_degree_2(equation):
    """
    Solve a polynomial equation of degree 2.
    """
    sorted_equation = sorted(equation.items(), reverse=True)
    a, b, c = 0, 0, 0
    if len(sorted_equation) > 0:
        if 2 in sorted_equation[0]:
            a = sorted_equation[0][1]
    if len(sorted_equation) == 2:
        if 1 in sorted_equation[1]:
            b = sorted_equation[1][1]
        elif 0 in sorted_equation[1]:
            c = sorted_equation[1][1]
    if len(sorted_equation) == 3:
        if 1 in sorted_equation[1]:
            b = sorted_equation[1][1]
        elif 0 in sorted_equation[1]:
            c = sorted_equation[1][1]
        if 0 in sorted_equation[2]:
            c = sorted_equation[2][1]
    print(f"a = {a}, b = {b}, c = {c}")
    quadratic = (b * b) - (4 * a * c)
    if quadratic < 0:
        print("Discriminant is strictly negative, the two solutions are:")
        print(f"(-{b} + i√{-quadratic}) / {2 * a}")
        print(f"(-{b} - i√{-quadratic}) / {2 * a}")
        sys.exit(0)
    if a == 0:
        print("The solution is:")
        print(-c / b)
        sys.exit(0)
    x = (-b + (quadratic ** 0.5)) / (2 * a)
    y = (-b - (quadratic ** 0.5)) / (2 * a)
    print("Discriminant is strictly positive, the two solutions are:")
    print_result(x)
    print_result(y)


def solve(equation):
    """
    Solve a polynomial equation of degree 2 or less.
    """
    degree = max(equation.keys())
    if degree > 2:
        print(
            "The polynomial degree is stricly greater than 2, I can't solve."
        )
        sys.exit(1)

    print_simplified(equation)
    if degree == 2:
        solve_degree_2(equation)
    elif degree == 1:
        solve_degree_1(equation)
    else:
        if equation[0] == 0:
            print("Any real number is a solution.")
        else:
            print("There is no solution.")
