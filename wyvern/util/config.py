""" 
    Config Utility Helper
  
    For now simply reads the config file
"""

from configparser import ConfigParser, RawConfigParser, NoOptionError, NoSectionError

config = RawConfigParser()
config.read("./config.cnf")


def get(section, key):
    try:
        config.get(section, key)
    except NoSectionError:
        return None
    finally:
        return config.get(section, key)
