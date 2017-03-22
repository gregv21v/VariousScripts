from logging import *
from timeInterval import *
from timer import *

import unittest

class TestStringMethods(unittest.TestCase):


    # functions tested
    #   getUsernames
    def test_getting_usernames(self):
        assertEqual(getUsernames()[0], "username")

    # functions tested
    #   getLogNames
    #   updateLog
    ## TODO: Complete the test_updating_log
    ##  test function
    def test_updating_log(self):
        # reset the username-log.txt file
        # to default-log.txt for testing
        f = open("default-log.txt", "r")



        logName = getLogNames()[0]

        assertEqual(logName, "username-log.txt")

        updateLog(logName, {"10"})


    # test time elapsed

    # test get time interval difference

    # test convertIntervalToMinutes

    # test convertMinutesToInterval

    # test divide time
