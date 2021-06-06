import logging

logging.basicConfig(filename='exception.log', format='[%(asctime)s] - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')


def info(message: str):
    logging.info(message)


def error(message: str):
    logging.error(message)
