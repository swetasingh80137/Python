#IF THE STATEMENT
marks=87
if marks>=90:
    print("you will get a mobile phone")
print("thank you")

if marks>80:
    print("you will get a mobile phone")
print("thank you")


#IF-ELSE STATEMENT
Marks=87
if marks>=90:
    print("you will get cycle")
else:
    print("no cycle")
print("thank you")


#IF-ELIF-ELSE STATEMENT
marks=87
if marks>=90:
    print("you can go to a trip")
elif marks >=80 and marks<90:
    print("you will get a phone")
elif marks >=70 and marks<80:
    print("you get a new cycle")
else:
    print("you will not get your phone back")
print ("thank you")


#NESTED IF
marks=96
if marks>=80:
    print("you will get a phone")
    if marks>=95:
        print("you can go to a trip")
else:
    print("no phone for a month")


#SHORT HAND IF STATEMENT (one line if statement)
marks=97
if marks>=90: print("you will get a new phone")


#SHORT HAND IF-ELSE STATEMENT
marks=87
print ("you will go to a trip") if marks>=90 else print("no phone for a week")



#WRITE A PROGRAM TO CHECK IF A NUMBER IS POSITIVE
num= int(input("enter a number here:"))
if num>0:
    print ("it is positive")

#WRITE A PROGRAM TO CHECK WHETHER A NUMBER IS ODD OR EVEN
#(remainder zero i.e. modulus)
num= int(input("enter a number here"))
if num%2== 0:
    print("it is an even number")
else:
    print ("it is an odd number ")

#WRITE A PROGRAM TO CREATE AREA CALCULATOR
print("******AREA CALCULATOR******")
print ("""press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle""")

choice= int(input("enter a number between 1-4:"))
if choice== 1:
    side= float(input("enter the length of one side"))
    area= side**2
    print("the area of square is", area)
elif choice==2:
    length= float(input("enter the length of rectangle:"))
    width= float(input("enter the width of rectangle"))
    area= width* length
    print ("the area of rectangle is", area)
elif choice==3:
    radius= float (input ("enter the radius if circle:"))
    area= (22/7)*(radius**2)
    print("the area of the circle is", area)
elif choice==4:
    base=float(input("enter the base of the triangle:"))
    height= float(input("enter the height of triangle"))
    area= 0.5* base* height
    print("the area of the triangle is", area)
else:
    print("invalid input")


#WRITE A PROGRAM CHECK WHETHER THE PASSED LETTER IS A VOWEL OR NOT
letter= input("enter a letter here:")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")
else:
    print ("it is a consonant")

#WRITE A PROGRAM TO CHECK IF A NUMBER IS A SINGLE DIGIT NUMBER, 2-DIGIT, AND SO ON UPTO 5- DIGITS
num=int(input("enter a number here upto 5 digits:"))
if num>=0 and num<=9:
    print("it is a single digit no.")
elif num>=10 and num<=99
    print("it is a double digit no.")
elif num>=100 and num<=999
    print("it is a triple digit no.")
elif num>=1000 and num<=9999
    print("it is a four digit no.")
else:
    print("it is a 5 digit no.")

