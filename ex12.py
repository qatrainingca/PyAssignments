#!/usr/bin/python
print "Genrating histogram"
list1 = raw_input ("Enter list of values separated by commas :")
list1 = eval(list1)
print list1
char1 = raw_input("Enter any character :")
for item in list1:
    print item * char1
print "End of assignment"
