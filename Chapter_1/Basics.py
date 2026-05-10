#Print the full keyword list using keyword.kwlist.
import keyword
print(keyword.kwlist)

# Write a docstring for a function. 
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add.__doc__)

#Variable Questions
#Swap two variables without a third variable.
a=5
b=6
a,b=b,a
print(a)
print(b)

#Store student data in 5 variables.
name="shary"
role_num=24
age=34
class_no=8
books=5
#Change the value of a variable 3 times and print each result. 
value1=45
print(value1)

value2=4
print(value2)
value3=43
print(value3)

#Types
x = 10
name = "Sara"
flag = True
print(type(x))
print(type(name))
print(type(flag))

#Types casting
age_text = "21"
age = int(age_text)
price = float("99.5")
score = str(100)
a="20"
print(age + 1)
print(price)
print(str(score))
print(a)


#Print()
print("A", "B", "C", sep="-")
print("Hello", end=" ")
print("World")
print("Hello \n Word")

#membership

print('a' in 'cat')
print(3 in [1, 2, 3])
print('x' not in 'python')

#len()
print(len('Python'))
print(len([1, 2, 3]))
print(len({'a': 1, 'b': 2}))


#range()
print(list(range(5)))
print(list(range(2, 8)))
print(list(range(1, 10, 2)))


#try catch

try:
     n = int(input('Enter: '))
     print(10 / n)
except ValueError:
     print('Invalid input')
except ZeroDivisionError:
     print('Cannot divide by zero')


try:
    x = 10 / 0
except ZeroDivisionError:
     print('Handled')
finally:
     print('Always runs')
 

