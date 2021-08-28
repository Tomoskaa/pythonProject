
def calculator(x, op, y):

    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '**':
        return x ** y
    elif op == '/':
        return x / y
    elif op == '//':
        return x // y
    elif op == '%':
        return x % y
    else:
        return "Greshka"


if __name__ == '__main__':
    x = int(input())
    operator = input()
    y = int(input())

    print("Rezultat:", calculator(x, operator, y))