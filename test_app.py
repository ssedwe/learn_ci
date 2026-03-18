import pytest
from utils import calculate_powers

@pytest.mark.parametrize("n, square, cube, fifth", [
    (2, 4, 8, 32),
    (0, 0, 0, 0),
    (-2, 4, -8, -32),
])
def test_calculate_powers(n, square, cube, fifth):
    result = calculate_powers(n)

    assert result["square"] == square
    assert result["cube"] == cube
    assert result["fifth_power"] == fifth


def test_invalid_input():
    with pytest.raises(ValueError):
        calculate_powers("abc")