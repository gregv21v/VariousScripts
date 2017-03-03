from datetime import timedelta, datetime
import time


## TimeInterval is a
##  Dictionary of {Hours Minutes}

## getTimeElapsed:
##  DateTime DateTime => TimeInterval
## GIVEN: a start time, and end time
## RETURNS: the time in minutes and hours elapsed
##  between the start time and end time
def getTimeElapsed(startTime, endTime):
    timeDiff = endTime - startTime
    diff = divmod(timeDiff.days * 86400 + timeDiff.seconds, 60)

    hours = diff[0] / 60
    minutes = diff[0] - (hours * 60)

    return {
        "hours" : hours,
        "minutes" : minutes
    }

## getTimeIntervalDiff:
##  TimeInterval TimeInterval => TimeInterval
## GIVEN: a TimeInterval a, and a TimeInterval b
## RETURNS: the difference between TimeIntervals
##  a, and b
## EXAMPLES:
##  getTimeIntervalDiff(
##      {"hours" : 6, "minutes" : 10},
##      {"hours" : 4, "minutes" : 12}
##  ) ==>
##  {
##      "hours" : 1,
##      "minutes" : 58
##  }
def getTimeIntervalDiff(a, b):
    newInterval = {
        "hours" : a["hours"] - b["hours"],
        "minutes" : a["minutes"] - b["minutes"]
    }

    if(newInterval["minutes"] < 0):
        newInterval["hours"] -= 1
        newInterval["minutes"] += 60

    return newInterval


## convertIntervalToMinutes:
##  TimeInterval => Natural
## GIVEN: a TimeInterval
## RETURNS: the number of minutes
##  in that time interval
def convertIntervalToMinutes(interval):
    return interval["hours"] * 60 + interval["minutes"]

## convertMinutesToInterval:
##  Natural => TimeInterval
## GIVEN: a set of minutes
## RETURNS: a time interval
##  representing the number of minutes
##  passed in
def convertMinutesToInterval(minutes):
    return {
        "hours" : int(minutes / 60),
        "minutes" : minutes - 60 * int(minutes / 60)
    }



## divideTime:
##  TimeInterval Natural => TimeInterval
## GIVEN: a TimeInterval interval, and a
##  Natural number n
## RETURNS: the same time interval with
##  it's total time divided by n.
## Note: Time for each interval will
##  be even, so there might be time discarded
##  by division
def divideTime(interval, n):
    # convert to minutes
    minutes = convertIntervalToMinutes(interval)
    newMinutes = int( minutes / n )
    return convertMinutesToInterval(newMinutes)
