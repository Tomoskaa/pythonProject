from constraint import *

def konji_ogranicuvanje(k1, k2):
    if k1[0] == k2[0] and k1[1] == k2[1]:
        return False
    if k1[0] - 2 == k2[0] and k1[1] - 1 == k2[1]:
        return False
    if k1[0] - 2 == k2[0] and k1[1] + 1 == k2[1]:
        return False
    if k1[0] - 1 == k2[0] and k1[1] - 2 == k2[1]:
        return False
    if k1[0] - 1 == k2[0] and k1[1] + 2 == k2[1]:
        return False
    if k1[0] + 1 == k2[0] and k1[1] - 2 == k2[1]:
        return False
    if k1[0] + 1 == k2[0] and k1[1] + 2 == k2[1]:
        return False
    if k1[0] + 2 == k2[0] and k1[1] - 1 == k2[1]:
        return False
    if k1[0] + 2 == k2[0] and k1[1] + 1 == k2[1]:
        return False
    return True

if __name__ == "__main__":

    problem = Problem()

    n = int(input())

    variables = range(0, n)
    domains = []
    for i in range(0, n):
        for j in range(0, n):
            domains.append((i, j))
    domains = [(row, col) for row in range(0, n) for col in range(0, n)]

    problem.addVariables(variables, domains)

    for konj1 in variables:
        for konj2 in variables:
            if konj1 < konj2:
                problem.addConstraint(konji_ogranicuvanje, (konj1, konj2))

    if n <= 4:
        solutions = problem.getSolutions()
        print(len(solutions))
    else:
        solution = problem.getSolution()
        print(solution)