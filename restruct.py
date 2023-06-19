"""
Problem
When we get "autodestruct" messege we run a script to make restart the asterisk.


@Version: 1.0
import subprocess #subprocess module to hadle script
import time       #system Time module
import re         #Reguler Expresion (REGEX)

"""
#Required modules

import subprocess
import time
import re

# This "def check_log_file()" function to check the Asterisk log file for the message "autodestruct":
# This function opens the Asterisk log file, seeks to the end of the file,
# and reads each line one at a time. , 
# the function returns True.
def check_log_file():
    log_file_path = "/var/log/asterisk/messages"
    with open(log_file_path, "r") as log_file:
        log_file.seek(0, 2)
        while True:
            line = log_file.readline()
            if "autodestruct" in line:
                return True
            time.sleep(0.1)

# This function runs the Asterisk command "core restart now" using the subprocess module.
# and the loop checks the log file every second for the message "autodestruct". 
# If the message is found, the loop calls the restart_asterisk function to restart Asterisk. 
# The loop then waits for one second before checking the log file again.
def restart_asterisk():
    subprocess.run(["/usr/sbin/asterisk", "-rx", "core restart now"])
    while True:
    if check_log_file():
        restart_asterisk()
    time.sleep(1)

# This code assumes that the Asterisk log file is located at "/var/log/asterisk/messages" 
# and that the Asterisk command "core restart now" is the correct command to use for restarting your Asterisk installation. 
# You may need to modify these values to match your specific setup.
"""
@Note
# The specific setup would require understanding the technical aspects of the setup, 
# such as the location of the log file, the command to restart Asterisk, and any other relevant configuration settings. 
# Here are some technical requirements and aspects to consider when modifying the code for your specific setup:

Location of the log file:
# The location of the Asterisk log file may differ depending on your setup. 
# You will need to determine the correct path to the log file and update the log_file_path variable in the check_log_file() function accordingly.

Message format: 
#The message format may differ depending on your Asterisk configuration. 
#If the "autodestruct" message is not exactly as you expect, you may need to modify the if "autodestruct" in line: statement in the check_log_file() function to match the correct message format.

Command to restart Asterisk: 
#The command to restart Asterisk may differ depending on your setup. 
#You will need to determine the correct command to use and update the subprocess.run() function in the restart_asterisk() function accordingly.

Permission issues: 
# The script may require permission to access the log file and to execute the Asterisk restart command. 
# Make sure the user running the script has the necessary permissions.

Performance impact: 
# Running the script continuously may have performance implications for your system. 
# You may need to adjust the frequency of the checks or find a more efficient way to monitor the log file.

Dependencies: 
# The script may have dependencies on other Python modules or external programs. 
# Make sure you have installed any required dependencies and that they are compatible with your system.
# The technical requirements for the script to work properly. 
# Testing and debugging the code thoroughly is also recommended to ensure that it works correctly for your specific setup.
"""