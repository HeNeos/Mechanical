# Coronabot: A bot for automatic attendance dialing in EARP FIM and login in Webex

## crontab
Run background processes, only available on Linux. For Windows, you can find alternative ways to run Python scripts at certain times.

crontab contains information on WHAT and WHEN to perform an action, in this case run the scripts. For example, if you need to join a webex meeting at 4pm on Tuesdays, you need to tell crontab the time, day, and path to the script for that meeting.

You must edit crontab according to your schedule and the name of the scripts you need to run; check that the path is correct and the time as well

## earp.py
earp.py is the script in charge of attendance dialing, this script is distinct from the others because the link is always the same and in crontab it must tell you what time you need to execute it.

earp.py will open a new chromium window and enter the EARP FIM website with your code and password (you must modify this according to your data), mark the newest assistance available and then refresh the tab and perform this action again until end the maximum execution time (set to approximately 2 hours)

## All other scripts
The other files are only used as an example in my personal configuration, you can see that they contain my name and my email necessary to enter webex; create your own scripts using these examples. You just need to modify the personal information, the meeting link and the script name (don't forget to modify this in crontab as well).

