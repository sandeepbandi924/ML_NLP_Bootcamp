import logging

#logging setting
logging.basicConfig(
    level=logging.DEBUG,
    format ='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('arm.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArmstrongNumber')

def isArmstrongNumber(number):
    """
    Check if the given number is an Armstrong number.
    :param number: The number to check.
    :return: True if the given number is an Armstrong number, False otherwise.
    """
    sum = 0
    temp = number
    logging.info('In Function')
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    logging.info('Out of Function')

    if sum == number:
        logging.info(f'Armstong Unit {number}')
        return True
    else:
        logging.info(f'Not Armstong Unit {number}')
        return False
    
isArmstrongNumber(370)
   