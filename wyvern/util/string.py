""" 
    String Utility Helper
  
    Helper for Strings 

"""
# -*- coding: utf-8 -*-
import re
import unidecode


def file_slug(slug):
    """ 
    Slugify
  
    returns a slug
  
    Parameters: 
    string (str): plain text string 
    # TODO: unicode fixes
  
    Returns: 
    return: slug of string
  
    """
    slug = unidecode.unidecode(slug).lower()
    return re.sub(r"[\W_]+", "_", slug)

    return slug
