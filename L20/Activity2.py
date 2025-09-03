import random, time
def getRandomDate(startdate, enddate):
    print("Printing random date between ", startdate, "and", enddate)
    randomGenerator = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startdate, dateFormat))
    endTime = time.mktime(time.strptime(enddate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random date = ", getRandomDate("10/1/2025", "10/30/2025"))