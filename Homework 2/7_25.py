"""
Karis Kim
CIS 2348
1624226
"""
def exact_change(user_total):
    numdollars = user_total // 100
    user_total %= 100
    numquarters = user_total // 25
    user_total %= 25
    numdimes = user_total // 10
    user_total %= 10
    numnickels = user_total // 5
    user_total %= 5
    numpennies = user_total
    return numdollars, numquarters, numdimes, numnickels, numpennies
def main():
    inputval = int(input())
    numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(inputval)
    if inputval <= 0:
        print('no change')
    else:
        if numdollars > 1:
            print('%d dollars' % numdollars)
        elif numdollars == 1:
            print('%d dollar' % numdollars)

        if numquarters > 1:
            print('%d quarters' % numquarters)
        elif numquarters == 1:
            print('%d quarter' % numquarters)

        if numdimes > 1:
            print('%d dimes' % numdimes)
        elif numdimes == 1:
            print('%d dime' % numdimes)

        if numnickels > 1:
            print('%d nickels' % numnickels)
        elif numnickels == 1:
            print('%d nickel' % numnickels)

        if numpennies > 1:
            print('%d pennies' % numpennies)
        elif numpennies == 1:
            print('%d penny' % numpennies)
if __name__ == '__main__':
    main()