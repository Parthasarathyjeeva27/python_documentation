for num in range(1,21,1): #Print numbers from 1 to 20
    print(num)
print("End of first program")


for num in range(0,51,2):#Print even numbers from 0 to 50
    print(num)
print("End of second program")


Mul_Table_of_2=int(input("enter the value"))#Print multiplication table of given number
for num in range(1,11,1):
    print(num,"X",Mul_Table_of_2,"=",num*Mul_Table_of_2)
print("End of third program")


END_digit=int(input("enter the ending digit"))#Print summation from 1 to given ending digit
Summation=0
for num in range(1,END_digit+1,1):
    Summation=Summation+num
print("the summation is:",Summation)
print("End of fourth program")


for num in range(10,0,-1):#Print numbers from 10 to 1
    print(num)
print("End of fifth program")


Summation=0 #Count numbers divisible by 3 from 0 to 100
for num in range(0,101):
    if num%3==0:
        Summation=Summation+1
print("Number divisible by 3 is:",Summation)
print("End of sixth program")


for num in range(1,11,1):#Print squares of numbers from 1 to 10
    square=num**2
    print("The Squares of",num, "is:",square)
print("End of seventh program")


str="PYTHON" #Print each character of the string "PYTHON"
for char in str:
    print(char)
print("End of eighth program")  


factorial=1 #Calculate factorial of a given number
factorial_num=int(input("enter the number "))
for num in range(1,factorial_num+1):
    factorial=factorial*num
print("The factorial is:",factorial)
print("End of ninth program")


for num in range(1,30,2): #Print odd numbers from 1 to 30
    print(num)
print("End of tenth program")