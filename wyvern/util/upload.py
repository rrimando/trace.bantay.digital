""" 
    Upload Utility Helper
  
    Helper for Uploads 

"""

import os
import uuid
import wyvern.util.config as config


def get_file_path(instance, filename):
    """ 
    Get Upload File Path
  
    return file path based on config
  
    Parameters: 
    instance (obj): Django Object
    filename (string): Filename
  
    Returns: 
    str: New path for file
  
    """
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(config.get("uploads", "folder"), filename)


def get_ck_file_path(filename):
    """ 
    Get Upload File Path For CKEditor
  
    return file path based on config
  
    Parameters:
    filename (string): Filename
  
    Returns: 
    str: New path for file
  
    """
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(config.get("uploads", "folder"), filename)


def handle_uploaded_file(file, path):
    with open(path, "wb+") as destination:
        for chunk in path.chunks():
            destination.write(chunk)
