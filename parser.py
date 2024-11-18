import re


def parse(string):
    print(f"input is: {string}")
    left_side, right_side = string.split('=')

    def parse_side(expression):
        print(f"expression in parse side {expression}")
        criterium = re.compile(r'([-+]?\d*)\s*\*?\s*(x?)\^?(\d*)')
        poly = {}
        signs = {'+': 1, '-': -1}
        for c, x, p, in criterium.findall(expression.replace(' ', '').replace('**', '^')):
            if not any((c, x, p)):
                continue
            coeff = signs[c] if c in ('+', '-') else int(c or 1)
            power = int(p or 1) if x else 0
            print(f"coeff is {coeff} and power {power}")
            if power in poly:
                poly[power] += coeff
                continue
            poly[power] = coeff
        print(f"poly is {poly}")
        return poly
    left_poly = parse_side(left_side)
    print(f"left poly is: {left_poly}")
    right_poly = parse_side(right_side)
    print(f"right poly is: {right_poly}")
