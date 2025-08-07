from logger import logging
def add(a,b):
    logging.debug("Addition is taking place")
    return(a+b)

logging.debug("Addition has been called")
add(3,5)