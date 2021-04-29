# File: mdcal.py
# Author: Paul Beach
# Date: 4/29/21
#
# This script creates a calendar in markdown formatted output, with embedded links for my daily journal in Obsidian
# Inspired by https://github.com/pn11/mdcal/blob/master/mdcal.py
# Run: python3 mdcal.py <year>

import calendar
import datetime
import sys

def create_calendar(year, month):
    mdstr = ""
    cal = calendar.Calendar(firstweekday=6)
    colnames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
       
    mdstr += '|' + '|'.join(colnames) + '|' + '\n'
    mdstr += '|' + '|'.join([':-:' for _ in range(len(colnames))]) + '|'

    for days in cal.monthdays2calendar(year, month):
        for d in days:
            if d[1] == 6:
                mdstr += '\n'
            if d[0] == 0:
                mdstr += '| '
            else:
                day = d[0]
                date = datetime.datetime(year, month, day)
                custom = "[[" + custom_strftime('%A, %B {S} %Y', date) + "\|" + str(day) + "]]"
                mdstr += '|' + custom
    return mdstr

def suffix(d): # https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

if __name__ == "__main__":
    argv = sys.argv
    year = int(argv[1])
    for month in range(1, 13):
        month_year = datetime.datetime(year, month, 1)
        print(month_year.strftime("%B, %Y\n"))
        print(create_calendar(year, month))
