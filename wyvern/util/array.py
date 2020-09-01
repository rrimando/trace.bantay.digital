""" 
    Array Utility Helper
  
    Helper for Arrays 

"""


def choices(em):
    """
    Choices

    returns value, name pair for dropdown options

    Parameters:
    em (obj): Django Object

    Returns:
    dict: Dictionary for options

    """
    return [(e.value, e.name) for e in em]


def list_choices(fl):
    """
    List Choices

    creates a dict from a flat dict

    Parameters:
    fl (list): List

    Returns:
    dict: Dictionary for options

    """

    return [(str(val), str(val)) for val in fl]
