import random
import time
def getrandom_date(startdate, enddate ):
    print("printing random date between", startdate, "and", enddate)
    dateformat = '%d-%m-%Y'

    starttime = time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(enddate, dateformat))

    randomtime = random.randint(starttime, endtime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate

print("random date =",getrandom_date("1-1-2016", "31-12-2018"))

