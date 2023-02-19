import configparser
import os 
# from certificateMappingConfig import get_app_file_path
def get_app_file_path(file):
    """Return the absolute path of the app's files. They should be in the same folder as this py file."""
    folder, _ = os.path.split(__file__)
    file_path = os.path.join(folder, file)
    return file_path

def read_path_config():
    config = configparser.ConfigParser()
    config.read(get_app_file_path('paths.ini'))
    return config

def read_certificate_mapping_config():
    config = configparser.ConfigParser()
    config.read(get_app_file_path('mappings.ini'))
    return config