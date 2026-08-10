age = input("Enter your age: ")  # Taking input from user
print("Your age is:", age)  # Outputting the input value

boy_name = input("Enter your name: ")  # Taking input from user
boy_age = input("Enter your age: ")  # Taking input from user
print("Hello", boy_name, "! You are", boy_age, "years old.")
girl_name = input("Enter your girlfriend's name: ")  # Taking input from user   
girl_age = input("Enter your girlfriend's age: ")  # Taking input from user
print("Hello", girl_name, "! You are", girl_age, "years old.")  
age_difference = int(boy_age) - int(girl_age)  # Calculating the age difference 
print("The age difference between", boy_name, "and", girl_name  , "is", age_difference, "years.")  # Outputting the age difference      
print("Hello", boy_name, "and", girl_name, "!")  # Outputting the input values   

print("Hello " + boy_name + " and " + girl_name + "!")  # Outputting the input values using string concatenation
print(f"Hello {boy_name} and {girl_name}!")


