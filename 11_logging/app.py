import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
    logging.FileHandler("app1.log"),
    logging.StreamHandler()
    ]
)
logger = logging.getLogger("Arithematicapp")
def add(a,b):
    result=a+b
    logging.debug(f"Addition of {a} and {b} :{result}")
    return result

def sub(a,b):
    result=a-b
    logging.debug(f"Substraction of {a} and {b} :{result}")
    return result

def mult(a,b):
    result=a*b
    logging.debug(f"Multiplication of {a} and {b} :{result}")
    return result

def divd(a,b):
    try:
        result=a/b
        logging.debug(f"Division of {a} and {b} :{result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Error: Division by zero is not allowed")
        return "Error: Division by zero is not allowed"

add(3,4)
sub(5,2)
mult(2,6)
divd(8,2)
divd(8,0)
