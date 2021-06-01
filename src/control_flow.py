def even_or_odd(number):
    """
    Know if a number is even or odd

    Args:
        number (int):

    Returns (str):
        'even' if number is even, 'odd' otherwise

    Examples:
        result = even_or_odd(1)
        print(result)  # odd

        result = even_or_odd(2)
        print(result)  # even
    """


def largest_minus_smallest(number1, number2):
    """
    Subtract largest number minus smallest

    Args:
        number1 (int): first number
        number2 (ins): second number

    Returns (int):
        subtraction

    Examples:
        result = largest_minus_smallest(1, 3)
        print(result)  # 2

        result = largest_minus_smallest(10, 3)
        print(result)  # 7

        result = largest_minus_smallest(22, 30)
        print(result)  # 8
    """


min_vehicle_model = 2005
vehicle_allowed_brands = ['FORD', 'CHEVROLET', 'RENAULT']
max_cylinder = 1000


def validate_vehicle(vehicle_model, vehicle_brand, cylinder):
    """
    Validate if vehicle is valid with some data.
    A vehicle is valid if:
        - Model must be greater than min_vehicle_model
        - Brand is in vehicle_allowed_brands
        - cylinder is less than max_cylinder

    Args:
        vehicle_model (int): model
        vehicle_brand (str): brand
        cylinder (int): motor size

    Returns (str):
        'valid vehicle' if is valid, 'invalid vehicle' otherwise

    Examples:
        result = validate_vehicle(2018, 'CHEVROLET', 800)
        print(result)  # valid vehicle

        result = validate_vehicle(2002, 'CHEVROLET', 800)
        print(result)  # invalid vehicle

        result = validate_vehicle(2018, 'AUDI', 800)
        print(result)  # invalid vehicle
    """


def max_number(number1, number2, number3):
    """
    Return max number between number1, number2 and number3

    Args:
        number1 (int):
        number2 (int):
        number3 (int):

    Returns (int):
    """


def positive_negative_or_zero(number):
    """
    Return if number is positive, negative or zero

    Args:
        number (int):

    Returns (str):
        'positive' if number is positive
        'negative' if number is negative
        'zero' if number is equal to 0
    """


def calculator(number1, number2, operation):
    """
    Basic calculator

    Args:
        number1 (int): First number
        number2 (int): Second number
        operation (str): Operation. Could be 'sum', 'subtraction', 'division'
                        or 'multiplication'

    Returns (int):
        Calculation result

    Examples:
        result = calculator(5, 10, 'sum')
        print(result)  # 15
    """


def add(value1, value2):
    """
    Simulate js behavior.
    If any of values is integer, make a sum.
    If any of value is string, make a concatenation

    Args:
        value1 (int or str):
        value2 (int or str):

    Returns:
        Sum or concatenation.

    Examples:
        result = add(5, 5)
        print(result)  # 10

        result = add(5, '5')
        print(result)  # 55
    """


def subtract(value1, value2):
    """
    Perform subtraction as integers

    Args:
        value1 (int or str):
        value2 (int or str):

    Returns:
        subtraction of integers

    Examples:
        result = subtract(10, 2)
        print(result)  # 8

        result = subtract(23, '17)
        print(result)  # 6
    """


def is_leap_year(year):
    """
    calculate if year is a leap year

    Leap year is when year is:
        - divisible by 4 and divisible by 400
        - divisible by 4 not divisible by 100

    Args:
        year (int):

    Returns (bool):
        True if year is leap year, False otherwise
    """


def longer_text_length(text0, text1):
    """
    which text is longer

    Args:
        text0 (str): first text
        text1 (str): second text

    Returns (str):
        longer text
    """
