'''
When you run this code, it will create a log file with the specified name in the "logs" directory 
and write the log messages to that file. The log messages will include timestamps,
line numbers, log levels, and the messages themselves.

'''
import logging
import os
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"                                 # Generate a filename based on the current date and time ->  09_15_2023_15_30_45.log

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)                                           # Create a path to the logs directory in the current working directory -->pwd/log/09_15_2023_15_30_45.log

os.makedirs(logs_path, exist_ok=True)                                                             # Ensure that the logs directory exists; if not, create it

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)                                                 # Create a full path to the log file within the logs directory  "C:\path\to\current\directory\logs\09_15_2023_15_30_45.log".
# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,                                                                       # Set the log file path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",                   # Define log message format
    level=logging.INFO,                                                                           # Set the logging level to INFO
)
