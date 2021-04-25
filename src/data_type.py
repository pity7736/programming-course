
def int_to_float(value):
    """
    Cast int to float

    Args:
        value (int): integer value

    Returns (float):
        float value

    Examples:
        result = int_to_float(10)
        print(result, type(result))
        10.0, <class 'float'>
    """


def float_to_int(value):
    """
    Cast float to int

    Args:
        value (float): float value

    Returns (int):
        int value

    Examples:
        result = float_to_int(10.5)
        print(result, type(result))
        10, <class 'int'>

    """


def upper_case_string(value):
    """
    Upper string value

    Args:
        value (str):

    Returns (str):
        string in upper case

    Examples:
        result = upper_case_string('hi world')
        print(result)
        HI WORLD
    """


def append_to_list(l, value):
    """
    Add value item to l in last position

    Args:
        l (list): list
        value (any): item to add

    Returns (list):

    Examples:
        result = append_to_list([1, 2, 3], 4)
        print(result)
        [1, 2, 3, 4]

    """


def insert_to_list(l, value, position):
    """
    Add value item to l in position

    Args:
        l (list): list
        value (any): item to add
        position (int): list position

    Returns (list):

    Examples:
        result = insert_to_list([1, 2, 3], 4, 2)
        print(result)
        [1, 2, 4, 3]

    """


def append_to_tuple(t, value):
    """
    Add value item to t in last position

    Args:
        t (tuple): tuple
        value (any): item to add

    Returns (tuple):

    Examples:
        result = append_to_tuple((1, 2, 3), 4)
        print(result)
        (1, 2, 3, 4)

    """
