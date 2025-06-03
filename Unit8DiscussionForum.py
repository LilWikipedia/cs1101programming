
# the try branch contains logic for the opening of a file

try:
    with open("a_random_file.txt", "r") as randomfile:
        I_love_cs1101 = randomfile.read()
        print(I_love_cs1101)
        
# the except block is thrown if the try logic fails, hence `try`

except FileNotFoundError:
    print("problem opening file, so this branch is thrown instead of program crashing")
