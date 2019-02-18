try:
    import ConfigParser as configparser
except:
    import configparser
import json
import os
import logging


def read_ini(config_file):
    init = config_file
    config = configparser.ConfigParser()
    config.read(init)
    return config


def read_json(config_file):
    with open(config_file) as data_file:
        config = json.load(data_file)
    return config


def read_env(config_file=None, format=None):
    try:
        if format == "json":
            config = read_json(config_file)
        else:
            config = read_ini(config_file)
    except:
        raise Exception("Error reading configuration")
    return config


def get_config():
    cfg = read_env(config_file=os.getenv("UNIT9_CONFIG"), format='json')
    return cfg


def get_log(log_name=None, log_file=os.getenv("UNIT9_LOG", "/tmp/unit9.log"), level=logging.INFO, format=None):
    format_env = os.getenv("UNIT9_LOG_FORMAT", "long")
    format = format if format else format_env
    if str(format) == 'long':
        f = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    if str(format) == 'short':
        f = '%(asctime)s - IPUR %(levelname)s - %(message)s'
    logger = logging.getLogger(log_name)
    # Don't propagate the log in the hierarchy
    logger.propagate = False
    logger.setLevel(level)
    ch = logging.StreamHandler()
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter(f)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
