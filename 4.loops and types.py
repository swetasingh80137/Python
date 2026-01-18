#LOOPS-REPEAT SOMETHING
#TYPES-FOR, WHILE, WHILE TRUE, NESTED

#FOR LOOP
#IT IS A LOOP THAT REPEATS SOMETHING IN A GIVEN RANGE
#THE RANGE HAS A STARTING POINT , ENDING POINT AND STEP/GAP IN IT, (+1 IS ADDED TO ENDING POINT FOR DEFINING A RANGE)

for i in range (1,6):
    print(i)
for i in range (1,6):
    print("hello")
#for odd no.
for i in range (1,6,2):
    print(i)
#for even value
for i in range (0,6,2):
    print(i)
#start even series with 2
for i in range (2,6,2):
    print(i)
#multiplication tables:
n=7
for i in range (1,11):
    print(n,"*",i,"=",n*i)

n= int(input("enter a number here:"))
for i in range (1,11):
    print(n,"*",i,"=",n*i)

n= int(input("enter a number here:"))
for i in range (1,51):
    print(n,"*",i,"=",n*i)
    #add (1,51,2)- to get only odd multiplication (2 at the end)


#WHILE LOOP
#EXECUTES TILL THE GIVEN CONDITION IS TRUE (INCREMENT IS DONE INSIDE LOOP)
n=0
while n<=5:
    print(n)
    n+=1
#odd and even (that is gap of 2)
n=0
while n <=10:
    print(n)
    n+=2
#multiplication table
n=1
a=7
while n<=10:
    print(a,"*",n,"=",n*a)
    n+=1


#WHILE TRUE (INFINITE LOOP)- TO BREAK THIS LOOP, BREAK STATEMENT IS USED
while True:
    num1= int(input("enter a no.:"))
    num2= int(input("enter a no. here:"))
    print (num1 + num2)
    repeat= input("do you want to stop the program:")
    if repeat== "yes":
        break


#NESTED LOOPS (A LOOP INSIDE A LOOP)- SOLVE PATTERN PROBLEMS

for i in range (1,4):
    for j in range (1,11):
        print(j)
    print()

#to print it in one line
for i in range (1,4):
    for j in range (1,11):
        print(j,end ="")
    print()


for a in range(1,6):
    for b in range (1, a+1):
        print(b,end="")
    print()

#FOR LOOP WITH CONDITIONAL STATEMENTS
#I have to play 10 songs and 3rd one is my favourite
for i in range (1,11):
    if i == 3:
        print ("add this song to the favourite")
    else:
        print(i)

#1-100, common multiple in table of 8 and 12
for i in range (1,101):
    if i%8==0  and i%12==0:
        print(i)

#WHILE LOOP WITH CONDITIONAL STATEMENTS
n=1
while n<=10:
    if n==3:
        print("add this to favourite")
    else:
        print(n)
    n +=1


#BREAK STATEMENTS- WHEN YOU WANT TO DESTROY A LOOP AT CERTAIN CONDITION OR COME OUT OF A LOOP
#CONTINUE STATEMENTS- WHEN YOU WANT TO SKIP A CONDITION
#BOTH OF THEM ARE USED WITH LOOP
for i in range (1,11):
    if i ==5:
        continue
    else:
        print(i)

for i in range (1,11):
    if i ==7:
        break
    else:
        print(i)



#write a program to find a sum of all the even nos. upto 50
sum=0
for i in range (1,51):
    if i %2==0:
        sum+=i
print("the sum of all even no. upto 50 is",sum)

#write a program to write first 20 nos. and the squared no.
for i in range (1,21):
    print (i, i**2)

#write a program to find sum of first 10 odd no. and using while loop
sum=0
n=0
while n<20:
    if n %2 != 0:
        sum += n
    n +=1
print("the sum of first 10 odd no. is",sum)


#write a program to check if a number is divisible by 8 and 12, up to 100 nos.
for i in range(1,101):
    if (i%8==0) and (i%12==0):
        print(i)

#write a program to create a billing system at supermarket (POV cashier)
while True:
    name = (input("enter customer name here:"))
    total  = 0
    while True :
          print ("enter the amount and quantity:")
          amount= float(input("enter amount:"))
          quantity= float(input("enter quantity:"))
          total =+ amount* quantity
          repeat= input("do you want to add more items? (yes/no):")
          if repeat== "no" or repeat=="no":
              break
    print("-"*40)
    print("Name:", name)
    print ("amount to be paid:", total)
    print("-"*40)
    print("**********happy shopping***********")
    repeat1= input("do you want to go to next customer?(yes/no):")
    if repeat1 == "no" or repeat1 == "No":
              break


#a= "why fit in, when you are born to stand out!"
#write a program to find the length of the string:
a= "why fit in, when you are born to stand out!"
print (len(a))
#or
b= (len(a))
print(b)
print("the length of given string is",b)

#write a program to check how many times alphabet o is occuring:
print(a.count("o"))
print("the no. of times small o is occuring is", a.count("o"))

#convert whole string into lower and upper case
x= a.lower()
print(x)
y= a.upper()
print(y)


#convert string into a title
z= a.title()
print(z)

#to find index number of "fit in"
print (a.find("fit in)"))


#pattern problems
#1 2 3 4
#1 2 3 4
#1 2 3 4
#1 2 3 4
for i in range (1,5): #rows
    for j in range (1,5): #columns
        print(j, end = " ")
    print()
#replace j with star or anything to get that pattern "*"


#1
#1 2
#1 2 3
#1 2 3 4
for i in range (1,5):
    for j in range (1,i+1):
        print( j, end= " ")
    print()

#1
#2 2
#3 3 3
#4 4 4 4
for i in range (1,5):
    for j in range (1, i+1):
        print(i, end=" ")
    print()


#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5
for i in range (1,6):
    for j in range (6,i,-1):
        print(i, end=" ")
    print()


#            *
#         *  *
#      *  *  *
#   *  *  *  *
#*  *  *  *  *
for i in range (1,6):
    for j in range (5,i,-1):
        print(" ",end =" ")
    for k in range (i):
        print("*", end = " ")
    print()


#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1
for i in range (1,6):
    for j in range (i, 0, -1):
        print(j, end= " ")
    print()


#*
#*  *
#*  *  *
#*  *  *  *
#*  *  *  *  *
#*  *  *  *
#*  *  *
#*  *
#*
for i in range (1,6):
    for j in range (1,i+1): #column is increasing by 1
        print("*", end=" ")
    print()
for i in range (5,0,-1): #5-coz 4321, where to stop- 0(zero), decrement- 1
    for k in range (0,i-1):    #column is decreasing by 1
        print("*", end =" ")
    print()


#1
#2 4
#3 6 9
#4 8 12 16
#5 10 15 20 25
#6 12 18 24 30 36
#7 14 21 28 35 42 49
#8 16 24 32 40 48 56 64
for i in range (1,9):
    for j in range (1,9):
        print(i * j, end =" ") #for box pattern (i*j, end =" ")
    print()
for i in range (1,9):
    for j in range (1, i+1):
        print(i*j, end =" ")
    print()














