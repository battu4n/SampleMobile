import logging
import inspect
def LogGen():
    logName=inspect.stack()[1][3]
    logger =logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("{0}.log".format(logName),mode='a')
    fileHandler.setLevel(logging.DEBUG)
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger