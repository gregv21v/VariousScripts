########################################################
# This program is a simple convient way to update your #
# log file. All you need to do is start it up when you #
# start a session, then type the command "exit" in the #
# terminal when you want to exit. After that, your log #
# file will be updated with all the relavent details.  #
########################################################


#############################
#### Additional Features ####
#############################
## TODO: add the ability to auto-update the log file
##  every few seconds. This has to be done with threads
##  otherwise it will interfere with the exit loop.
## TODO: add the ability to pause the program, so that
##  you can leave for a second then come back.
## TODO: (advanced) add the ability to automatically
##  commit to the repo.


#### Program Flow
# After starting the program, it follows the following steps:
# 1) save the current time in a variable
# 2) if you type 'exit', the program will do the following
#  1) calculate the time elapsed while the program was running
#  2) store the difference in the username-log.txt file
#  3) exit the program


from datetime import timedelta, datetime
import time
import os


# Get the name of the log file
# in this repo.
def getLogFilename():
    # find the log file
    for fl in os.listdir("."):
        if "log" in fl:
            return fl


# Update the contents of the log
# file to reflect the time
# spent during this sesssion.
# Interp:
#   logFilename is the name of the file where the user
#       stores information about his current session.
# Examples:
#   updateLog("joeshmo-log.txt") => joe shmoes log file has
#                                   been update to the amount of
#                                   times spent this sesssion
#                                   and the current date.
def updateLog(logFilename):
    # get the original information from the file
    logRead = open("venezia9g-log.txt", "r")

    lines = logRead.readlines()
    updatedLines = [
        str(hours) + " hours and " + str(minutes) + " minutes spent this session\n",
        currentTime.strftime("%Y-%m-%d") + "\n"
    ]

    logRead.close()

    # write the updated information to the file
    logWrite = open("venezia9g-log.txt", "w")

    logWrite.write(updatedLines[0])
    logWrite.write(updatedLines[1])

    for i in range(2, len(lines)):
        logWrite.write(lines[i])

    logWrite.close()



#1 save current time
startTime = datetime.now();

cmd = ""

#2 Loop unit you exit
while(cmd != "exit"):
    cmd = raw_input(">>");

currentTime = datetime.now();


#2, 1 find the time elapsed
timeDiff = currentTime - startTime
diff = divmod(timeDiff.days * 86400 + timeDiff.seconds, 60)

hours = diff[0] / 60
minutes = diff[0] - (hours * 60)


#2, 2 Store the difference in the username-log.txt file
updateLog(getLogFilename())
