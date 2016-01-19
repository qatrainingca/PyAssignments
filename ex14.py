#!/usr/bin/python
print "Number of words length"
list1 = input("Enter any words of list separated by commas :")
print list1




newlist = [len(str(element)) for element in list1]
print newlist
print list1[2]
