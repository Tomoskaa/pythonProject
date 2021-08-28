from constraint import *


def solve(solver):
    if solver == "BacktrackingSolver":
        problem = Problem(BacktrackingSolver())
    elif solver == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    elif solver == "MinConflictsSolver":
        problem = Problem(MinConflictsSolver())

    # Definiram vrednosti koi moze da se vnesuvaat
    variables = range(1, 10)
    maxVariables = range(81)
    problem.addVariables(maxVariables, variables)

    # Za sekoja redica definiram razlicna vrednost
    for i in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), range(i * 9, i * 9 + 9))

    # Za sekoja kolona definiram razlicna vrednost
    for i in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), range(i, 80 + i, 9))

    # Za sekoj blok definiram razlicna vrednost
    problem.addConstraint(AllDifferentConstraint(), [0, 1, 2, 9, 10, 11, 18, 19, 20])
    problem.addConstraint(AllDifferentConstraint(), [3, 4, 5, 12, 13, 14, 21, 22, 23])
    problem.addConstraint(AllDifferentConstraint(), [6, 7, 8, 15, 16, 17, 24, 25, 26])
    problem.addConstraint(AllDifferentConstraint(), [27, 28, 29, 36, 37, 38, 45, 46, 47])
    problem.addConstraint(AllDifferentConstraint(), [30, 31, 32, 39, 40, 41, 48, 49, 50])
    problem.addConstraint(AllDifferentConstraint(), [33, 34, 35, 42, 43, 44, 51, 52, 53])
    problem.addConstraint(AllDifferentConstraint(), [54, 55, 56, 63, 64, 65, 72, 73, 74])
    problem.addConstraint(AllDifferentConstraint(), [57, 58, 59, 66, 67, 68, 75, 76, 77])
    problem.addConstraint(AllDifferentConstraint(), [60, 61, 62, 69, 70, 71, 78, 79, 80])

    solution = problem.getSolution()

    return solution


if __name__ == "__main__":
    n = input()
    solution = solve(n)
    print(solution)