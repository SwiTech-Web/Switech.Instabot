import logging
import os
import configparser

from time import strftime


root = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists('log'):  # Create the folder if it doesn't exists
    os.mkdir('log')

config = configparser.ConfigParser()
config.read(os.path.join(root, 'logger.ini'))

filename = "log/{}-{}.log".format(config['PYLOGGER']['Appname'], strftime("%Y_%m_%d_%H_%M_%S"))

pylogger = logging.getLogger(__name__)
pylogger.setLevel(logging.getLevelName(config['PYLOGGER']['Level']))

handler = logging.FileHandler(filename, 'w', 'utf-8')
formatter = logging.Formatter(
    fmt='[%(asctime)s][%(levelname)s] : [%(filename)s][%(funcName)s] : %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)

handler.setFormatter(formatter)
pylogger.addHandler(handler)
