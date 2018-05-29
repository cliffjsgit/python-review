#!/usr/bin/env python3

###############################################################################
#
print("\nExercise 5-1\n")
#
# The time module provides a function, also named time, that returns the current
# Greenwich Mean Time in "the epoch", which is an arbitrary time used as a 
# reference point. On UNIX systems, the epoch is 1 January 1970.
#
# >>> import time
# >>> time.time()
#     1437746094.5735958
#
# Question 1
# 1. Write a script that reads the current time and converts it to a time of day
# in hours, minutes, and seconds, plus the number of days since the epoch.
#
import time
epoch = time.time()
answer1=False
answer2=False
print("Time (GMT): {}\n".format(answer1)+
      "Days Since epoch: {}".format(answer2))