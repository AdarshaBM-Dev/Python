a = 10 
b = 20

print(a+b)

a , b ,c = 10, 20, 30
a = b = c = 10

#data types
name = "John" #string
age = 30 #int
height = 5.9 #float
is_student = True #boolean

print(type(name))
print(type(age))
print(type(height)) 
print(type(is_student))


#dynamic typing
is_student = "yes" #string
print(type(is_student)) #string

#type casting
age_float = float(age) #casting int to float
print(type(age_float)) #float
print(age_float) #30.0  

s="100"
print(int(s)+age) #casting string to int and adding to 

#arithmetic operations
x = 10  
y = 3
print(x + y)  # Addition    
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor Division
print(x % y)  # Modulus or riemainder
print(x ** y) # Exponentiation

#swapping values
a = 5
b = 10
a, b = b, a  # Swapping values using tuple unpacking
print(a, b)
print("a:", a)  # Output: a: 10
print("b:", b)  # Output: b: 5  
