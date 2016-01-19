#!/usr/bin/python
#def palindrome(str1):
#    str1 == str1[::-1]
#    return str1
print "Recognise Palindrome"
str1 = raw_input ("Enter any string :")
if (str1 == str1[::-1]):
    print "String is a palindrome"
else:
    print "String is not a palindrome"
print "End of assignment"
