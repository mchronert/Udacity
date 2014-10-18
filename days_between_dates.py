#!/usr/local/bin/python

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def is_leap(year): #determines if the input year is a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
Month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def YTD(y,m,d): #determines how many days in the current year so far
    start = 0
    month_count = 0 
    while start < m-1: # -1 becuase month days list starts at 0
        if is_leap(y) == True and start == 1: #account for feb in leap years
            month_count += Month_days[start]+1
        else:
            month_count += Month_days[start]
        start += 1
    return d + month_count

  
        
def days_remain_year(y,m,d): #how many days are remaining in the year
    return 365 - YTD(y,m,d)
    
def year_diff_days(year1,year2): #how many days between years assuming years are NOT adjacent
    day_count = 0
    if year2 == year1 or year2-year1 == 1:
        return 0
    else:
        while year2-1 > year1:
            if is_leap(year2 - 1) == True:
                day_count += 366
            else:
                day_count += 365
            year2 -= 1
        return day_count
      
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1 == year2: #if same year, take difference of YTD
        return YTD(year2,month2,day2)-YTD(year1,month1,day1)
    if year2 - year1 == 1: #if years adjacent, take YTD in current and remaining in last
        return YTD(year2,month2,day2) + days_remain_year(year1,month1,day1)
    else: #if years NOT adjacent sum YTD, remaining and days in the years between
        return YTD(year2,month2,day2) + days_remain_year(year1,month1,day1) + year_diff_days(year1,year2)


# Test routine: this was copied from the Udacity question

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
