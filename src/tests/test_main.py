import pytest
from unittest.mock import Mock, patch
from src.main import main, _add

@pytest.mark.parametrize(
    "x, y, z",
    [
        (1, 1, 2),
        (1, 2, 3)
    ],
)
# Mock a third party function and its return value
def test_main_happy_path(x, y, z):
    with patch("src.main.os._exists", return_value=False) as mock_exists, patch("src.main.os.makedirs") as mock_makedirs:
        result = main(x, y)

        assert result == z
        mock_exists.assert_called_once()
        mock_makedirs.assert_called_once_with("dummyfile", exist_ok=True)

@pytest.mark.parametrize(
    "x, y, z",
    [
        (1, 1, 2),
        (1, 2, 3)
    ],
)
# Mock a third party function and its return value
def test_main_file_exists(x, y, z):
    with patch("src.main.os._exists", return_value=True) as mock_exists, patch("src.main.os.makedirs") as mock_makedirs:
        result = main(x, y)

        assert result == z
        mock_exists.assert_called_once()
        assert mock_makedirs.call_count == 0

# Mock a third party function and assert exception
def test_main_os_exception():
    with patch('src.main.os.makedirs', side_effect=OSError()) as mock_makedirs:
        with pytest.raises(OSError) as error_info:
            main(1, 0)

        # Please note the indent should be the same as raises exception
        assert error_info.typename == 'OSError' 
        mock_makedirs.assert_called_once()