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
## TODO: (advanced) add the ability to automatically
##  commit to the repo.
## TODO: add the ability to temporarily delete the
##  the log file, so you can have multiple commits for a session
##  not sure how useful this would be though, as you could just
##  have smaller sessions


#### Program Flow
# After starting the program, it follows the following steps:
# 1) save the current time in a variable
# 2) if you type 'exit', the program will do the following
#  1) calculate the time elapsed while the program was running
#  2) store the difference in the username-log.txt file
#  3) exit the program

from logging import *
from timeInterval import *
from datetime import timedelta, datetime

#1 save current time
startTime = datetime.now();

cmd = ""

#2 Loop unit you exit
while(cmd != "exit"):
    currentTime = datetime.now();
    cmd = raw_input(">>");

    if(cmd == "check"):
        timeElapsed = getTimeElapsed(startTime, currentTime)
        print("Hours: " + str(timeElapsed["hours"]) + "  Minutes: " + str(timeElapsed["minutes"]))
    elif(cmd == "takebreak"):
        startBreak = datetime.now()

        print("You are now on a break. When you want to finish this break")
        print("enter the command end.")
        inpt = raw_input(">>")
        while(inpt != "end"):
            inpt = raw_input(">>")

        endBreak = datetime.now()

        # calculate the time elapsed
        elapsed = getTimeElapsed(startBreak, endBreak)

        # display the time elapsed
        print(elapsed)

    elif(cmd == "restart"):
        startTime = datetime.now()
    elif(cmd == "help"):
        f = open("help.txt", "r")

        print(f.read())


currentTime = datetime.now();

timeElapsed = getTimeElapsed(startTime, currentTime)

#2, 1 find the time elapsed
#2, 2 Store the difference in the username-log.txt file
updateLog(getLogFilename(), timeElapsed)
