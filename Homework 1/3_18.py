"""
Karis Kim
CIS 2348
1624226
"""
import math
color = {'red': 35, 'blue': 25, 'green': 23}

height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = height * width
paint_galloncover = 350
formula_gallon = area/paint_galloncover

print('Wall area:\n',area,'square feet')

print('Paint needed:\n','{:.2f}'.format(formula_gallon),'gallons')

gallon_can = math.ceil(formula_gallon)
print('Cans needed:\n',gallon_can,'can(s)')


while True:
    pick_color = input('Choose a color to paint the wall:\n')
    if (pick_color in color):
        break
    print (f"The available colors are: {list(color.keys())}")

print(f"Cost of purchasing {pick_color} paint: ${color[pick_color]}")


