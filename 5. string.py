#STRING- combination of letters , no., symbols enclosed inside a quotation

#STRING MANIPULATION------------------------------------------------------------------------------------
a= "Harry Potter and the Goblet of Fire"

#length of string
print (len(a))

#count- to find no. of times a letter character is occuring
print(a.count("o"))

#upper case - convert
print(a.upper())

#lower case- convert
print(a.lower())

#index
print(a.index("o"))
print(a. index ("o",15,34))

#title- 1st letter of all the words in capital
print("this is title method-----------", a.title())

#capitalize- 1st letter of the string capitalize
print("this is capitalize method------", a.capitalize())

#casefold-
print("this is casefold method-------", a.casefold())

#find-
print(a.find("o"))
print(a.find("o",15,34))

#format to write variable inside a string
name= "john"
age=24
b= "my name is",name
print(b)
c= "my name is {}"
print (c.format (name))
d="my name is {}. and my age is {}"
print(d.format(name, age))

#center- fills given character and centralizes the string
print(name.center(20)) #20spaces
print(name.center (20,"*"))




#=================================================================================================================
#STRING FUNCTIONS-----------------------------------------------------------------------------------
a="hello"
b="Hello123"
c="123456"
d="HELLO"
e= " "
f="Hello 123@"
g=("1.234")

#isalnum- returns true if all character in string are alphanumeric
print("a is alphanumeric string------", a.isalnum())
print("b is alphanumeric string-------", b.isalnum())
print("e is alphanumeric string-----", e.isalnum())
print(f, f.isalnum())

#isalpha- returns true if all characters in string are alphabets
print(a, a.isalpha())
print(c, c.isalpha())

#isdecimal- returns true if all characters in strings are decimals
print(g, g.isdecimal())
print(c, c.isdecimal())

#isdigit- returns true if all characters in string are digits
print(g, g.isdigit())

#isnumeric-returns true if all characters in string are numeric
print(c, c.isnumeric())

#islower-checks if the string is in lower case or not
print(a, a.islower())

#isupper-checks if the string is in upper case or not
print(d, d.isupper())

#isspace- returns true if all characters in strings are white spaces
print(e, e.isspace())
print(f, f.isspace())

#istitle- returns true if string follows rule of title
print(f, f.istitle())

#===================================================================================================================
#string methods -------------------------------------------------------------------------------------------

#endswith- returns true if string ends with the specified value
a= "Harry Potter"
print(a.endswith("P"))
print(a.endswith("t",6,9))  #range 6 and 9

#startswith- returns true if string starts with specified value
print(a.startswith("H"))
print(a. startswith("p",6,9))

#swapcase- convert lower to upper and vice versa
print(a.swapcase())

#strip- returns a trimmed version of the string
print(a.strip())
b= ("              **** harry potter ****             ")
print(b.strip()) #only spaces remove
print(b.strip("*, ")) #star also got removed

#split- splits the string at specified separator and returns a list
d= "#oofd#brb#omw#tb"
print(d.split("#"))
e= "@ydyj@tfuftftcjy@hfytf@dtt@tfy"
print(e.split("@"))


#ljust- returns a left justified version of string
a= "harry potter"
x=a.ljust(20) #20spaces
print(x, "is my favourite movie")
y=a.ljust(20,"*")
print(y, "is my favourite movie")


#rjust-returns a right justified version of string
x=a.rjust(40)
print(x, "is my favourite movie")
y=a.rjust(40, "*")
print(y, "is my favourite movie")


#replace- returns a string where a specified value is replaced with a value
a= "my name is john"
print (a)
print(a.replace("john","lisa"))
b="my name is john and john like to play, john is a nice person"
print(b.replace("john","leesa"))


#rindex- searches the string for a specified value and returns last position of where it was found
a=" harry potter and the prisoner of azkaban"
print(a.rindex("harry"))

#rfind- same as rindex



#=================================================================================================================
#STRING SLICING

a="Harry Potter and the Goblet of Fire"
print(a)
print(a[0:5])   #we need harry word only, so the index of h is 0 and index of y is 4 so we write plus 1)
print(a[6:12])
print(a[:5])
print(a[-4:])

b="0123456789"
print(b)
print(b[::2]) #gaps of 2 between no.
print(b[:7]) #end at 6 so take end value 7
print(b[:7:2])  #gap of 2 and end
print (b[::-1])   #reverse of string
print (b[6::-1])


