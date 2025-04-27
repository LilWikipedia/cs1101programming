# Positive/Negative option countdown Question 1

# Standard count down based on script from section 5.8 of the textbook
def down(n):
    """Standard count down, from n to `Go!`"""
    if n <= 0:
        print('Go!')
    else:
        print(n)
        down(n-1)


def up(n):
    """This function counts up from a negative n to `Go!`"""
    if n >= 0:
        print('Go!')
    else:
        print(n)
        up(n+1)

# Get user input
try:
    num = int(input("Enter an integer: "))

    # cheking if user input number is a positive int
    if num > 0:
        print(f"\nCalling countdown({num}):")
        down(num)
    # 'else if' branch if user input is a negative integer
    elif num < 0:
        print(f"\nCalling countup({num}):")
        up(num)
    # now if both of the above statements fail (meaning user input == 0)
    else: 
        print(f"\nCalling countdown({num}) for input 0:")
        # Choice for zero: calling countdown
        down(num)

except ValueError:
    print("Invalid input. Please enter an integer.")