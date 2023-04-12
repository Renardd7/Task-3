#The program is making letter 'I'
ans = 0  # initialize jawab to 0

# keep asking for input until an odd number is entered
while ans % 2 == 0:
    ans = int(input("Input odd number = "))
    if ans % 2 == 0:
        print("Wrong input")

# use a nested for loop to print the pattern
for b in range(1, ans+1):
    for k in range(1, ans+1):
        if b == 1 or b == ans or k == ans//2+1:
            # if b is the first or last row or k is in the middle column,
            # print an *
            print("* ", end="")
        else:
            # otherwise, print two spaces
            print("  ", end="")
    print() 
