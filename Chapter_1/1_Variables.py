#Variable

print("**********************1. Creating variable *************************")
#1. Creating varaible and print data
#creates integer variable
a=12
#create string variable
b="Shahriyar Khan"
#create float variable
c=12.3
print(a)
print(b)
print(c)
#same output
print(a,b,c)

print("*********************** 2. print the stored value id *****************")
#2. When value is stored in memory fetching the data from its ID
str1="Shahriyar"
#print(str1)
print(id(str1))
print("*************** 3. delete python variable **********")
#3. delete python variable
del a
#deleted show nameError
#print(a)
print("*********************** 4. multiple variable in one statement *****************")
#4. multiple variable in one statement or same value assign to multiple variable 
#same value assign to multiple varaible
var1=var2=var3=1
# create multiple varaible with different values at a time
var4,var5,var6=5,14,10
#multiple values print in one statments
print(var1,var2,var3,var4,var5,var6)

print("*********************** 5.using naming convention*****************")

#using naming convention
#1.start from letter or underscore
__var1=12
print(__var1)
#invalid

#%var1,1var,keywords if else etc
#using naming pattrens
varOne,VarOne,var_one="CamelCase","PascalCase","Snackcase"

#operator is returns True if both the operands have same id() value.
var1 is var2 is var3 
print(id(var1),id(var2),id)



