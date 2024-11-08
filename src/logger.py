import logging
import os 
from datetime import datetime
from src.logger import logging

log_file =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ## this shows the format of log file which will show 
logs_path =os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)

Log_file_path =os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=Log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
    level=logging.INFO,
)
if __name__=="__main__":
    logging.info("logging has started")
