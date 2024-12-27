#Nabems first assignment, which has been dew for way too long....

#"""
# A Palindrome is a word or number that can be read the same backwards.
# Examples are 'madam','kayak','radar','121','434', ETC.
# This code determines whether am integer or a string is a palindrome or not
# """

word = input("Enter a word or value:")
#in this case the user can enter a word or integer which will both be read as strings.

reverse = word [::-1]
#"""
# here the slicing method is used.

if word == reverse:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")


