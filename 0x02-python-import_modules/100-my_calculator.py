#!/usr/bin/python3
import sys
import calculator_1
if __name__ == '__main__':
    n = len(sys.argv) - 1
    if (n != 3):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    opp = sys.argv[2]
    if (opp != '+' and opp != '-' and opp != '*' and opp != '/'):
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (opp == '+'):
        print('{} {} {} = {}'.format(a, opp, b, calculator_1.add(a, b)))
    elif (opp == '-'):
        print('{} {} {} = {}'.format(a, opp, b, calculator_1.sub(a, b)))
    elif (opp == '*'):
        print('{} {} {} = {}'.format(a, opp, b, calculator_1.mul(a, b)))
    else:
        print('{} {} {} = {}'.format(a, opp, b, calculator_1.div(a, b)))
