genders =("male", "female", "other")
print(genders)  # Outputting the tuple of genders
print(type(genders))  # Outputting the type of the variable 'genders'
print(len(genders))  # Outputting the length of the tuple 'genders'
print(genders[0])  # Outputting the first item in the tuple 'genders'
print(genders[-1])  # Outputting the last item in the tuple 'genders'

#tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2  # Concatenating two tuples
print(result)  # Outputting the concatenated tuple

#tuple repetition
tuple3 = ("Hello",) 
result = tuple3 * 3  # Repeating the tuple three times      
print(result)  # Outputting the repeated tuple

 #membership  tuple
print(1 in tuple1)  # Checking if 1 is in tuple1

#counting occurrences in tuple
tuple4 = (1, 2, 3, 1, 2, 1)
count_1 = tuple4.count(1)  # Counting the occurrences of 1 in tuple4
print(count_1)  # Outputting the count of occurrences of 1 in tuple4    

#matrix representation using tuple  
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))  # A tuple of tuples representing a matrix
print(matrix)  # Outputting the matrix  

#sets
fruits = {"apple", "banana", "cherry"}  # A set of fruits
print(fruits)  # Outputting the set of fruits

#unordered sets
numbers = {1, 2, 3, 4, 5}  # A set of numbers
print(numbers)  # Outputting the set of numbers # set is unordered, so the order of elements may vary each time you run the 

#set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Union of two sets       
print(union_set)  # Outputting the union of set1 and set2
intersection_set = set1.intersection(set2)  # Intersection of two sets  
print(intersection_set)  # Outputting the intersection of set1 and set2
difference_set = set1.difference(set2)  # Difference of two sets
print(difference_set)  # Outputting the difference of set1 and set2
print(set1 | set2)  # Outputting the union of set1 and set2 using the '|' operator
print(set1 & set2)  # Outputting the intersection of set1 and set2
print(set1 - set2)  # Outputting the difference of set1 and set2 using the '-' operator

#methods of set
fruits.add("date")  # Adding an item to the set
print(fruits)  # Outputting the set after adding an item
fruits.remove("banana")  # Removing an item from the set
print(fruits)  # Outputting the set after removing an item
fruits.discard("cherry")  # Discarding an item from the set
print(fruits)  # Outputting the set after discarding an item
fruits.pop()  # Removing and returning an arbitrary item from the set
print(fruits)  # Outputting the set after popping an item
