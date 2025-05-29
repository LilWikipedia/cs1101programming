# #declare my list of 10 employees then split and slice
# employees = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]
# subList1 = employees[:5]
# subList2 = employees[5:]
# subList2.append("Kriti Brown") # Add new employee to 2
# del subList1[1] # Remove the second employee from 1
# merged_list = subList1 + subList2 # Merge
# salary_list = [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000] # a salary list
# salary_list.append(63000) #adding a salary
# updatedsalarylist = [salary * 1.04 for salary in salary_list] # four percent raise
# sorted_salary_list = sorted(updatedsalarylist, reverse=True) # sort and reverse
# top_3_salaries = sorted_salary_list[:3] # get top 3

# # results
# print("SubList1=", subList1)
# print("SubList2=", subList2)
# print("Merged List=", merged_list)
# print("Updated Salary List=", updatedsalarylist)
# print("Top 3=", top_3_salaries)

#
sentence = input()

# Step 1: Convert sentence into word list
word_list = sentence.split()

# Step 2: Reverse the word list
reversed_word_list = word_list[::-1]

# Output
print("Original Sentence:", sentence)
print("Word List:", word_list)
print("Reversed Word List:", reversed_word_list)
