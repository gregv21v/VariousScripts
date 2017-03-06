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
## TODO: (intermediate) add the ability to auto-update
##  your log file every few seconds. This has to be done
##  with threads otherwise it will interfere with the command
##  loop.
## TODO: (advanced) add the ability to automatically
##  commit to your repo.
## TODO: (easy) add the ability to add time. It will be useful
##  in those situations where you forget to start the
##  program when you start working on the project

#### Program Flow
# After starting the program, it follows the following steps:
# 1) save the current time in a variable
# 2) if you type 'exit', the program will do the following
#  1) calculate the time elapsed while the program was running
#  2) store the difference in the username-log.txt file
#  3) exit the program

# Implementing multiple partners:
# Multiple partners will have a list of
# partners, and when program is exited
# or times are logged it will split
# the total time between all the partners
# present at the coding session.

# The partners can be determined by getting
# their names from the log files.
# Before exiting the program, the user can
#  choose the user logs he wants to update.



from logging import *
from timeInterval import *
from datetime import timedelta, datetime

#1 Save current time
startTime = datetime.now();


cmd = ""

#2 Loop unit you exit
while(cmd != "exit"):
    currentTime = datetime.now()
    cmd = raw_input(">>");

    if(cmd == "check"):
        currentTime = datetime.now()
        timeElapsed = getTimeElapsed(startTime, currentTime)
        print("Hours: " + str(timeElapsed["hours"]) + "  Minutes: " + str(timeElapsed["minutes"]))

    elif(cmd == "takebreak"):
        startBreak = datetime.now()

        print("You are now on a break. When you want to finish this break")
        print("type end.")
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

# Find the time elapsed
timeElapsed = getTimeElapsed(startTime, currentTime)


# Choose the users that you want to update the logs
#  for. If there is only one user, the logs will
#  be updated automatically. If there are multiple
#  users, you will have the option of choosing
#  which users you want to include in the log.
logs = getLogNames()
if(len(logs) == 1):
    updateLog(logs[0], timeElapsed)
else:
    # show a numbered list of log files
    # and prompt the user for the ones
    # he or she wants to select

    for i in range(0, len(logs)):
        print(int(i) + ") " + logs[i])

    print("Input the number for the users you")
    print("would like to log time for. If you")
    print("choose multiple users, the time will")
    print("be split evenly among them.")
    userIndices = raw_input(">").split(" ")

    for i in xrange(0, len(logs)):
        if(i in userIndices):
            updateLog(logs[i], divideTime(timeElapsed, len(userIndices)))
        else:
            updateLog(logs[i], {"hours" : 0, "minutes" : 0})
