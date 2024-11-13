import sys
import parser

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: wrong number of arguments")
        sys.exit (1)
    polynomial = parser.parse(sys.argv[1]);
