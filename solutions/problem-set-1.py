#!/usr/bin/env python2.7
# Problem Set 0
# Name: Sisi Wei

# 1
def copycat(input):
    print input

# 2

def addition(x, y, z):
    print x + y + z

# 3

def conversion(f):
    print (f-32)*5.0/9

# 4

def find_the_max(x, y, z):
    biggest = x
    print "Starting out"
    print biggest

    if y > biggest:
        biggest = y
        print "y is bigger"
        print biggest

    if z > biggest:
        biggest = z
        print "z is bigger"
        print biggest

# 5
def total_students():
    pupils_by_year = [["first years", 40], ["second years", 40], ["third years", 38]]

    # total_pupils = pupils_by_year[0][1] + pupils_by_year[1][1] + pupils_by_year[2][1]

    total_pupils = 0

    for year in pupils_by_year:
        total_pupils = total_pupils + year[1]
        print total_pupils

total_students()















