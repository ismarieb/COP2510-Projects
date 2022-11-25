# Driver: Ismarie Birriel
# Navigator: Lam Nguyen
# Program prompts user to enter grades which gets stored in a list
# and calculates mean and standard deviation of the list
import math

grades = []
new_grade = 0
n = 0
i = 0
total = 0
sdstep2 = 0
print('Enter class grades (-1 when finished): ')
while new_grade != -1 or new_grade > 0:
    new_grade = int(input())
    if new_grade < 0 and new_grade != -1:
        print('Undefined mean and standard deviation')
        new_grade = -1
    elif new_grade != -1:
        grades.append(new_grade)
        n = n + 1

if new_grade == -1:
    while i != n:
        total = total + grades[i]
        i = i + 1

    if n > 0:
        mean = total / n
        print(f'Mean: {mean}')
    i = 0

    while i != n:
        sdstep1 = (grades[i] - mean)**2
        sdstep2 = sdstep2 + sdstep1
        i = i + 1

    if n > 0:
        st_deviation = math.sqrt((1/n)*(sdstep2))
        print(f'Standard deviation: {st_deviation:.2f}')
