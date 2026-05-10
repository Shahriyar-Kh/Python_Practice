#type casting is the process of converting one data type to another data type. In python we can use built in functions to convert one data type to another data type.
#type casting types
#1. implicit type casting which is done automatically by python when we perform operations on different data types. For example, when we add an integer and a float, python will automatically convert the integer to a float before performing the addition.
#2. explicit type casting which is done manually by the programmer using built in functions such as

print("*********************** 1. type casting *****************")
a=10#int change to 10.0
b=10.5#float
c=a+b#float
print(c)
#add boolean
d=True#this is equal to 1
c=a+b+d
print(c)

print("*********************** 2. using type casting functions (int,float,str,bytes) *****************")

print("*********************** 2.1 using int function *****************")
#using int function
a1=10.4
print(int(a1))#this convert float to int


print("*********************** 2.2 using float function *****************")
#using float function
a2=20
print(float(a2)) 

print("*********************** 2.3 using str function *****************")
#using str function
#string to integer
str1="10"
print(int(str1)) 

print("*********************** 2.4 using bytes function *****************")
#binary string to intger
#binary string 1 and 0 only with base 2
a=int("101101",2) # 
print(a)

print("*********************** 3. using int function with different base *****************")

print("*********************** 3.1 binary to integer *****************")
#binary to integer
a=int("101101",2)
print(a)

print("*********************** 3.2 octal to integer *****************")
#octal to integer
a=int("20",8)
print(a)

print("*********************** 3.3 hexadecimal to integer *****************")
#hexa decimal to integer
a=int("2A4",16)
print(a)

print("*********************** 4. using float and str function *****************")

#using float function
a=float(1.00E4)
print(a)

a=float(1.00E-4)
print(a)

#integer to string
a=str(20)
print(a)

#float to string
a=str(30.45)
print(type(a))

a=str(2.34E-4)
print(a)

print("*********************** 5. using list and tuple function *****************")
#using list() function string to list 
c=("Hello")
list1=list(c)
print(list1)

#String to tuple using tuple function
tuple1=tuple(c)
print(tuple1)

