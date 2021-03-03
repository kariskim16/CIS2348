create_password = input()

"""
Karis Kim
CIS 2348
1624226
"""
new_password = ''

i = 0
while i < len(create_password):
    ch = create_password[i]
    if ch == 'i':
        new_password += '!'
    elif ch == 'a':
        new_password += '@'
    elif ch == 'm':
        new_password += 'M'
    elif ch == 'B':
        new_password += '8'
    elif ch == 'o':
        new_password += '.'
    else:
        new_password += ch
    i += 1

new_password += "q*s"

print(new_password)