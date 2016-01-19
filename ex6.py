#!/usr/bin/python
def product_list(list1):
    product = 1
    for item in list1:
        product *= item
    return product

print "sum and multiply "

list1 = raw_input("Enter your list of values separated by commas :")
list1 = eval(list1)
print list1

key = raw_input("Enter + or * :")

if key == '+' :
    print "using sum operation"
    print "Sum is :" , sum(list1)
else:
    key == '*'
    print "using product operation"
    print "product is :" , product_list(list1)
print "End of assignment"
