import logging

## logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"), 
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a} and {b} to get {result}")
    return result

def subtract(a,b):
    result=a-b
    logger.debug(f"Subtracting {b} from {a} to get {result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"Multiplying {a} and {b} to get {result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"Dividing {a} by {b} to get {result}")
        return result
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero")
        return None
    
add(10,15)
subtract(15,10)
multiply(10,5)
divide(10,0)
divide(10,2)