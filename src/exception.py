import sys
import traceback
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Retrieve exception traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where error occurred
    line_number = exc_tb.tb_lineno  # Get the line number of the error
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0  ## This will raise a division by zero exception
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)