def unit_5(n):
    length = len(n)
    reversed_string = n[::-1]
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in n:
        if char in vowels:
            vowel_count += 1
            
    return length, vowel_count, reversed_string
    
n = input("enter name:")
length, vowel_count, reversed_string = unit_5(n)
print("Length of my name:", length)
print("Number of vowels in my name:", vowel_count)
print("Reversed:", reversed_string)
unit_5


























    # Initialize vowel count.


    # Define a string containing all vowels (both lowercase and uppercase).


    # Iterate through the string to count vowels.
    # A 'for' loop iterates over each character in the string.
    # The 'in' operator checks if a character is present in the 'vowels' string.


    # Reverse the string.  String slicing with a step of -1 creates a reversed copy.
    

    


# Get input



    # This function takes a string as input, calculates its length,
    # counts the number of vowels, and reverses the string.

    # Args:
    #     n: The input string (user name).

    # Returns:
    #     A tuple containing:
    #     - The length of the string.
    #     - The number of vowels in the string.
    #     - The reversed string.
    # """

    # # Strings in Python are immutable sequences of characters.  We can access
    # # individual characters using indexing (e.g., n[0] is the first character).
    # # The len() function returns the number of characters in a string.