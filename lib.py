# Chapter 1

#exercise 7
"""
In the United States, a car fuel efficiency is measured in miles
per gallon. In the metric system, it is usually measured in liters
per 100 kilometers.
a) Write a function called convert_mileage that converts from
miles per gallon to liters per 100 kilometers.
b) Test that your functions returns the right values for 20 and
40 miles per gallon.
c) How did you figure out what the right value was? How closely
do the computer results match the ones you expected?
"""
def convert_mileage(miles,gallon):

    mile_to_kilometer=1.609

    gallon_to_liter=3.785

    kilometer=100*(miles*mile_to_kilometer)
    liter=gallon*gallon_to_liter

    mpl=kilometer/liter

    return mpl
    
