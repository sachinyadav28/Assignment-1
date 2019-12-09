#Write a Python program that accepts a comma-separated sequence of words as input
#and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#>> orange,apple,mango,grapes
#Then, the output should be:
#>> apple,grapes,mango,orange
x = input("Enter fruits with comma separated ")
y = x.split(",")
y = sorted(y)
print(",".join(y))
