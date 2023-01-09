"""
# Python Nested if practice codes:
------------------------------------------------

age > 25 and Female 1, 2, 3, 4, 5
age > 25 and Male 7, 8, 9

age = int(input('Enter your age: '))
gender = input('enter gender(Male/Female): ')
if age > 25:
    if gender == 'female':
        print('you will stay @room no.1, 2, 3, 4, 5')
    else:
        print('you will stay @room no.7, 8, 9')
===============================================

money = int(input('Enter your money: '))
gender = input('enter gender(Male/Female):')
if money > 99000:
    if gender == 'female':
        print('you got the Apple mobile')
    else:
        print('you got the Apple laptop')
===============================================

weight= int(input('Enter your weight: '))
gender = input('enter gender(Male/Female): ')
if weight > 80:
    if gender == 'female':
        print('Do exercise')
    else:
        print('loss the fat')
=================================================

p = input('you have cold or not?: ')
t = float(input('temperature: '))
if (p == 'cold' or p == 'COLD'):
    if t > 90:
        print('take medicine Sinarest')
    else:
        print('take medicine vicks')
elif (p == 'hot' or p == 'HOT'):
    if t > 100:
        print('need to admit')
    else:
        print('take rest in home')
else:
    print('no need of medicine')
=====================================================

story_nm = input('which story you like: ')
age = int(input('enter age:'))
if story_nm == 'cindrella':
    if age < 6:
        print(story_nm, 'story for small kids age is: ', age)
    else:
        print(story_nm, 'this story like to all kids age is: ', age)
elif story_nm == 'thumbLina':
    if age < 10:
        print(story_nm, 'story for kids age is: ', age)
    else:
        print(story_nm, 'this story like to all kids age is: ', age)
else:
    print(story_nm, 'this story for child age is:', age)
==========================================================

year = int(input('enter year: '))
if year % 400 == 0:
 if year % 4 == 0 :
     print('Leap Year')
 else:
     print('Not a Leap year')
else:
    print('enter correct year')
===========================================================

search = input('enter search engine name: ')
time = float(input('enter time: '))
if search == 'Google':
    if time > 10:
       print('you use', search, 'engine for all required knowledge, at time', time)
    else:
       print('you use', search, 'engine for all required knowledge, at time', time)
elif search == 'other':
    if time > 6:
       print('you use', search, 'engine for all required knowledge, at time', time)
    else:
       print('you use', search, 'engine for all required knowledge, at time', time)
else:
    print('you use', search, 'engine this is not valid for getting knowledge, at time', time)
==============================================================
"""
