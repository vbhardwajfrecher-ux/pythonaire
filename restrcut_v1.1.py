import subprocess
import time
import re
import logging

# Set up logging
logging.basicConfig(filename='autodestruct.log', level=logging.INFO)

# Define the log file path
log_file_path = "/var/log/asterisk/messages"

# Define the restart command
restart_command = "/usr/sbin/asterisk -rx 'core restart now'"

# Define the regex pattern to match the log message
log_pattern = re.compile(r'.*autodestruct.*')

# Define the check_log_file function
def check_log_file():
    with open(log_file_path, "r") as log_file:
        log_file.seek(0, 2)
        while True:
            line = log_file.readline()
            if log_pattern.match(line):
                logging.info('Found autodestruct message in log file.')
                return True
            time.sleep(0.1)

# Define the restart_asterisk function
def restart_asterisk():
    subprocess.run(restart_command, shell=True)
    logging.info('Restarted Asterisk.')

# Set up a loop to monitor the log file
while True:
    if check_log_file():
        try:
            restart_asterisk()
        except subprocess.CalledProcessError as e:
            logging.error(f'Error restarting Asterisk: {e}')
    time.sleep(1)
