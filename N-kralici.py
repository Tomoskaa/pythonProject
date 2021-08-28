from constraint import *


def queens_attacking(q1, q2):
    if (abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])) or q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    return True


if __name__ == '__main__':

    problem = Problem(BacktrackingSolver())

    n = int(input())

    queens = range(1, n+1)

    domains = []
    for i in range(0, n):
        for j in range(0, n):
            domains.append((i, j))

    domains = [(row, col) for row in range(0, n) for col in range(0, n)]

    problem.addVariables(queens[0:], domains)

    for queen1 in queens:
        for queen2 in queens:
            if queen1 < queen2:
                problem.addConstraint(queens_attacking, (queen1, queen2))



    if n <= 6:
        solutions = problem.getSolutions()
        print(len(solutions))
    else:
        solution = problem.getSolution()
        print(solution)

