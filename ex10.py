#!/usr/bin/python
print "checks numbers are in common are not "
list1 = raw_input("Enter numbers in 1st list separated by commas:")
list1 = eval(list1)
print list1
list2 = raw_input("Enter numbers in 2nd list separated by commas:")
list2 = eval(list2)
print list2
#for num1 in list1:
#    for num2 in list2:
#        if (num1 == num2):
#            print "num is in list"
#        else:
#            print "num is not list"
if set(list1) & set(list2):
    print "Number was found"
else:
    print "Number not in list"
print "End of assignment"
