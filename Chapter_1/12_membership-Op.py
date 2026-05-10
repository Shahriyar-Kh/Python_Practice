#Membership operator in python
#Membership operators are used to check if a value is present in a sequence (such as a string, list, or tuple) or not. In python, we have two membership operators that can be used to perform different operations on the variables. The most common membership operators are in and not in.

print("*********************** 1. using in operator for membership *****************")
#using two op in not in return boolean value
print("************************ 1.1 using in operator for membership in string *****************")
string="Shahriyar khan"
a="khan"
b="jan"
print(f"{a} in {string}=",a in string) 
print(f"{b} in {string}=",b in string) 


print("*********************** 1.2 using not in operator for membership  in list *****************")
#using not in op for membership 
#using list
list=[2,4,6,8,10]
a=2
b=3
c=a in list
print("{0} in {1} ={2}".format(a,list,c))
print(f"{b} in {list} = {b in list}")

print("*********************** 1.3 using in operator for membership in tuple *****************")
#using dictionary   
dict={1:"khan",2:40,3:10,3:4,4:6}
a=2
b=40
print(f"{a} in {dict} ={a in dict}")
print(f"{b} in {dict} ={b in dict}")

print("*********************** 2. using not in operator for membership in set *****************")
#using not in op for membership 
#using set
set={1,2,3,4,5}
a=2
b=6
print(f"{a} not in {set} = {a not in set}")
print(f"{b} not in {set} = {b not in set}")

