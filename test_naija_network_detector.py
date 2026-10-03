import pytest

from naija_network_detector import detect_nigerian_network


@pytest.mark.parametrize(
    ('phone_number', 'expected'),
    [
        ('08033000000', 'MTN'),
        ('08050000000', 'Glo'),
        ('08090000000', '9mobile'),
        ('07025000000', 'visafone'),
        ('07026000000', 'visafone'),
        ('07027000000', 'multilinks'),
        ('07028000000', 'starcomms'),
        ('07029000000', 'starcomms'),
        ('2348033000000', 'MTN'),
        ('08040000000', 'Ntel'),
        ('07020000000', 'Smile'),
        ('07070000000', 'zoom'),
    ],
)
def test_detect_nigerian_network(phone_number, expected):
    assert detect_nigerian_network(phone_number) == expected


def test_invalid_number_format():
    assert detect_nigerian_network('12345') == 'Invalid Nigerian number format'
