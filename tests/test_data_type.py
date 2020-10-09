from app.helpers import decorate_data_type
import pytest

@pytest.mark.parametrize("number, expected", [
    ('24', 24),
    ('2.5', 2.5),
    ('224.55', 224.55),
    ('2.333.444', 2333444)
])
def test_data_type(number, expected):
    assert decorate_data_type(number) == expected
