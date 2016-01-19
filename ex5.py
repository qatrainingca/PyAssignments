#!/usr/bin/python
from string import maketrans
print "Assignment on translating strings"

str1 = raw_input ("Enter any string :")
intab = "bcdfghjklmnpqrstvwxyz"
outtab = "123456789!@#$%^&*()-+"
transtr1 = maketrans(intab, outtab)
print str1.translate(transtr1)
print "End of assignment"
