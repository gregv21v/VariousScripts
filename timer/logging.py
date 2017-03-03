from datetime import timedelta, datetime
import os

# Get the name of the log file
# in this repo.
def getLogNames():
    logNames = []
    # find the log file
    for fl in os.listdir(".."):
        if "-log" in fl:
            logNames.append("../" + fl)

    return logNames

# Get the name of the log file
# in this repo.
def getUsernames():
    logNames = []
    # find the log file
    for fl in os.listdir(".."):
        if "-log" in fl:
            logNames.append(fl[0:-len("-log.txt")])

    return logNames


# Update the contents of the log
# file to reflect the time
# spent during this sesssion.
# Interp:
#   logFilename is the name of the file where the user
#       stores information about his current session.
# Examples:
#   updateLog("joeshmo-log.txt", {"hours" : 4, "minutes" : 20})
#                                => joe shmoes log file has
#                                   been update to the amount of
#                                   times spent this sesssion
#                                   and the current date.
def updateLog(logFilename, elapsedTime):
    # get the original information from the file
    logRead = open(logFilename, "r")
    currentTime = datetime.now()

    lines = logRead.readlines()
    updatedLines = [
        str(elapsedTime["hours"]) + " hours and "
            + str(elapsedTime["minutes"]) + " minutes spent this session\n",
        currentTime.strftime("%Y-%m-%d") + "\n"
    ]

    logRead.close()

    # write the updated information to the file
    logWrite = open(logFilename, "w")

    logWrite.write(updatedLines[0])
    logWrite.write(updatedLines[1])

    for i in range(2, len(lines)):
        logWrite.write(lines[i])

    logWrite.close()
