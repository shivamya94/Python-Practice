import logging
import os

#create logger string
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_folder = "Logs"
log_file = "running_log.log"

os.mkdirs(log_folder,exist_ok = True)










# def add_number(a,b):
#     out = a + b
#     print("Succesully printed")

#     return out


# num = add_number(3,4)
# print(num)