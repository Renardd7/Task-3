#coding to make right triangle
num = int(input("Number:")) #take user input, change the str to int
for b in range(1, num + 1): 
#'range()' function is used to generate sequence of numbers which are then used as the loop variable in a for loop
    for k in range(1, b + 1): #in this we start from 1 and go up to 'num'
        if b == num or k == b or k == 1: #this is the condition to check if the conditions is true
            print('* ',end='') #use '*' to print the triangle
        else:
            print('  ',end='') #and make a blank space so it's not interrupted 
    print() #statement outside the inner loop to print a newline character
        