# # Positive/Negative option countdown Question 1

# # Standard count down based on script from section 5.8 of the textbook
# def down(n):
#     """Standard count down, from n to `Go!`"""
#     if n <= 0:
#         print('Go!')
#     else:
#         print(n)
#         down(n-1)


# def up(n):
#     """This function counts up from a negative n to `Go!`"""
#     if n >= 0:
#         print('Go!')
#     else:
#         print(n)
#         up(n+1)

# # Logic
# try:
#     count_number = int(input("enter a number:"))

#     # cheking if user input count_numberber is a positive int
#     if count_number > 0:
#         print(f"\nCalling countdown({count_number}):")+
#         down(count_number)
#     # 'else if' branch if user input is a negative integer
#     elif count_number < 0:
#         print(f"\nCalling countup({count_number}):")
#         up(count_number)
#     # now if both of the above statements fail (meaning user input == 0)
#     else: 
#         print(f"\nCalling countdown({count_number}) for input 0:")
#         # Choice for zero: calling countdown
#         down(count_number)

# except ValueError:
#     print("Invalid input. Please enter an integer.")
# Prompt user to enter two numbers




f1 = float(input("Divide: "))
f2 = float(input("By / :"))

try:
    print("RuntimeLog - Calculating user inputs..")
    ans = f1 / f2
    print("RuntimeLog - Results found!")
    print(f"RuntimeLog - {f1} / {f2} = {ans}")
except ZeroDivisionError:
    print("ErrorLog - Impossible Request `ZeroDivisionError` Cannot divide by 0")