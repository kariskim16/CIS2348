x = input().split()
person_name = x[0]
while person_name != '-1':
    try:
        person_age = int(x[1]) + 1
    except ValueError:
        person_age = 0
    print('{} {}'.format(person_name, person_age))

    x = input().split()
    person_name = x[0]