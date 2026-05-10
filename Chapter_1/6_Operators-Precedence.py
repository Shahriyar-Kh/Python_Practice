#Operator Precedence in python
#Operator precedence is the order in which operators are evaluated in an expression. In python, the operator precedence is determined by the following rules:
#1. Parentheses: expressions inside parentheses are evaluated first.    
#2. Exponentiation: the ** operator is evaluated next.
#3. Multiplication, division, and modulus: the *, /, and % operators are evaluated next.
#4. Addition and subtraction: the + and - operators are evaluated next.


a,b,c,d,e=5,6,16,8,0

question1=(a+b)*c/d # question1=11*16/8=11*2=22
print("the result of (a+b)*c/d=",question1)

question2=((a+b)*c)/d# question2=(11*16)/8=176/8=22
print("the result of ((a+b)*c)/d=",question2)

question3=(a+b)*(c/d)# question3=(11)*(2)=22
print("the result of (a+b)*c/d=",question3)

question4=a+(b*c)/d# question4=5+96/8=5+12=17
print("the result of (a+b)*c/d=",question4)



