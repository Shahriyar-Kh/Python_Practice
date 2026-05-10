#identity op two is and is not use for matching but when memory address same

print("*********************** Identity operator in python *****************")
#Identity operator in python
#Identity operators are used to compare the memory location of two objects. In python, we have two identity operators that can be used to perform different operations on the variables. The most common identity operators are is and is not. The is operator returns true if both operands refer to the same object in memory, while the is not operator returns true if both operands do not refer to the same object in memory.

a="shahriyar"
b=a
#Print the memory address of a and b 
print("id(a) and id(b)=",id(a)," and ",id(b))
#using is operator for identity
print("a is b:",a is b)#true
#using is not operator for identity
print("a is not b:",a is not b)#false


#using list
a=[1,2,3]
b=[1,2,3]

print("a is b = ", a is b)#false
print("a is not b= ", a is not b)#true
