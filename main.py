from plyer import notification
# plyer is a python library for accessing features of your hardware/platforms
# Please look at the documentation given by Ms. Adami
title = 'Welcome Message' # Title of the notification

message = 'Here is the awesome desktop notification!' # The message that will be displayed in the desktop notification

# Calling the notification method from the plyer library, while using the notify function.
# Set various parameters for the notification pop up - all parameters will be passed using notify method

notification.notify(title = title, # Calls the title variable to set the title of the desktop notification
                    message = message, # Calls the message variable to display the message in the notification
                    app_icon = None, # name of the icon to be displayed with the message
                    # You can use images that are saved in the same root folder of the program.
                    timeout = 10, # time to display the message for ___ seconds, defaults to 10 seconds
                    toast = False) # simple message instead of a full notification,

# Extra Practice:
# 1) Set daily tracker for Covid stats - you should have it pull data from an online resources.
# The notification should happen at the same time 7:00am

# 2) Create a daily notification to take your medicine.
# you need to take the medicine at the same time, twice a day - Once at 9am and another at 9pm

# 3) Create an hourly notification to alert the person to take a drink of water.

# * You should have all of these notifications in the same program. Allow it to run for at least an hour to test the
# the notifications.
# * If you need to set the timer, you need import the time library
hggyjuhhhhhhhhhhhhhhuy77q1                                                            w3 
