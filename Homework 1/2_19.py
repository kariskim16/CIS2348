"""
Karis Kim
CIS 2348
1624226
"""
cups_of_lemon = float(input("Enter amount of lemon juice (in cups): "))
cups_of_water = float(input("Enter amount of water (in cups): "))
cups_of_nectar = float(input("Enter amount of agave nectar (in cups): "))
servings = float(input("How many servings does this make?" ))

print('Lemonade ingredients - yields '+ '{:.2f}'.format(servings))+' servings'
print(f'{cups_of_lemon:.2f} cup(s) lemon juice')
print(f'{cups_of_water:.2f} cup(s) lemon juice')
print(f'{cups_of_nectar:.2f} cup(s) lemon juice')

diff_servings = float(input("How many servings would you to make?"))
serving_formula = diff_servings/servings
newjuice = cups_of_lemon * serving_formula
newwater = cups_of_water * serving_formula
newnectar = cups_of_nectar * serving_formula

print('Lemonade ingredients - yields '+ '{:.2f}'.format(diff_servings))+' servings'
print(f'{newjuice:.2f} cup(s) lemon juice')
print(f'{newwater:.2f} cup(s) water')
print(f'{newnectar:.2f} cup(s) agave nectar')

print('Lemonade ingredients - yields '+ '{:.2f}'.format(diff_servings))+' servings'
print('{:.2f}'.format(newjuice/16) + ' gallon(s) lemon juice')
print('{:.2f}'.format(newwater/16) + ' gallon(s) water')
print('{:.2f}'.format(newnectar/16) + ' gallon(s) agave nectar')

