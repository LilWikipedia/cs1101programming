#1
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# This function iterates through the input string 's', checking only the first letter. 
# If the first character is lowercase, it returns True. Otherwise, it returns False. 
# It stops after the first charactar though which is not what we want so this function is not correct.

#2
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# This function is almost identical to the previous example except it iterates through a literal string
# instead. Because there is no change in the logic aside from that, this function also presents incorrect results.

#3
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# This one iterates through the input string 's'. In each iteration, the variable 'flag' is assigned the boolean result
# of checking if the current character 'c' is lowercase. The 'flag' value is overwritten in every step though, so after the loop finishes, 
# the function returns the final value of 'flag', which corresponds to the islower result for the last character of the string.
# this is not whay we want so this is incorrect

#4
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# This example initializes flag to False to start. It goes through the string, updating flag with the logical 'OR' of its current value 
# and islower. This means flag becomes True if it was already True, or if the current character is lowercase. Once flag becomes True- 
# meaning a lowercase character has been found- it will remain True for the rest of the loop. The function returns the final value of flag,
# indicating whether any lowercase character was encountered. This is the correct function.

#5

s="UnitFive"
print(any_lowercase1(s))
print(any_lowercase2(s))
print(any_lowercase3(s))
print(any_lowercase4(s))
print(any_lowercase5(s))
    