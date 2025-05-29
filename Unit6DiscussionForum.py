# Here i demonstrate the difference between object equivalence, and identity using lists.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 references the same object as list1

print("List1:", list1)
print("List2:", list2)
print("List3:", list3)

print("\nEquivalence and Identity:")
print("list1 == list2:", list1 == list2)  # expected result: True because list1 and list2 have the same value
print("list1 is list2:", list1 is list2)  # expected result: False because list1 and list2 are different objects in memory
print("list1 == list3:", list1 == list3)  # expected result: True because list1 and list3 have the same value
print("list1 is list3:", list1 is list3)  # expected result: True because list1 and list3 are the same object

print("\nAliasing:")
list1.append(4)  # Modifying list1 also modifies list3 because they are the same object
print("List1 after modification:", list1)
print("List3 after modification:", list3)  # list3 is also changed because it's an alias of list1
print("List2 after modification:", list2) # List2 remains unchanged because it's a different object

# function that modifies list:
def modify_list(my_list):  # my_list is a parameter of the function
    """This function modifies a list by appending the value 5 to it."""
    my_list.append(5) # Modifies the object referenced by my_list

# usage
original_list = [6, 7, 8] # original_list is an argument
print("\nOriginal List before function call:", original_list)
modify_list(original_list)  # Passing the list as an arg
print("Original List after function call:", original_list)  # The original list is modified, desired result

# #  Breakdown # # 
# - Argument: original_list
# - Parameter: my_list
# - Object: The actual list [6, 7, 8] in memory is the object in this example.
# - Reference: original_list and my_list are both references to the same list object in memory,
#   but when the function modifies my_list, it's actually modifying the object that original_list refers to,
#   which is why the change is reflected outside the function.
