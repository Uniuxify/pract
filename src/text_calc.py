class Clac:
    def __init__(self):
        pass

    def _parse(self, expr):
        if '+' in expr:
            op = '+'
        elif '-' in expr:
            op = '-'
        elif '*' in expr:
            op = '*'
        else:
            op = '/'

        a, b = expr.split(op)
        return a, op, b

    def calc(self, expr):
        a, op, b = self._parse(expr)
        if op == '+':
            return a + b
        if op == '*':
            return a * b
        if op == '/':
            return a / b
        if op == '-':
            return a - b


def main():
    pass


if __name__ == '__main__':
    main()
