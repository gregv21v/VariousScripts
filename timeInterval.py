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
