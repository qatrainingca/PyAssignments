#!/usr/bin/python
print "Assignment for max of 3 numbers"
a = input ("Enter a value :")
b = input ("Enter b value :")
c = input ("Enter c value :")
if (a>b):
    if (a>c):
        print "Max value is a"
    else:
        print "Max value is c"
else:
    if (b<c):
        print "Max value is c"
    else:
        print "Max value is b"
