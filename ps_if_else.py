"""
# Que.1 find maximum between two numbers
n1 = int(input('enter the first number:'))
n2 = int(input('enter the secound number:'))
if n1 > n2:
    print(n1,'is maximum then n2')
else:
    print(n2,'is maximum then n1')
====================================================

# Que.2 find maximum among three numbers
n1 = int(input('enter the first number:'))
n2 = int(input('enter the secound number:'))
n3 =  int(input('enter the third number:'))
if (n1 > n2) and (n1 > n3):
    print(n1,'is maximum then n2 and n3')
elif n2 > n3:
    print(n2,'is maximum then n1 and n3')
else:
     print(n3,'is maximum then n2 and n1')
=====================================================

# Que.3 check whether number is +ve, -ve or zero
num = int(input('enter the number:'))
if num > 0:
    print('then number is positive')
elif num < 0:
    print('then number is negative')
else:
    print('then number is zero')

or
num = float(input('enter the number:'))
if num > 0:
    print(num,'is positive')
elif num == 0:
    print(num,'is zero')
else:
    print(num,'is negative')
=====================================================

# Que.4 check whether number is divisible by 5 or not
num = float(input('enter the number:'))
if (num % 5 == 0):
    print(num,'is divisible by 5')
else:
    print(num,'is not divisible by 5')
======================================================

# Que.5 check whether number is even or odd
num = int(input('enter the number:'))
if num % 2 == 0:
    print(num,'is even')
else:
    print(num,'is odd')
====================================================

# Que.6 check whether a year is leap year or not
year = int(input('enter the year:'))
if (year % 400 == 0):
    print(year,'is a leap year')
elif (year % 4 == 0 and year % 100 != 0):
    print(year,'is a leap year')
else:
    print(year, 'is not a leap year')

or
year = int(input('enter the year:'))
if (year % 4 == 0 or year % 400 == 0 or year % 100 == 0):
    print(year,'is a leap year')
else:
    print(year, 'is not a leap year')
====================================================

# Que.7 check whether character is alphabet or not
char = str(input('enter the any character:'))
if (char.isalpha()):
    print(char,'is an alphabet')
else:
    print(char,'is not an alphabet')

or
char = str(input('enter the any character:'))
if ('a'<= char <='z') or ('A'<= char <='Z'):
    print(char,'is an alphabet')
else:
    print(char,'is not an alphabet')
====================================================

# Que.8 to input any character check whether it is vowel or consonant
a = str(input('enter the any alphabet:'))
V = a.lower()
v = ('a','e','i','o','u')
if (V in v):
    print('its a vowel')
else:
    print('its a consonant')

or
a = str(input('enter the any alphabet:'))
if a in ('a','e','i','o','u','A','E','I','O','U'):
    print('the given alphabet is a vowel')
else:
    print('the given alphabet is a consonant')
==============================================================

# Que.9 check whether character is uppercase or lowercase alphabet
char = str(input('enter the any alphabet:'))
if char.isupper():
    print(char, 'is a uppercase alphabet')
else:
    print(char, 'is a lowercase alphabet')

=========================================================

# Que.10 to count total number of notes in given amount
amount = int(input('enter amount multiple of 100,200,500 and 2000:'))
notes = int(input('enter which currency notes you have:'))
a = amount
n = notes
if (n == 100 and a % n == 0):
    ct = int(a/n)
    print('you have', ct, 'currency notes of', n)
elif (n == 200 and a % n == 0):
    ct = int(a/n)
    print('you have', ct, 'currency notes of', n)
elif (n == 500 and a % n == 0):
    ct = int(a/n)
    print('you have', ct, 'currency notes of', n)
elif (n == 2000 and a % n == 0):
    ct = int(a/n)
    print('you have', ct, 'currency notes of', n)
else:
    ('you have entered wrong details')
=============================================================

# Que.11 to input angles of a triangle and check whether triangle is valid or not
a = int(input('enter the angle 1:'))
b = int(input('enter the angle 2:'))
c = int(input('enter the angle 3:'))
total = a + b + c
if (total == 180):
    print('triangle is valid')
else:
    print('triangle is invalid')
==========================================================

# Que.12 to input all sides of a triangle and check whether triangle is valid or not
a = int(input('enter the side 1:'))
b = int(input('enter the side 2:'))
c = int(input('enter the side 3:'))
if (a + b > c):
    print('triangle is valid')
elif (c + b > a):
    print('triangle is valid')
elif (a + c > b):
    print('triangle is valid')
else:
    print('triangle is invalid')
===========================================================

# Que.13 check whether the triangle is equilateral,isoscales or scalene triangle
a = int(input('enter the side 1:'))
b = int(input('enter the side 2:'))
c = int(input('enter the side 3:'))
if a == b == c:
    print('triangle is equilateral triangle')
elif a == b or a == c or b == c:
    print('triangle is isoscales triangle')
else:
    print('triangle is scalene triangle')
===========================================================
# Que.14 calculate profit or loss. input is selling cost and actual cost
s_cost = int(input('enter the selling cost:'))
a_cost = int(input('enter the actual cost:'))
if s_cost > a_cost:
    profit = s_cost - a_cost
    print('you made a profit of:',profit)
elif s_cost < a_cost:
    loss = a_cost - s_cost
    print('you made a loss of:',loss)
else:
    print('you made no profit no loss')
==============================================================

# Que.15 calculate percentage and grade
phy = int(input('please entered your marks obtained in physics out of 100:'))
chem = int(input('please entered your marks obtained in chemistry out of 100:'))
bio = int(input('please entered your marks obtained in biology out of 100:'))
math = int(input('please entered your marks obtained in mathematics out of 100:'))
comp = int(input('please entered your marks obtained in computer out of 100:'))

total_marks = phy + chem + bio + maths + comp
percentage = total_marks / 5

if percantage >= 90:
    print('you passed with grade A')
elif percantage >= 80:
    print('you passed with grade B')
elif percantage >= 70:
    print('you passed with grade C')
elif percantage >= 60:
    print('you passed with grade D')
elif percantage >= 40:
    print('you passed with grade E')
elif percantage < 40:
    print('you failed with grade f')
else:
    print('you are fail and resticatated')
===========================================================

# Que.16 calculate its gross salary
basic = int(input('enter a basic salary of an employee:'))
if basic <= 10000:
    hra = basic* 0.2
    da = basic* 0.8
elif basic <= 20000:
    hra = basic * 0.3
    da = basic * 0.9
else:
    hra = basic * 0.35
    da = basic * 0.95
gross = basic + hra + da
pf = 0.12* basic
net = gross - pf;
print('basic salary:',basic)
print('gross salary:',gross)
print('net salary:',net)

0r
basic_salary = int(input("Enter a basic salary of an employee: "))
if basic_salary <= 10000:
    print("Gross salary is: ", basic_salary + basic_salary * 0.2 + basic_salary * 0.8)
elif basic_salary <= 20000:
    print("Gross salary is: ", basic_salary + basic_salary * 0.3 + basic_salary * 0.9)
else:
    print("Gross salary is: ", basic_salary + basic_salary * 0.35 + basic_salary * 0.95)
======================================================

# Que.17 calculate total electricity bill
units = int(input('please entered number of units you consumed:'))
if (units > 50):
    amount = units* 0.50
    surcharge = 17
elif (units > 100):
    amount = units* 0.75
    surcharge = 0.17
elif (units > 100):
    amount = units* 1.25
    surcharge = 0.17
elif (units > 250):
    amount = units* 1.50
    surcharge = 0.17
else:
    amount = units* 2
    surcharge = 0.17
total_bill = amount + surcharge
print('electricity bill:',total_bill)

or
u = int(input('Enter a total consumption of units:'))
if u <= 50:
    t_c = u * 0.5
    f_c = t_c + 0.17 * t_c
    print('Total bill is:', f_c)
elif u <= 150:
    t_c = (50 * 0.5) + ((u-50) * 0.75)
    f_c = t_c + (0.17 * t_c)
    print('Total bill is:', f_c)
elif u <= 250:
    t_c = (50 * 0.5) + (100 * 0.75) + ((u-150) * 1.25)
    f_c = t_c + (0.17 * t_c)
    print('Total bill is:', f_c)
else:
    t_c = (50 * 0.5) +(100 * 0.75) + (100 * 1.25) + ((u - 250) * 1.5)
    f_c = t_c + (0.17 * t_c)
    print('Total bill is:', f_c)
"""
