# Getting input from user
kata = input("Enter a sentence = ")
# Initializing variables
count = 0
# Counting the number of words in the input string
for i in range(len(kata)):
    if kata[i] == ' ':
        count += 1
# Displaying the count of words in the input string
print("Word count =", count+1)