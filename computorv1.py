import sys
import parser
import re


def check_syntax(expression):
    user_input = expression.split()
    for exp in user_input:
       print(f"input: {exp}")
    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: wrong number of arguments")
        sys.exit (1)
    valid_input = check_syntax(sys.argv[1])
    polynomial = parser.parse(valid_input);
