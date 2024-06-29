from logger import logging

def add(a,b):
    logging.debug("Addition of two numbers")
    return a+b

logging.debug("Addition function is called")
add(10,15)
    