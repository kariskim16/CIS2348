cups_of_lemon = float(input("Enter amount of lemon juice (in cups): "))
cups_of_water = float(input("Enter amount of water (in cups): "))
cups_of_nectar = float(input("Enter amount of agave nectar (in cups): "))
servings = float(input("How many servings does this make?" ))


print('Lemonade ingredients - yields '+ str('{:.2f}'.format(serving))+' servings'
print(str('{:.2f}'.format(cups_of_lemon)) + ' cup(s) lemon juice')
print(str('{:.2f}'.format(cups_of_water))+ 'cup(s) water')
print(str('{:.2f}'.format(cups_of_nectar))+ 'cup(s) agave nectar')

diff_servings = float(input("How many servings would you to make?"))
serving_formula = diff_serving/servings
newjuice = cups_of_lemon * serving_formula
newwater = cups_of_water * serving_formula
newnectar = cups_of_nectar * serving_formula

print('Lemonade ingredients - yields '+ str('{:.2f}'.format(diff_servings))+' servings')
print(str('{:.2f}'.format(newjuice)) + 'cup(s) lemon juice')
print(str('{:.2f}'.format(newwater)) + 'cup(s) water')
print(str('{:.2f}'.format(newnectar)) + 'cup(s) agave nectar')

print('Lemonade ingredients - yields '+ str('{:.2f}'.format(diff_servings))+' servings')
print(str('{:.2f}'.format(newjuice/16)) + 'cup(s) lemon juice')
print(str('{:.2f}'.format(newwater/16)) + 'cup(s) water')
print(str('{:.2f}'.format(newnectar/16)) + 'cup(s) agave nectar')