#bitwise Operators in python
#Bitwise operators are used to perform bitwise operations on the binary representation of the numbers. In python, we have several bitwise operators that can be used to perform different operations on the binary representation of the numbers. The most common bitwise operators are:
#1. & for bitwise and
#2. | for bitwise or
#3. ^ for bitwise xor
#4. ~ for bitwise not
#5. << for left shift
#6. >> for right shift


print("*********************** 1. using & operator for bitwise and *****************")
#using and(&) operator
"""
0 & 0 is 0
1 & 0 is 0
0 & 1 is 0
1 & 1 is 1 # means both bits are 1 then only result is 1 otherwise 0

"""
a=60
b=13
c=a&b
print("a&b = {0} & {1} is ={2} ".format(a,b,c))
#understanding the above code
print("a:",bin(a))#00111100
print("b:", bin(b))#001101
"""
a: 0b111100
b: 0b1101
so 
0011 1100 & 0000 1101=0000 1100=12
    """
print(int("1100",2))#output 12 : in simple calculation  0*2^3+0*2^2+1*2^1+1*2^0=12


 
print("*********************** 2. using | operator for bitwise or *****************")
#Betwise OR (|) operator
"""
0 | 0 is 0
0 | 1 is 1
1 | 0 is 1
1 | 1 is 1 # means at least one bit is 1 then result is 1 otherwise 0
"""
d=a|b
print("a|b(a or b) {0}|{1} is ={2}".format(a,b,d))
#understanding the working 
"""
0011 1100 |(OR) 0000 1101= 0011 1101=61
    """
print("00111101=",int("00111101",2))#61


print("*********************** 3. using ^ operator for bitwise xor *****************")
#Binary XOR Operator (^) 

"""
0 ^ 0 is 0
0 ^ 1 is 1
1 ^ 0 is 1
1 ^ 1 is 0 # means bits are different then result is 1 otherwise 0
    """
e=a^b
print("a^b(a XOR b) {0} ^ {1} is= {2}".format(a,b,e))
#understanding the working
"""
0011 1100 ^(XOR) 0000 1101= 00110001=49
    """
print("00110001=",int("00110001",2))#49


print("*********************** 4. using ~ operator for bitwise not *****************")
#Binary NOT Operator (~)
#first convert to bits then flips those bits 0 to 1 and 1 to 0
f=~a
print("~a (NOT a) ~{0} is ={2} ".format(a,a,f))
#understanding working
"""
a=60=0011 1100
so ~a=1100 0011= -61
"""
print(int("11000011",2))#-61


print("*********************** 5. using << operator for left shift *****************")

#Left Shift Operator (<<)
#
a=16
b=2
g=a<<b
print("a<<b {0} << {1} is={2}".format(a,b,g))
#understanding working 

"""
print(bin(a))#10000
print(bin(b))#10

10000 << 2=1000000=64

print(int("1000000",2))
"""
#Right Shift Operator (>>)
a=16
b=2
h=a>>b
print("a>>b {0} >> {1} is={2}".format(a,b,h))
"""
print(bin(a))#10000
print(bin(b))#10

10000 >> 2=100=4

print(int("100",2))
"""
#Binary NOT Operator (~)
#first convert to bits then flips those bits 0 to 1 and 1 to 0
a1=8
a2=~a1
print("a1: {0} to ~{1} is ={2} ".format(a1,a1,a2))
#understanding working
"""
8=1000=~0000 0111=1111 0111
"""
print(int("11110111",2))
