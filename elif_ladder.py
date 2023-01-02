"""
# Python elif ladder practice codes:
------------------------------------------------

name = str(input('Enter your name: '))
per = float(input('Enter the percentage: '))

if per >= 75:
    print(name, 'you got distinction')
elif per >= 65:
    print(name, 'you got first class')
elif per >= 55:
    print(name, 'you got second class')
elif per >= 45:
    print(name, 'you got pass class')
else:
    print(name, 'sorry you are fail')

============================================

name = str(input('Enter your name: '))
per = float(input('Enter the percentage: '))

if per >= 90:
    print(name, 'you got bike')
elif per >= 80:
    print(name, 'you got mobile')
elif per >= 70:
    print(name, 'you got watch')
elif per >= 55:
    print(name, 'you got shirt')
else:
    print(name, 'sorry you got nothing')
=============================================

size = float(input('Enter the size: '))
if size > 200:
    print('Its xxl size')
elif size > 100:
    print('Its xl size')
elif size > 50:
    print('Its l size')    
else:
    print('Its m size')
==============================================

name = str(input('Enter your name: '))
per = float(input('Enter the percentage: '))

if per >= 90:
    print(name, 'you got job in Infosys')
elif per >= 80:
    print(name, 'you got job in TCS')
elif per >= 70:
    print(name, 'you got job in Vipro')
elif per >= 55:
    print(name, 'you got job in local company')
else:
    print(name, 'better luck next time')
=============================================

name = str(input('Enter your name: '))
per = float(input('Enter the percentage: '))

if per >= 110:
    print(name, 'you had full present')
elif per >= 80:
    print(name, 'you had very good a present')
elif per >= 70:
    print(name, 'you had good present')
elif per >= 55:
    print(name, 'you had low present')
else:
    print(name, 'you consider in default list')
=================================================

time = float(input('whats time now(^ to 24): '))
if (time >= 6) and (time < 12):
    print('Good Morning')
elif (time >= 12) and (time < 16):
    print('Good Afternoon')
elif (time >= 16) and (time < 20):
    print('Good Evening')
else:
    print('Good Night')
==================================================

color = input('Enter color name: ')
if color == 'White':
    print('today', color, 'color day')
elif color == 'Blue':
    print('today', color, 'color day')
elif color == 'Green':
    print('today', color, 'color day')
else:
    print('its multi color', color, 'day')
===================================================

ch = str(input('which TV channel like: '))
if ch == 'star':
    print('This is', ch, 'Channel')
elif ch == 'Marathi':
    print('This is', ch, 'Channel')
elif ch == 'Sports':
    print('This is', ch, 'Channel')
elif ch == 'discovery':
    print('This is', ch, 'Channel')
else:
    print('this is news channel')
====================================================

season = input('Enter season name: ')
discount = int(input('how much discount: '))
if season != 'summer' and season != 'winter':
    print(season, 'starts, so Discount on Raincoat up-to', discount, '%')
elif season == 'summer':
    print(season, 'starts, so Discount on cotton wear up-to', discount, '%')
elif season == 'winter':
    print(season, 'starts, so Discount on sweter up-to', discount, '%')
else:
    print('Its not rainy, winter & summer season')
======================================================
"""
