#concatination of string
first_name = "John"
last_name = "Doe"   
full_name = first_name + " " + last_name  # Concatenating first name and last name
print("Full Name:", full_name)  # Outputting the concatenated full name 

#repetition of string
message = "warning! "
print(message*100)  # Outputting the message 100 times

print(message.upper())  # Outputting the message in uppercase
print(message.lower())  # Outputting the message in lowercase
print(message.capitalize())  # Outputting the message with the first letter capitalized
print(message.title())  # Outputting the message in title case
print(message.strip()*2)  # Outputting the message with leading and trailing whitespace removed
print(message.replace("warning", "alert"))  # Replacing "warning" with "alert" in the message
print(message.split("!"))  # Splitting the message into a list using "!" as the delimiter
print(message.find("warning"))  # Finding the index of "warning" in the message
print(message.count("warning"))  # Counting the occurrences of "warning" in the message
print(message.startswith("warning"))  # Checking if the message starts with "warning"
print(message.endswith("!"))  # Checking if the message ends with "!"
print(message.isalpha())  # Checking if the message contains only alphabetic characters
print(message.isdigit())  # Checking if the message contains only digits
print(message.isalnum())  # Checking if the message contains only alphanumeric characters
print(message.islower())  # Checking if the message is in lowercase
print(message.isupper())  # Checking if the message is in uppercase
print(message.isspace())  # Checking if the message contains only whitespace characters
print(message.isprintable())  # Checking if the message is printable
print(message.isidentifier())  # Checking if the message is a valid identifier
print(message.isnumeric())  # Checking if the message contains only numeric characters
print(message.isdecimal())  # Checking if the message contains only decimal characters


print(len(message))  # Outputting the length of the message

#indexing and slicing of string
message = "Hello, World!"   
print(message[0])  # Outputting the first character of the message
print(message[-1])  # Outputting the last character of the message  
print(message[0:5])  # Outputting the first 5 characters of the message
print(message[7:])  # Outputting the characters from index 7 to the             
print(message[:5])  # Outputting the first 5 characters of the message
print(message[::2])  # Outputting every second character of the message
print(message[::-1])  # Outputting the message in reverse order
print(message[1:10:2])  # Outputting every second character from index 1 to 10 of the message
print(message[::3])  # Outputting every third character of the message
print(message[1::2])  # Outputting every second character starting from index 1 of the message
print(message[::4])  # Outputting every fourth character of the message
#[start:stop:step]


s = "Python Programming"
s = "Python \nProgramming" # newline character
s = "Python \tProgramming" #tab character
s = "Python \rProgramming" #carriage return character
s = "Python \bProgramming" #backspace character
s = "Python \fProgramming"# form feed character
s = "Python \vProgramming" #vertical tab character
s = "Python \aProgramming" #alert character
s = "Python \0Programming" #null character
s = "Python \x50Programming" #hexadecimal character
s = "Python \u0050Programming" #unicode character

print(s)