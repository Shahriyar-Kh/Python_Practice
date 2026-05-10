#arithmetic operators in python are used to perform mathematical operations on numbers. The arithmetic operators in python are:
#1. + for addition
#2. - for subtraction
#3. * for multiplication
#4. / for division
#5. // for floor division
#6. % for modulus
#7. ** for exponentiation or power


print("*********************** 1. using + operator for addition *****************")
# using + op for addition 
a=4
b=6
c=a+b
#1st method using format function
#formate function is used to format the string and it is used to insert the values in the string. It is a built in function in python and it is used to insert the values in the string using placeholders. The placeholders are represented by {} and the values are inserted in the placeholders using the format function.
print("The addition of {0} and {1} is = {2}".format(a,b,c))


#2nd method
print(f"Result:{a}+{b}={c}")

#3rd method
print(f"Result:{a+b}")


#addition of integer and complix numbers
a1=4+5j
b1=4
c=a1+b1
print("The addition of {0} and {1} is = {2}".format(a1,b1,c))

print("*********************** 2. using - operator for subtraction *****************")
#using - for subtraction
c=a-b
print("The subtraction of {0} and {1} is = {2}".format(a,b,c))


print("*********************** 3. using * operator for multiplication *****************")
#using * for mult
c=a*b
print("The multiplication of {0} and {1} is = {2}".format(a,b,c))

print("*********************** 4. using / operator for division *****************")

#using / for divid but result in float
c=a/b
print(f"Division:{a}/{b}={c} ")


#using double // for divid but result in int
c=a//b
print("Division of {0} and {1} is = {2}".format(a,b,c))

print("*********************** 5. using % operator for modulus *****************")
#using % modulas for remainder
a2=13
b2=5
c=a2%b2
print("The remainder of {0} and {1} is = {2}".format(a2,b2,c))

print("*********************** 6. using ** operator for exponentiation *****************")
#using exponent op ** or power
a3=4+5j
b3=2
c=a3**b3
print("{0} Power {1} is = {2}".format(a3,b3,c))
print("""
      (4+5j)^2=16+40j+25j^2
      Remember that j^2 is equal to -1
      so the expression simplifies to
      16+40j−25=−9+40j
      """)

