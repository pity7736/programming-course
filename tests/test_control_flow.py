
from pytest import mark

from src.control_flow import even_or_odd, largest_minus_smallest,\
    validate_vehicle, max_number, positive_negative_or_zero, calculator, add,\
    subtract,is_leap_year, longer_text_length


even_or_odd_values = (
    (4, 'even'),
    (3, 'odd'),
    (241, 'odd'),
    (182, 'even'),
)


@mark.parametrize('number, response_expected', even_or_odd_values)
def test_even_or_odd(number, response_expected):
    response = even_or_odd(number)
    assert response == response_expected


largest_minus_smallest_params = (
    (2, 3, 1),
    (10, 8, 2),
    (22, 30, 8),
    (45, 14, 31),
    (80, 80, 0),
)


@mark.parametrize('number1, number2, response_expected',
                  largest_minus_smallest_params)
def test_largest_minus_smallest(number1, number2, response_expected):
    response = largest_minus_smallest(number1, number2)
    assert response == response_expected


validate_vehicle_values = (
    (2018, 'CHEVROLET', 800, 'valid vehicle'),
    (2002, 'CHEVROLET', 800, 'invalid vehicle'),
    (2015, 'AUDI', 800, 'invalid vehicle'),
    (2006, 'CHEVROLET', 1200, 'invalid vehicle'),
    (2010, 'FORD', 999, 'valid vehicle'),
    (2010, 'FORD', 1000, 'invalid vehicle')
)


@mark.parametrize('vehicle_model, vehicle_brand, cylinder, response_expected',
                  validate_vehicle_values)
def test_validate_vehicle(vehicle_model, vehicle_brand, cylinder,
                          response_expected):
    response = validate_vehicle(vehicle_model, vehicle_brand, cylinder)
    assert response == response_expected


max_number_values = (
    (1, 2, 3, 3),
    (5, 1, 4, 5),
    (3, 7, 5, 7),
    (876, 851, 972, 972),
)


@mark.parametrize('number1, number2, number3, response_expected',
                  max_number_values)
def test_max_number(number1, number2, number3, response_expected):
    response = max_number(number1, number2, number3)
    assert response == response_expected


positive_negative_or_zero_values = (
    (20, 'positive'),
    (-6, 'negative'),
    (0, 'zero'),
    (1, 'positive'),
    (-50, 'negative'),
)


@mark.parametrize('number, response_expected', positive_negative_or_zero_values)
def test_positive_negative_or_zero(number, response_expected):
    response = positive_negative_or_zero(number)
    assert response == response_expected


calculator_values = (
    (10, 20, 'sum', 30),
    (34, 19, 'subtraction', 15),
    (100, 20, 'division', 5),
    (3, 4, 'multiplication', 12),
    (131, 20, 'sum', 151),
)


@mark.parametrize('number1, number2, operation, response_expected',
                  calculator_values)
def test_calculator(number1, number2, operation, response_expected):
    response = calculator(number1, number2, operation)
    assert response == response_expected


add_values = (
    (5, 5, 10),
    ('2', 5, '25'),
    (8, '13', '813'),
    ('10', '2', '102'),
    (9, '2', '92'),
)


@mark.parametrize('value1, value2, response_expected', add_values)
def test_add(value1, value2, response_expected):
    response = add(value1, value2)
    assert response == response_expected


subtract_values = (
    (10, 2, 8),
    ('5', 5, 0),
    (23, '17', 6),
    ('10', '38', -28),
    ('12', '8', 4)
)


@mark.parametrize('value1, value2, response_expected', subtract_values)
def test_subtract(value1, value2, response_expected):
    response = subtract(value1, value2)
    assert response == response_expected


leap_year_params = (
    (2000, True),
    (1900, False),
    (2400, True),
    (2300, False),
    (2020, True),
    (2024, True),
)


@mark.parametrize('year, expected_result', leap_year_params)
def test_is_leap_year(year, expected_result):
    assert is_leap_year(year) is expected_result


longer_text_length_params = (
    ('hi', 'world', 'world'),
    ('this is a long text', 'short text', 'this is a long text'),
)


@mark.parametrize('text0, text1, expected_result', longer_text_length_params)
def test_longer_text_length(text0, text1, expected_result):
    assert longer_text_length(text0, text1) == expected_result
