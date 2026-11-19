# print statement
print("sufiyan beg",23,34, sep='~', end='875\n')
print("beg")

# Escape Sequence Characters
print("sufiyan beg\nand he is a good boy \'from shajapur\'")

# DAY:6 DATA TYPES
# Variables is a storage location in memory(RAM) to store data values. In python, variables are created when you assign a value to it.
name = "Sufiyan" # this type of variable is called string variable
age = 21 # this type of variable is called integer variable
a = 23.5 #this type of variable is called float variable
c = complex(2,3) # this type of variable is called complex variable
s = True # this type of variable is called boolean variable
print(name,'\n',age,'\n',a,'\n',c,'\n',s)
# print(name+a) # this will give an error because we cannot add string and float variable
print(name+str(a)) # this will give an output because we are converting float variable to string variable

# mutable and immutable variables
# mutable variables are those variables whose value can be changed after it is created. For example, lists and dictionaries are mutable.
# immutable variables are those variables whose value cannot be changed after it is created. For example, strings and tuples are immutable.

# Map data type
# dictionary=data type is a collection of key-value pairs. It is also known as dictionary in

# DAY:7 OPERATORS

# Arithmetic Operators
print(5+3) # addition
print(5-3) # subtraction
print(5*3) # multiplication
print(5/3) # division
print(5%3) # modulus / Remainder
print(5**3) # exponentiation
print(5//3) # floor division    

# Exercise: 1 Create a calculator
"""
Create a calculater capable of performning addition, 
subtraction, multiplication, and division operation on two numbers. 
your program should format the output in a readable manner! 
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("additions is ",a+b,"\n",type(a+b))
print("subtraction is ",a-b,"\n",type(a-b))
print("multiplication is ",a*b,"\n",type(a*b)) 
print("division is ",a/b,"\n",type(a/b))
print("modulus is ",a%b,"\n",type(a%b))
print("floor division is ",a//b,"\n",type(a//b))
print("exponentiation is ",a**b,"\n",type(a**b))

#DAY:8 TYPE CASTING IN PYTHON

# Type casting is the process of converting one data type to another data type. In python, we can use the following functions to perform type casting:
#LIKE: int(), float(), str(), bool(), complex(), list(), tuple(), set(), dict()


#there are two types of type casting in python:

#1. Implicit Type Casting: In implicit type casting, the python interpreter automatically converts one
a = 10
b = 20
c = 10.5
print("Before Implicit type casting: ",a+c)

#2. Explicit Type Casting: In explicit type casting, the programmer manually converts one data type to another data type using the above functions.
print("Before type casting: ",int(a)+int(b)+float(c))

#DAY:10 TAKING INPUT IN PYTHON

# pythan is automatikally setting the input data type as string. so we need to convert it into integer or float if we want to perform any mathematical operation on it.

 
x = input("Enter your name: ")
print("Hello ",x) 

y = input("Enter the first value: ")
z = input("Enter the second value: ")
print("The sum of the two values is: ",y+z)
print("The sum of the two values is: ",int(y)+int(z)) # converting string to integer

print("additions is ",int(x)+int(y))
print("subtraction is ",float(x)-float(y))
print("multiplication is ",int(x)*int(y)) 
print("division is ",int(x)/int(y))
print("modulus is ",int(x)%int(y))
print("floor division is ",int(x)//int(y))
print("exponentiation is ",a**b)


#DAY:11 strings IN PYTHON

name = "Sufiyan Beg"
friends = "MohhammedShariqueMalik"
print("hello my name is " + name)
print("this is my friends" + friends)

print(name[0]) # this will print the first character of the string
print(name[-1]) # this will print the last character of the string  

print(name[0:6]) # this will print the first 6 characters of the string
print(name[0:]) # this will print the whole string
print(name[0:6:2]) # this will print the first 6 characters of the string with a step of 2  

print(friends[0:-1]) # this will print the whole string except the last character
print(friends[0:-4]) # this will print the whole string except the last 4 characters
print(friends[0:-4:2]) # this will print the whole string except the last 4 characters with a step of 2
print(friends[-1:-1]) # this will print the whole string in reverse order
print(friends[-1:0]) # this will print the whole string in reverse order except

for character in friends:
    print(character) # this will print each character of the string in a new line