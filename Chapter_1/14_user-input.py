#User Input in python
#User input is a way to get data from the user. In python, we can use the input() function to get input from the user. The input() function takes a string as an argument and displays it to the user as a prompt. The user can then enter a value, which is returned as a string.


print("*********************** User Input in python *****************")
#Example
name="Shahriyar"
city="karachi"
print("Hello my name is",name)
print("i am from ",city)


#using input function
name1=input("Enter the name: ")
city1=input("Enter the city name: ")
print("Hello my name is ",name1)
print("i am from ",city1)

#finding area of rectangle using user input
width=int(input("Enter the width: "))
height=int(input("Enter the height: "))
area=width*height
print("Area of rectangle",area)


#finding interest rate using float()
amount=float(input("Enter Amount: "))
rate=float(input("Enter rate of interest: "))
interest=amount*rate/100
print(f"Amount of {amount} interest is :{interest}")
