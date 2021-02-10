"""
Karis Kim
CIS 2348
1624226
"""
cups_of_lemon = float(input("Enter amount of lemon juice (in cups):\n")) #part 1
cups_of_water = float(input('Enter amount of water (in cups):\n'))
cups_of_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))

print('\nLemonade ingredients - yields '+ '{:.2f}'.format(servings))+' servings'
print(f'{cups_of_lemon:.2f} cup(s) lemon juice')
print(f'{cups_of_water:.2f} cup(s) lemon juice')
print(f'{cups_of_nectar:.2f} cup(s) lemon juice')

diff_servings = float(input("\nHow many servings would you to make?\n")) #part 2

print('\nLemonade ingredients - yields {:.2f} servings'.format(diff_servings))
print('{:.2f} cup(s) lemon juice'.format(cups_of_lemon * diff_servings / servings))
print('{:.2f} cup(s) water'.format(cups_of_water * diff_servings / servings))
print('{:.2f} cup(s) agave nectar'.format(cups_of_nectar * diff_servings / servings))

print('\nLemonade ingredients - yields {:.2f} servings'.format(diff_servings))#part 3
print('{:.2f} gallon(s) lemon juice'.format(cups_of_lemon * diff_servings / servings / 16))
print('{:.2f} gallon(s) water'.format(cups_of_water * diff_servings / servings / 16))

