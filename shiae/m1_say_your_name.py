#!/usr/bin/env python3
"""
This module is meant to be your first program that you've made for EV3.
  Make the robot say your name and then beep.
  Use the samples to learn the API calls needed (not much code to write)

Authors: Dave Fisher and Allison Shi.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


# ------------------------------------------------------------------
# TODO: 2. Make the robot say "David Fisher can write E V 3 programs"
#   But of course use YOUR NAME.
#
#   Use the samples to figure out the necessary lines of code.
#     Hint: This program can be done in as little as 2 lines of code (1 import, 1 function call)
#   Feel free to run it, change it, and run it again with any message you like.
#   This program is simple, but if you can do this, then you have the tools to do FAR more.
# ------------------------------------------------------------------

import ev3dev.ev3 as ev3


def main():
    name()


def name():
    # ev3.Sound.speak("TIME CUBE 4ce In 1884, meridian time personnel met in "
    #                 "Washington to change Earth time. First words said was "
    #                 "that only 1 day could be used on Earth to not change "
    #                 "the 1 day bible. So they applied the 1 day and "
    #                 "ignored  the  other  3 days.").wait()

    # ev3.Sound.speak("TIME CUBE 4ce In 1884,  meridian time personnel met in "
    #                 "Washington to change Earth time").wait()

    # ev3.Sound.speak("Allison").wait()

    ev3.Sound.speak(
        "oiueaeoiuaeoiuaeoiuaoieuoaieuaoieeiaoiueiuaoeiuaoieuaoi"
        "euoaieuaoieuoaieuaoieu").wait()


main()

