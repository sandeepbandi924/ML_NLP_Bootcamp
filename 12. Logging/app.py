import logging

#logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithematicApp')

def add(x, y):
    result=x+y
    logger.info(f'Adding {x} + {y}= {result}')
    return result

def subtract(x, y):
    result=x-y
    logger.info(f'Subtracting {x} - {y}  = {result}')
    return result

def multiply(x, y):
    result=x*y
    logger.info(f'Multiplying {x} * {y}= {result}')
    return result

def divide(x, y):
    try:
        result=x/y
        logger.info(f'Dividing {x} / {y}= {result}')
        return result
    except ZeroDivisionError as e:
        logger.error(e)
        return None
    
add(10,20)
subtract(10,20)
multiply(10,20)
divide(12,10)
divide(10,0)



