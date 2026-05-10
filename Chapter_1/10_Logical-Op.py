#Logical operator in python
# Logical operators are used to combine conditional statements. In python, we have three logical operators that can be used to perform different operations on the variables. The most common logical operators are and, or, and not.
# 1. and operator is used to check if both the conditions are true. If both the conditions are true, then the result is true, otherwise the result is false.
# 2. or operator is used to check if at least one of the conditions is true
# 3. not operator is used to check if the condition is false. If the condition is false, then the result is true, otherwise the result is false. 


print("*********************** 1. using and operator *****************")

x=10
y=20

#using and logical op both condition true then true
print("x>0 and x<10 = ",x>0 and x<10)#T and F=F
print("x>0 and y>10 = ",x>0 and y>10)# T and T=T
print("x%2==0 and y%2==0 = ",x%2==0 and y%2==0)#T and T=T

print("*********************** 2. using or operator *****************")
#using or logic at least one true then true 
print("\nx>0 or x<10 = ",x>0 or x<10)# F or T=T
print("x>0 or y>10 = ",x>0 or y>10)#T or T=T
print("x<0 or x<10 = ",x<0 or x<10)#F or F=F


print("*********************** 3. using not operator *****************")
#using not operator if condition false then true
print("\nnot(x>0) = ",not(x>0))#F
print("not(x<0) = ",not(x<0))#T




