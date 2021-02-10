"""
Karis Kim
CIS 2348
1624226
"""
print('Birthday Calculator')
print('Current Day')

currentMonth = int(input('Month: '))
currentDay = int(input('Day: '))
currentYear = int(input('Year: '))

print('Birthday')
bdayMonth = int(input('Month: '))
bdayDay = int(input('Day: '))
bdayYear = int(input('Year: '))

ageformula = currentYear - bdayYear

# if today's month and day >= birthday's month and day, then current year - birthyear, works.
# Otherwise, we have to subtract 1 from the age.
if currentMonth < bdayMonth:
    ageformula -= 1
elif currentMonth == bdayMonth and bdayDay > currentDay:
    ageformula -= 1

print('You are',ageformula, 'years old.')

if currentMonth == bdayMonth and currentDay == bdayDay:
  print("Happy Birthday!")