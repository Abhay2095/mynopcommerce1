import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('.\\Logs\\homepage.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s  :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)            # filehandler object

        logger.setLevel(logging.INFO)
        return logger



