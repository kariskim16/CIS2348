"""
Karis Kim
CIS 2348
1624226
"""
a1 = int(input())
b2 = int(input())
c3 = int(input())

a1 = int(input())
b2 = int(input())
c3 = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
            print(x, y)
            solution_found = True

if not solution_found:
    print("No solution")