#list
items = ["apple", "banana", "cherry"]
print(items)  # Outputting the list of items

#indexing and slicing of list
print(items[0])  # Outputting the first item in the list
print(items[-1])  # Outputting the last item in the list        

l = [1, "two", 3.0, True, [5, 6, 7]]  # A list containing different data types
print(l)  # Outputting the list with different data types   

items = ["apple", "banana", "cherry", "date", "elderberry"]
print(items[1:4])  # Outputting items from index 1 to 3
items.pop()  # Removing the last item from the list
print(items)  # Outputting the list after removing the last item
items.pop(1)  # Removing the item at index 1 from the list
print(items)  # Outputting the list after removing the item at index 1
items.append("fig")  # Adding a new item to the end of the list
print(items)  # Outputting the list after adding a new item
items.insert(1, "grape")  # Inserting a new item at index 1
print(items)  # Outputting the list after inserting a new item
items.remove("grape")  # Removing the item "banana" from the list
print(items)  # Outputting the list after removing "banana"
items.sort()  # Sorting the list in ascending order
print(items)  # Outputting the sorted list
items.reverse()  # Reversing the order of the list
print(items)  # Outputting the reversed list
items[0] = "kiwi"  # Changing the first item in the list to "kiwi"
print(items)  # Outputting the list after changing the first item
print(len(items))  # Outputting the length of the list

numbers = [5, 2, 9, 1, 5, 6]
# Sorting the list in ascending order   
print(sorted(numbers))  # Outputting the sorted list without modifying the original list
print(sum(numbers))  # Outputting the sum of all items in the list

print(items.count("apple"))  # Counting the occurrences of "apple" in the list      
print(items.index("cherry"))  # Finding the index of "cherry" in the list


#nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # A list containing other lists
print(nested_list)  # Outputting the nested list    