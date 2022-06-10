"""
# using while loop
# Que.1 print all natural numbers from 1 to n
num = int(input('enter maximum natural number: '))
i = 1
while (i<= num):
    print(i)
    i = i+ 1
================================================

# Que.2 print all natural numbers reverse from n to 1
num = int(input('enter any natural number: '))
i = num
while (i >= 1):
    print(i, end = '')
    i = i- 1
=================================================

# Que.3 print all alphabets from a to z
# Printing a - z
print('alphabets from a - z are : ')
# a = 97 and z = 122
i = 97
while (i <= 122):
    print(chr(i),end = ' ')
    i += 1

or
# Printing A - Z
print('alphabets from  A- Z are : ')
# A = 65 and Z = 90
i = 65
while (i <= 90):
    print(chr(i),end = ' ')
    i += 1
=============================================

# Que.4 print all alphabets reverse from z to a
# Printing z - a
print('alphabets from z - a are : ')
# a = 97 and z = 122
i = 122
while (i >= 97):
    print(chr(i),end = ' ')
    i -= 1

or
# Printing Z - A
print('alphabets from Z - A are : ')
# A = 65 and Z = 90
i = 90
while (i >= 65):
    print(chr(i),end = ' ')
    i -= 1
====================================================

# Que.5 print all even numbers between 1 to 100
print('\nEven numbers from 1 to 100 are : ')
num = 2
while num<= 100:
    print(num, end = ' ')
    num = num + 2

or
print('\nEven numbers from 1 to 100 are : ')
i = 1
while (i <= 100):
    if((i % 2)== 0):
        print(i, end = ' ')
    i = i + 1
=============================================

# Que.6 print all even numbers reverse between 100 to 1
print('\nEven numbers from 100 to 1 are : ')
num = 100
while num >= 1:
    print(num, end = ' ')
    num = num - 2

#or
print('\nEven numbers from 100 to 1 are : ')
i = 100
while (i >= 1):
    if((i % 2)== 0):
        print(i, end = ' ')
    i = i - 1
===========================================

# Que.7 print all odd numbers between 1 to 100
print('\nOdd numbers from 1 to 100 are : ')
num = 1
while num<= 100:
    print(num, end = ' ')
    num = num + 2

or
print('\nOdd numbers from 1 to 100 are: ')
i = 1
while (i <= 100):
    if((i % 2)!=0):
        print(i, end = ' ')
    i = i + 1
=================================================

# Que.8 print all odd numbers reverse between 100 to 1
print('\nOdd numbers from 100 to 1 are : ')
num = 98
while num>= 0:
    print(num + 1, end = ' ')
    num = num - 2

or
print('\nOdd numbers from 100 to 1 are: ')
i = 100
while (i >= 1):
    if((i % 2)!=0):
        print(i, end = ' ')
    i = i - 1
==============================================

# Que.9 find sum of all natural numbers between 1 to n
num = int(input('enter any natural numbers 1 to: '))
sum = 0
i = 1
while i <= num:
    print(i,end = ' ')
    sum += i
    i += 1
print()
print('Sum of all natural numbers: ', sum)
====================================================

# Que.10 find sum of all even numbers between 1 to n
num = int(input('enter sum of even numbers 1 to: '))
sum = 0
i = 2
while i <= num:
    print(i, end = ' ')
    sum += i
    i += 2
print()
print('Sum of all even numbers: ', sum)
==================================================

# Que.11 find sum of all odd numbers between 1 to n
num = int(input('enter sum of odd numbers 1 to: '))
sum = 0
i = 1
while i<= num:
    print(i, end=' ')
    sum += i
    i += 2
print()
print('Sum of all odd numbers: ', sum)
===========================================

# Que.12 check whether number is perfect or not
num = int(input('enter any number: '))
sum = 0
i = 1
while i < num:
       if num % i == 0:
            sum += i
       i = i + 1
print()
if sum == num:
    print(num, 'is PERFECT number')
else:
    print(num, 'is not PERFECT number')
===========================================

# Que.13 print multiplication table of any number take user input
num = int(input('enter number to print table: '))
print('\nTable of:', num)
i = 1
while i <= 10 :
    print(num, 'x', i, '=', (num * i))
    i = i +1

or
num = int(input('enter number to print table: '))
print('\nTable of until of:', num)
i = 1
while i <= num :
    j = 1
    while j <= 10:
        print(i, 'x', j, '=', (i * j))
        j = j +1
    i = i +1
    print('\n')
=============================================

# Que.14 count number of digits in a number
num = int(input('enter any number: '))
# Store to temporary variable.
temp = num
count = 0
while (temp != 0):
    # Increment counter
    count += 1
    # Remove last digit of 'temp'
    temp = int(temp / 10)
print('\nTotal digits in', num, ':', count)
=================================================

# Que.15 find first and last digit of a number
num = input('enter the number: ')
while num.isnumeric():
    l = len(num)
    print('first digit of given number is:', num[0])
    print('last digit of given number is:', num[l-1])
    break
=====================================================

# Que.16 find sum first and last digit of a number
num = input('enter the number: ')
while num.isnumeric():
    l = len(num)
    sum = int(num[0]) + int(num[l-1])
    print('sum of first and last digit is: ',sum)
    break
===================================================

# Que.17 swap first and last digit of a number
num = input('enter the number: ')
while num.isnumeric():
    l = len(num)
    print('the number', num, 'after swapping first and last digit is: ', num[l-1] +num[1:l-1] +num[0])
    break
==========================================================

# Que.18 calculate sum of digits of a number
num = int(input('enter any number: '))
sum = 0
temp = num
while temp != 0:
    # r is a reminder
    r = num % 10
    sum = sum + r
    temp = temp// 10
print('the sum of:',num, 'is:',sum)
==============================================

# Que.19 calculate product of digit of number
num = int(input('enter any number: '))
product = 1
while(num != 0):
    product = product * (num % 10)
    # Remove last digit from num
    num = int(num / 10)
print('\nProduct of all digits in', num, ':', product)
==============================================

# Que.20 to enter the number and print its reverse
num = int(input('enter any number: '))
temp = num
reverse = 0
while(temp != 0):
    reverse = (reverse * 10) + (temp % 10)
    temp = int(temp / 10)
print('\nReverse number of', num, ':', reverse)
===============================================

# Que.21 check whether a number is palindrome or not
num=int(input('enter any number: '))
rev = 0
x = num
while num > 0:
    rev = (rev * 10)+ num % 10
    num = num // 10
if x == rev :
    print(x,'is a palindrome')
else:
    print(x,'is not a palindrome')
==============================================

# Que.22 find frequency of each digit in a given integer
num = int(input('enter any number: '))
print('digit\tFrequency')
for i in range(0,10):
    count = 0
    n = num
    while n > 0:
        digit = n %10
        if digit == i:
            count = count +1
        n = n //10
    if count > 0:
        print(i, '       ', count)
==============================================

# Que.23 enter a digit and print in word
words_upto_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
words_for_tens = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
num = int(input('enter a number: '))
if num > 99999:
    print('can not solve for more than 5 digits')
else:
    d = [0, 0, 0, 0, 0]
    i = 0
    while num > 0:
        d[i] = num % 10
        i += 1
        num = num // 10
    num = ' '
    if d[4] != 0:
        if d[4] == 1:
            num += words_upto_19[d[3]] + ' thousand '
        else:
            num += words_for_tens[d[4]] + ' ' + words_upto_19[d[3]] + ' thousand '
    else:
        if d[3] != 0:
           num += words_upto_19[d[3]] + ' thousand '
    if d[2] != 0:
        num += words_upto_19[d[2]] + ' hundred '
    if d[1] != 0:
        if d[1] == 1:
            num += words_upto_19[d[0]]
        else:
            num += words_for_tens[d[1]] + ' ' + words_upto_19[d[0]]
    else:
        if d[0] != 0:
            num += words_upto_19[d[0]]
print('number is in word:', num)
==============================================

# Que.24 find power of number
base = int(input('enter the base: '))
exponent = int(input('enter the exponent: '))
power = 1
while exponent != 0:
    power = power * base
    exponent -= 1
print('\nResult of', base, '^', exponent, 'is:', power)
===============================================

# Que.25 calculate factorial of a number
num = int(input('enter any number: '))
fact = 1
while num > 0:
    fact = fact * num
    num = num -1
print('factorial of a number is:', fact)
==============================================

# Que.26 find HCF of two numbers
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
i = 1
while (i <= num1 and i <= num2):
        if((num1 % i) == 0 and (num2 % i) == 0):
            gcd = i
        i = i +1
print('\nHCF', num1, 'and', num2, ':', gcd)
================================================

# Que.27 find LCM of two numbers
num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
# Find the max number
max_num = num2
if (num1 > num2):
    max_num = num1
i = max_num
lcm = 1
while(True):
    if((i % num1) == 0 and (i % num2) == 0):
        lcm = i
        break
    i += max_num
print('\nLCM of', num1, 'and', num2, ':', lcm)
=================================================

# Que.28 check whether a number is prime number or not
num = int(input('enter any number: '))
count = 0
i = 1
while i <= num:
    if ((num % i) == 0):
        count = count + 1
    i = i + 1
if count == 2:
    print(num, 'is a prime number')
else:
    print(num, 'is not a prime number')
================================================

# Que.29 print all prime number between 1 to n
num = int(input('find prime numbers 1 to: '))
print('\nAll prime numbers 1 to', num, 'are: ')
n = 2
while n <= num:
    i = -1
    j = 2
    while j <= 1:
        if(n % j == 0):
            i += 1
            j += 1
        else:
            j += 1
    if i == -1:
        print(n, end=' ')
        n = n + 1
    else:
        n = n + 1
=================================================

# Que.30 find sum of all prime numbers between 1 to n
num = int(input('Find sum of prime numbers 1 to: '))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
print('\nSum of all prime numbers 1 to', num, ':', sum)
================================================

# Que.31 check whether a number is armstrong number or not
num = int(input('enter number to check: '))
original_num = num
# Find total digits in given number
digits = int(math.log10(num) + 1)
sum = 0
while (num > 0):
    last_digit = int(num % 10)
    sum = sum + round(math.pow(last_digit, digits))
    # Remove the last digit
    num = num / 10
    # Empty print statement for new line
print()
if original_num == sum:
    print(original_num, 'is ARMSTRONG NUMBER')
else:
    print(original_num, 'is not ARMSTRONG NUMBER')
=======================================================

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
====================================================

# Que.33 print fibonacci series up to n terms
num = int(input('enter number of series: '))
n1 = 0
n2 = 1
n3 = 0
while n3 <= num :
    print(n3, end = ' , ' )
    n1 = n2
    n2 = n3
    n3 = n1 + n2
==============================================

# Que.34 to print the given number pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

num = int(input('enter the number of rows: '))
i = 1
while i <= num:
    j = 1
    while j <= i:
        print(i , end= ' ')
        j += 1
    print()
    i += 1
==================================================

# Que.35 to print the given star pattern
*
**
***
****
*****

num = int(input('enter the number of rows: '))
i = 1
while i <= num:
    print(i* '*' , end= ' ')
    print()
    i += 1

"""
