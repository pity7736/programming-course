from pytest import mark

from src.data_type import int_to_float, float_to_int, append_to_list, \
    insert_to_list, append_to_tuple, upper_case_string


int_values_params = (
    (1212, 1212.0),
    (10, 10.0),
)


@mark.parametrize('value, expected_value', int_values_params)
def test_int_to_float_1212(value, expected_value):
    assert type(int_to_float(value=value)) is float
    assert int_to_float(value=value) == expected_value


float_value_params = (
    (1212.5, 1212),
    (10.0, 10)
)


@mark.parametrize('value, expected_value', float_value_params)
def test_float_to_int(value, expected_value):
    assert type(float_to_int(value)) is int
    assert float_to_int(value) == expected_value


string_params = (
    ('python', 'PYTHON'),
    ('programming', 'PROGRAMMING')
)


@mark.parametrize('string, expected_string', string_params)
def test_upper_case_string(string, expected_string):
    assert upper_case_string(string) == expected_string


list_append_params = (
    ([1, 2, 3], 4, [1, 2, 3, 4]),
    (['a', 'b', 'c'], 'd', ['a', 'b', 'c', 'd'])
)


@mark.parametrize('l, value, expected_l', list_append_params)
def test_list_append(l, value, expected_l):
    assert append_to_list(l=l, value=value) == expected_l


list_insert_params = (
    ([1, 2, 3], 4, 1, [1, 4, 2, 3]),
    ([1, 2, 3], 4, 0, [4, 1, 2, 3]),
)


@mark.parametrize('l, value, position, expected_l', list_insert_params)
def test_list_insert(l, value, position, expected_l):
    assert insert_to_list(l=l, value=value, position=position) == expected_l


def test_tuple_append():
    assert append_to_tuple(t=(1, 2, 3), value=4) == (1, 2, 3, 4)
