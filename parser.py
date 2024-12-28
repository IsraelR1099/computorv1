import re


def parse(string):
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
    # print(f"left poly is: {left_poly}")
    right_poly = parse_side(right_side)
    # print(f"right poly is: {right_poly}")
    return left_poly, right_poly


def combine_sides(left_side, right_side):
    for power in right_side:
        if power in left_side:
            left_side[power] -= right_side[power]
        else:
            left_side[power] = -right_side[power]
    print(f"left side: {left_side}")
    return left_side
