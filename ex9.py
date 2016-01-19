#!/usr/bin/python
list1 =raw_input("Enter list of values separated by commas :")
list1 = eval(list1)
print list1
num = input("Enter any value to check in or not in list :")
if (num in list1):
    print "Number is in list"
else:
    print "Number not in list"
print "End of assignment"
