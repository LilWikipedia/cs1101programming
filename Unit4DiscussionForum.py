#Precondition

# def PreconditionViolation(BadArg):
#     print("This is an example of a precondition violation")
    
# PreconditionViolation()

#Postcondition

# def PosconditionViolation(a, b):
#     print("This is an example of a postcondition violation")
#     a = 1
#     b = 1
#     result = a+b 
#     if result != 10:
#         print("Postcondition violated because the result is not equal to ten")
#     return result

# PosconditionViolation(1,1)


#Return value violation

def ReturnValueViolation(a, b):
    print("This is an example of a return value violation")
    a = 1
    b = 1
    result = a + b 
    if result != 10:
        print("Return value violated because the result is not equal to ten")
    return result

ReturnValueViolation(1, 1)# will raise an exception because 1 + 1 != 10
