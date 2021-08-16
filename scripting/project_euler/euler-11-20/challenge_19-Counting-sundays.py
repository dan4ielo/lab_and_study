# You are given the following information

# 1 Jan 1900 was a Monday. - It was actually a Tuesday

# 31 days - Jan, Mar, May, Jul, Aug, Oct, Dec
# 30 days - Apr, Jun, Sep, Nov - They skipped September
# 28-29 days - Feb

# A leap year occurs on any year evenly divisible by 4, but not on a century (100) unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

months = {
'Jan':31,
'Feb':28,
'Mar':31,
'Apr':30,
'May':31,
'Jun':30,
'Jul':31,
'Aug':31,
'Sep':30,
'Oct':31,
'Nov':30,
'Dec':31
}

years = [_ for _ in range (1901, 2001)]
sundays = 0
day_of_the_week = 2
for year in years:
    if year % 4 == 0: # Select a leap year
        months['Feb'] = 29 # Make Feb have 29 days
        # cycle through the months
        for month in months: # month = Jan
            day_of_the_month = 1
            while day_of_the_month <= months[month]:
                if day_of_the_week == 7 and day_of_the_month == 1:
                    day_of_the_week = 0
                    sundays += 1
                if day_of_the_week == 7: 
                    day_of_the_week = 0
                day_of_the_week += 1
                day_of_the_month += 1
        months['Feb'] = 28 # Reset Feb
    else:
        # cycle through the months
        for month in months: # month = Jan
            day_of_the_month = 1
            while day_of_the_month <= months[month]:
                if day_of_the_week == 7 and day_of_the_month == 1:
                    day_of_the_week = 0
                    sundays += 1
                if day_of_the_week == 7: 
                    day_of_the_week = 0
                day_of_the_week += 1
                day_of_the_month += 1

# That counts all sundays you moron ... You need Sundays on the 1st of a month
#for year in years:
#    if year % 4 == 0: # Select a leap year
#        months['Feb'] = 29 # Make Feb have 29 days
#        # cycle through the months
#        for month in months: # month = Jan
#            day_of_the_month = 1
#            while day_of_the_month <= months[month]:
#                if day_of_the_week == 7: 
#                    sundays += 1
#                    day_of_the_week = 0
#                day_of_the_week += 1
#                day_of_the_month += 1
#        months['Feb'] = 28 # Reset Feb
#    else:
#        # cycle through the months
#        for month in months: # month = Jan
#            day_of_the_month = 1
#            while day_of_the_month <= months[month]:
#                if day_of_the_week == 7: 
#                    sundays += 1
#                    day_of_the_week = 0
#                day_of_the_week += 1
#                day_of_the_month += 1

print (sundays)
