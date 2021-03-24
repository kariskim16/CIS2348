"""
Karis Kim
1624226
CIS 2348
"""
numbers = input().split()

noneg_int=[]


for num in numbers:

    # Convert the string number into integer.

    num = int(num)

    # Checks whether number is non-negative.

    if num >= 0:

        noneg_int.append(num)

noneg_int.sort()


for i in noneg_int:
    print(i,end=' ')