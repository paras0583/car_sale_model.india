import logging
import os
from datetime import datetime
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # getting the current date time etc in string .log format
logs_dir = os.path.join(os.getcwd(),'logs') # adding logs directory to our main directory
os.makedirs(log_dir , exist_ok=True) # now if already exist then just stop
log_file_path = os.path.join(logs_dir, log_file) # making the file of above string which as date and time inside our logs directory

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.info("Logging setup complete.")