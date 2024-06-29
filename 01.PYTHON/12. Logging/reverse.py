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

#reverse a number

def reverse(number):
    """
    Reverse the given number.
    :param number: The number to reverse.
    :return: The reversed number.
    """
    result=0
    logging.info('In Function')
    while number>0:
        remainder=number%10
        result=result*10+remainder
        number=number//10
    logging.info('Out of Function')
    logging.info(f'Reverse is {result}')
    return result

reverse(1234567)