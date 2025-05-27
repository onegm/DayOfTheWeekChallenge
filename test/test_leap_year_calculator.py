from ..leap_year_calculator import is_leap_year
from unittest import TestCase


class TestLeapYearCalculator(TestCase):
    leap_years = [1604, 1728, 1840, 1964, 2020, 2028]
    leap_years_400 = [1600, 2000, 2400]
    not_leap_years = [1603, 1726, 1833, 1962, 2014, 2025, 2034]
    not_leap_years_100 = [1700, 1800, 1900, 2100, 2200]

    def test_is_leap_year_divisible_by_4(self):
        for year in self.leap_years:
            self.assertTrue(is_leap_year(year))

    def test_is_leap_year_divisible_by_400(self):
        for year in self.leap_years_400:
            self.assertTrue(is_leap_year(year))

    def test_is_not_leap_year_divisible_by_4(self):
        for year in self.not_leap_years:
            self.assertFalse(is_leap_year(year))

    def test_is_not_leap_year_divisible_by_100(self):
        for year in self.not_leap_years_100:
            self.assertFalse(is_leap_year(year))


