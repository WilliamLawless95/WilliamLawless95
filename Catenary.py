# This Python script solves the 'Hanging Cable Problem' featured as an Amazon interview question.

# The script prompts the user to enter the length of a hanging cable,
# The height of each of the two towers between which the cable hangs, and
# The height of the cable at its lowest point.

# The output will be the distance between the two towers.

# Import the math library.
import math

# Import the name and system modules from the os library.
from os import name, system

# This function clears the screen for the user to see the output more clearly.


def clear():
    if name == 'nt':    # Windows Operating Systems
        _ = system('cls')
    else:               # MacOS and Linux Operating Systems
        _ = system('clear')


# Prompt the user to enter the length of the cable (in meters).
length = float(input('Please enter the length of the cable (m): '))
if length < 0:  # The cable cannot be of a negative length.
    length = abs(length)

# Prompt the user to enter the height of the first tower (in meters).
tower1 = float(input('Please enter the height of the first tower (m): '))
if tower1 < 0:  # The tower cannot be of a negative height.
    tower1 = abs(tower1)
    
# Prompt the user to enter the height of the first tower (in meters).
tower2 = float(input('Please enter the height of the second tower (m): '))
if tower2 < 0:  # The tower cannot be of a negative height.
    tower2 = abs(tower2)
    
# Prompt the user to enter the height of the center of the cable (in meters).
# If the towers are of unequal heights, the user is to enter 0.
height = float(input('Please enter the height of the cable\'s lowest point (m)\n - '
                     '(If the towers are of unequal heights, enter 0): '))
if tower1 != tower2:
    height = 0
print('\n')

# Clear the screen for the user to see the output more clearly.
clear()

# Move the cable into the coordinate plane with the tangential point (0, 0).
# If the towers are of equal heights, then:
if tower1 == tower2:
    y = tower1 - height
    x = length / 2

# The Hyperbolic Identity is: cosh**2(t) - sinh**2(t) = 1
    try:
        a = abs((y**2 - x**2) / (2*y))
        print('The cable is ', length, 'm long.')
        print('The two towers are ', tower1, 'm high.')
        print('The cable hangs ', height, 'm off the ground.\n')
        x = math.asinh(x / a)
    # The cable is folded in two.
    except ZeroDivisionError:
        print('The two towers are at the same point.')
    else:
        if height < 0:
            # The cable has too much slack.
            print('ERROR: The cable is dragging on the ground.')
        else:
            # Print out the results, rounding to 3 decimal places.
            print('The distance between the two towers is {:.3f}'.format(2 * a * x), 'm.')
else:
    # If the two towers are of unequal heights, then the math gets a lot uglier.
    z1 = tower1
    z2 = tower2
    y = length
    print('The entire cable is ', y, 'm long.')
    print('The first tower is ', z1, 'm high.')
    print('The second tower is ', z2, 'm high.')

    # Solve for a using the Quadratic Equation.
    a1 = (((z1 + z2) * (y ** 2 - (z1 - z2) ** 2)) +
          (2 * y * math.sqrt(z1 * z2 * (y ** 2 - (z1 - z2) ** 2)))) / (2 * (z1 - z2) ** 2)
    a2 = (((z1 + z2) * (y ** 2 - (z1 - z2) ** 2)) -
          (2 * y * math.sqrt(z1 * z2 * (y ** 2 - (z1 - z2) ** 2)))) / (2 * (z1 - z2) ** 2)

    # We use the small of the two solutions.
    a = min(a1, a2)

    # We calculate the length of each cable segment such that y1 + y2 = y.
    y1 = math.sqrt(z1 ** 2 + 2 * z1 * a)
    y2 = math.sqrt(z2 ** 2 + 2 * z2 * a)

    # We calculate the between the two towers such that x1 + x2 = x.
    x1 = a * math.log((z1 + y1 + a) / a)
    x2 = a * math.log((z2 + y2 + a) / a)

    # Print out the results, rounding to 3 decimal places.
    print('The two cable segments are {:.3f}'.format(y1), ' m and {:.3f}'.format(y2), ' m long, respectively.')
    print('The two towers are {:.3f}'.format(x1 + x2), ' m apart.')
