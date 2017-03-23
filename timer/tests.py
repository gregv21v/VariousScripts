from logging import *
from timeInterval import *
from timer import *

import unittest

## TODO: find a better place to store the example -log.txt files

class TestStringMethods(unittest.TestCase):

    # functions tested
    #   getUsernames
    def test_getting_usernames(self):
        self.assertIn("username", getUsernames())

    # functions tested
    #   getLogNames
    def test_getting_log_name(self):
        self.assertIn("../username-log.txt", getLogNames())

    # functions tested
    #   getLogNames
    #   updateLog
    ## TODO: Complete the test_updating_log
    ##  test function
    def test_updating_log(self):
        # reset the username-log.txt file
        # to default-log.txt for testing
        default = open("../default-log.txt", "r")
        test = open("../username-log.txt", "w")

        test.write(default.read())
        test.close()

        timeInterval = {"hours" : "5", "minutes" : "6"}
        updateLog("../username-log.txt", timeInterval)

        test = open("../username-log.txt", "r")
        line = test.readlines()[0]
        words = line.split(" ")

        # find the hours
        hours = words[0]

        # find the minutes
        minutes = words[3]

        self.assertEqual(timeInterval["hours"], hours)
        self.assertEqual(timeInterval["minutes"], minutes)


    # test time elapsed

    # test get time interval difference

    # test convertIntervalToMinutes

    # test convertMinutesToInterval

    # test divide time


if __name__ == '__main__':
    unittest.main()
