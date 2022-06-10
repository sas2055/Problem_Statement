"""
# using for loop
# Que.1 print all natural numbers from 1 to n
num = int(input('enter any natural number: '))
print('\nNatural numbers from 1 to ', num)
for i in range(1, num + 1):
    print(i, end= ' ')
==================================================

# Que.2 print all natural numbers reverse from n to 1
num = int(input('enter any natural number: '))
print('\nNatural numbers from n to 1', num)
for i in range(num, 0, - 1 ):
    print(i, end= ' ')
===================================================

# Que.3 print all alphabets from a to z
# Printing a - z
print('alphabets from a - z are : ')
# a = 97 and z = 122
for alpha in range(97, 123):
    print(chr(alpha), end=' ')

or
# Printing A - Z
print('alphabets from A - Z are : ')
# A = 65 and Z = 90
for alpha in range(65, 90):
    print(chr(alpha), end=' ')

or
print('alphabets from a - z are: ')
for ch in string.ascii_lowercase:
    print(ch, end= ' ')
print('\nAlphabets from A - Z are: ')
for ch in string.ascii_uppercase:
    print(ch, end=' ')
===================================================

# Que.4 print all alphabets reverse from z to a
# Printing z - a
print('alphabets from z - a are : ')
# a = 97 and z = 122
for alpha in range(122, 96 ,-1):
    print(chr(alpha), end=' ')

or
# Printing Z - A
print('alphabets from Z - A are : ')
# A = 65 and Z = 90
for alpha in range(90, 64, -1):
    print(chr(alpha), end=' ')
=================================================

# Que.5 print all even numbers between 1 to 100
print('\nEven numbers from 1 to 100 are : ')
for i in range(1, 101):
    #Check for even or not.
    if((i % 2) == 0):
        print(i, end=' ')
==============================================

# Que.6 print all even numbers reverse between 100 to 1
print('\nEven numbers from 100 to 1 are : ')
for i in range(100, 0, -1):
    #Check for even or not.
    if ((i % 2) == 0):
        print(i, end=' ')
===============================================

# Que.7 print all odd numbers between 1 to 100
print('\nOdd numbers from 1 to 100 are: ')
for i in range(1, 100):
    #Check for odd or not.
    if((i % 2) != 0):
        print(i, end=' ')
===========================================

# Que.8 print all odd numbers reverse between 100 to 1
print('\nOdd numbers from 100 to 1 are: ')
for i in range(100, 0, -1):
    #Check for odd or not.
    if((i % 2) != 0):
        print(i, end=' ')
===========================================

# Que.9 find sum of all natural numbers between 1 to n
num = int(input('Enter any natural number 1 to : '))
sum = 0
for i in range(1, num + 1):
    sum += i
print('\nSum of all natural numbers: ', sum)
===================================================

# Que.10 find sum of all even numbers between 1 to n
num = int(input('enter sum of even numbers 1 to: '))
total = 0
for i in range(1, num + 1):
     # Check for even or not.
    if((i % 2) == 0):
        total = total + i
print('\nSum of even numbers from 1 to', num,'is: ', total)
===================================================

# Que.11 find sum of all odd numbers between 1 to n
num = int(input('enter sum of odd numbers 1 to: '))
sum = 0
for i in range(1, num + 1):
    #Check for odd or not.
    if(not (i % 2) == 0):
        sum = i + sum
print('\nSum of odd numbers from 1 to', num, 'is:', sum)
====================================================

# Que.12 check whether number is perfect or not
num = int(input('enter any number: '))
sum = 0
# Calculate sum of all proper divisors
for i in range(1, num):
    if num % i == 0:
        sum += i
# Empty print statement for new line
print()
# Check whether the sum of divisors is equal to num
if sum == num:
    print(num, 'is PERFECT number')
else:
    print(num, 'is not PERFECT number')
=======================================================

# Que.13 print multiplication table of any number take user input
num = int(input('enter number to print table: '))
print('\nTable of:', num)
# Printing table of given number
for i in range(1, 11):
    print(num, '*', i, '=', (num * i))
========================================================

# Que.14 count number of digits in a number
num = str(input('enter the number: '))
count = 0
for digit in num:
    count = count +1
print('total number of digit present is: ',count)
=======================================================

# Que.15 find first and last digit of a number
num = input('enter the number: ')
for dig in num:
    if num.isnumeric():
        l = len(num)
print('first digit of given number is:', num[0])
print('last digit of given number is:', num[l-1])
=======================================================

# Que.16 find sum first and last digit of a number
num = input('enter the number: ')
for dig in num:
    if num.isnumeric():
        l = len(num)
sum = int(num[0]) + int(num[l - 1])
print('sum of first and last digit is: ', sum)
========================================================

# Que.17 swap first and last digit of a number
num = input('enter the number: ')
for dig in num:
    if num.isnumeric():
        l = len(num)
print('the number', num, 'after swapping first and last digit is: ', num[l-1] +num[1:l-1] +num[0])
=======================================================

# Que.18 calculate sum of digits of a number
num = input('enter any number: ')
sum = 0
for i in range(0, len(num)):
    sum = sum + int(num[i])
print('\nSum of digits is:', sum)
======================================================

# Que.19 calculate product of digit of number
num = str(input('enter any number: '))
product = 1
for i in num:
    product = product * int(i)
print('\nProduct of all digits in', num, ':', product)
======================================================

#Que.20 to enter the number and print its reverse
num = input('enter any number: ')
reverse = ''
for i in range (len(num) -1, -1, -1):
    reverse = reverse + num[i]
print('reverse number is', num, 'is:', reverse)
=======================================================

# Que.21 check whether a number is palindrome or not
num=input('enter any number:')
i = 0
for i in range(len(num)):
    if num[i]!=num[-1-i]:
        print('It is not a palindrome')
        break
    else:
        print('It is a palindrome')
        break
======================================================

# Que.22 find frequency of each digit in a given integer
num = input('enter the number: ')
for i in set(num):
   l = num.count(i)
   print('frequency of a given integer is: ',i, '=', l ,'times')
======================================================

# Que.23 enter a digit and print in word
words_upto_19 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven',
                 'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
words_for_tens = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
num = int(input('enter a digit from 0 to 99: '))
for i in str(num):
    if num == 0:
        output = 'zero'
    elif num <= 19:
        output = words_upto_19[num]
    elif num <= 99:
        output = words_for_tens[num // 10] + ' ' + words_upto_19[num % 10]
    else:
        output = 'please enter a value from 0 to 99 only'
print('number is in word: ',output)
======================================================

# Que.24 find power of number
base = int(input('enter base: '))
exponent = int(input('enter exponent: '))
power = 1
for i in range(1, exponent + 1):
    power = power * base
print('\nResult', base, '^', exponent, ':', power)
print('Using math class:', math.pow(base, exponent))
=======================================================

# Que.25 calculate factorial of a number
num = int(input('enter any number: '))
print('\nAll factors of', num, 'are: ')
for i in range(1, num + 1):
    # Completely divisible or not.
    if(num % i == 0):
        print(i, end = ' ')
=======================================================

# Que.26 find HCF of two numbers
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
# Find minimum between two numbers
min = num1
if num2 < num1:
    min = num2
for i in range(1, min + 1):
    if((num1 % i) == 0 and (num2 % i) == 0):
            hcf = i
print('\nHCF of', num1, 'and', num2, ':', hcf)
========================================================

# Que.27 find LCM of two numbers
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
# l = to store the lcm
# g = to store the gcd
# Find maximum between two numbers
for i in range(1, num1 + 1):
    if i <= num2:
        if((num1 % i) == 0 and (num2 % i) == 0):
            g = i
l = (num1 * num2)/ g
print('\nLCM of', num1, 'and', num2, ':', l)
========================================================

# Que.28 check whether a number is prime number or not
num = int(input('enter any number: '))
i = 1
# Check for prime
for i in range(2, num):
    if (int(num % i) == 0):
        i = num
        break
if i is num:
    print('\n' + str(num), 'is not a prime number')
else:
    print('\n' + str(num), 'is a prime number')
=======================================================

# Que.29 print all prime number between 1 to n
num = int(input('find prime numbers 1 to: '))
print('\nAll prime numbers 1 to', num, 'are: ')
for i in range(2, num + 1):
    if num > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
    # If the number is prime then print it.
        else:
            print(i, end=' ')
=======================================================

# Que.30 find sum of all prime numbers between 1 to n
num = int(input('Find sum of prime numbers 1 to: '))
sum = 0
for i in range(2, num + 1):
    j = 2
    for j in range(2, i):
        if (int(i % j) == 0):
            j = i
            break
    # If the number is prime then add it.
    if j is not i:
        sum += i
print('\nSum of all prime numbers 1 to', num, ':', sum)
======================================================

# Que.31 check whether a number is armstrong number or not
num = input('Enter number to check: ')
m = 0
for i in range(0,len(num)):
    m = m + int(num[i])**3
if m == int(num):
    print(num,'is Armstrong number')
else:
    print(num,'is not Armstrong number')
========================================================

# Que.32 print all armstrong number between 1 to n
num = int(input('enter the armstrong number 1 to: '))
for i in range(1, num + 1):
    n = i
    result = 0
    s = len(str(i))
    while(i != 0):
        digit = i % 10
        result = result + digit**s
        i = i//10
    if n == result:
        print(n, end= ' ')
========================================================

# Que.33 print fibonacci series up to n terms
num = int(input('enter number of series: '))
n1 = 0
n2 = 1
print(n1,end= ' ')
print(n2,end= ' ')
for i in range(num-2):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end= ' ')
==================================================i=====

# Que.34 to print the given number pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

n = int(input('enter the number of rows:'))
# outer loop to handle number of rows
for i in range(n + 1):
    # nested loop
        for j in range(i):
            # display numbers
            print(i,end='')
            # new line after each row
        print('')
===========================================

# Que.35 to print the given star pattern
*
**
***
****
*****

n = int(input('enter the number of rows:'))
# outer loop to handle number of rows
for i in range(0,n):
    # inner loop to handle number of columns
    # values is changing according to outer loop
        for j in range(0,i + 1):
            # printing stars
            print('*',end='')
            # ending line after each row
        print()
"""

