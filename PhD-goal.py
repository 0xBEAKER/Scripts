#!/usr/bin/env python
# File: PhD-goal.py
# Date: 9/11/17
# Author: Paul Beach
# This script uses the Todoist API to load my tasks, selects the items associated with a project tracking PhD graduation requirements
# and then displays the task due soonest from that project on a 1602 LCD display

from datetime import *
import subprocess
import time
import json
import lcdDriver

lcdAddress = 0x3f # default address of i2c backpack is 0x3f

# function to retrieve the next goal from Todoist
def getGoal():
    # create a curl command and pass to the OS to execute - token is your Todoist API token - there's surely a better way to do this
    data = subprocess.check_output("curl https://todoist.com/api/v7/sync -d token=yourTokenGoesHere -d sync_token=* -d resource_types='[\"items\"]'", shell=True)
    data = json.loads(data)

    project = [] # create an empty list to store the relevant projects

    for item in data['items']: # iterate over all the results returned
        if item['project_id'] == 199083469: # find all items under the project I want
           project.append([datetime.strptime(item['due_date_utc'][4:15], '%d %b %Y'), item['content']]) # add the converted datetime object (DD MMM YYYY only) and the text

    project.sort(key=lambda r: r[0]) # sort the items according to the date field in ascending order

    due_date = "Due in " + str((project[0][0] - datetime.today()).days) + " days" # calculate the number of days between the due date and today, and embed in a string

    return project[0][1], due_date

def displayGoal(goal):
    lcd = lcdDriver.Lcd(lcdAddress) # setup LCD
    lcd.backlightOn()

    if len(goal[0]) < 17: # if the task is less than 17 chars, no need to scroll the text, just display it and sleep
        lcd.lcdDisplayStringList([ goal[0], goal[1] ])
        time.sleep(900)

    else: # since the text is longer than 16 characters, scroll it
        padding = ' ' * 16 # padding blank spaces for the end
        for j in range (0, 350): # iterate 350 times before refreshing
            lcd.lcdDisplayStringList([goal[0], goal[1] ]) # display the initial text, then pause for 3 seconds
            time.sleep(2.5)
            for i in range (0, len(goal[0])): # for each letter in the text, run this loop
                lcd.lcdDisplayStringList([(goal[0] + padding)[i:], goal[1] ]) #display the text + padding, starting from the ith character
                time.sleep(.4) # pause for dramatic effect

def __main__():
    while True: # run forever
        displayGoal(getGoal())

if __name__ == '__main__':
    __main__()
