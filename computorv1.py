import sys
import parser
import re


def check_syntax(expression):
    try:
        left, right = expression.split('=')
    except ValueError:
        print("Error: invalid input")
        sys.exit(1)

    def check_side(side):
        ret = re.fullmatch(
            r'^([-+]?\d*(\.\d+)?\*?[xX](\^\d+)?|[-+]?\d+(\.\d+)?)([-+]\d*(\.\d+)?\*?[xX](\^\d+)?|[-+]?\d+(\.\d+)?)*$',
            side.replace(' ', '').replace('**', '^'))
        if not ret:
            print("Error: invalid input")
            sys.exit(1)
        return side
    left = check_side(left)
    right = check_side(right)
    if 'x' not in left.lower() and 'x' not in right.lower():
        print(
            "Error: invalid input - equation must at least one variable term"
        )
        sys.exit(1)
    return expression


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: wrong number of arguments")
        sys.exit(1)
    valid_input = check_syntax(sys.argv[1])
    left_side, right_side = parser.parse(valid_input)
    print(f"left side: {left_side}")
    print(f"right side: {right_side}")
    parser.combine_sides(left_side, right_side)
