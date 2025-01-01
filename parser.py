import re


def parse(string) -> tuple:
    left_side, right_side = string.split('=')

    def parse_side(expression):
        criterium = re.compile(
            r'([-+]?\d*\.*\d*)\s*\*?\s*(x?)\^?(\d*)', re.IGNORECASE)
        poly = {}
        # signs = {'+': 1, '-': -1}
        for c, x, p, in criterium.findall(expression.replace(' ', '').replace('**', '^')):
            if not any((c, x, p)):
                continue
            if c in ('+', '-'):
                coeff = 1.0 if c == '+' else -1.0
            else:
                coeff = float(c) if '.' in c else int(c or 1)
            # coeff = signs[c] if c in ('+', '-') else int(c or 1)
            power = int(p or 1) if x else 0
            if power in poly:
                print(f"Same power, summing {poly[power]} and {coeff}")
                poly[power] += coeff
                continue
            poly[power] = coeff
        return poly
    left_poly = parse_side(left_side)
    right_poly = parse_side(right_side)
    return left_poly, right_poly


def format_equation(equation) -> str:
    """
    Format the equation dictionary into a readable string
    """
    terms = []
    for power, coeff in sorted(equation.items(), reverse=True):
        if coeff == 0:
            continue
        term = f"{coeff}" if power == 0 else f"{coeff}*X^{power}" if power > 1 else f"{coeff}*X"
        terms.append(term)
    return " + ".join(terms).replace("+ -", "- ")


def combine_sides(left_side, right_side) -> dict:
    """
    Combine terms from right_side into left_side
    Display intermediate steps
    """
    print("Combining sides of the equation:")
    print("Initial left side:", format_equation(left_side))
    print("Initial right side:", format_equation(right_side))
    for power in right_side:
        if power in left_side:
            print(
                f"For X^{power}: {left_side[power]} (from left side) - {right_side[power]} (from right side)"
            )
            left_side[power] -= right_side[power]
        else:
            print(
                f"For X^{power}: Adding -{right_side[power]} to the left side"
            )
            left_side[power] = -right_side[power]
    print("Resulting combined equation:", format_equation(left_side))
    return left_side
