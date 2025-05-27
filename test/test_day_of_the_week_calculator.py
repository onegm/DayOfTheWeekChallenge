import random
from unittest import TestCase
from datetime import datetime, timedelta
from ..day_of_the_week_calculator import get_day_of_the_week

class TestDayOfTheWeek(TestCase):
    def test_get_day_of_the_week_today(self):
        today = datetime.today()
        self.assertEqual(
            today.weekday(),
            get_day_of_the_week(
                today.day,
                today.month,
                today.year
            )
        )

    def test_get_day_of_the_week_yesterday(self):
        yesterday = datetime.today() - timedelta(days=1)
        self.assertEqual(
            yesterday.weekday(),
            get_day_of_the_week(
                yesterday.day,
                yesterday.month,
                yesterday.year
            )
        )

    def test_get_day_of_the_week_one_year_ago(self):
        some_day = datetime.today() - timedelta(weeks=52)
        some_day -= timedelta(days=random.randint(0, 6))
        self.assertEqual(
            some_day.weekday(),
            get_day_of_the_week(
                some_day.day,
                some_day.month,
                some_day.year
            )
        )

    def test_get_day_of_the_week_three_years_ago(self):
        some_day = datetime.today() - timedelta(weeks=52 * 3)
        some_day -= timedelta(days=random.randint(0, 6))
        self.assertEqual(
            some_day.weekday(),
            get_day_of_the_week(
                some_day.day,
                some_day.month,
                some_day.year
            )
        )

    def test_get_day_of_the_week_ten_years_ago(self):
        some_day = datetime.today() - timedelta(weeks=52*10)
        some_day -= timedelta(days=random.randint(0, 6))
        self.assertEqual(
            some_day.weekday(),
            get_day_of_the_week(
                some_day.day,
                some_day.month,
                some_day.year
            )
        )

    def test_get_day_of_the_week_one_year_later(self):
        some_day = datetime.today() + timedelta(weeks=52)
        some_day += timedelta(days=random.randint(0, 6))
        self.assertEqual(
            some_day.weekday(),
            get_day_of_the_week(
                some_day.day,
                some_day.month,
                some_day.year
            )
        )

    def test_get_day_of_the_week_three_years_later(self):
        some_day = datetime.today() + timedelta(weeks=52 * 3)
        some_day += timedelta(days=random.randint(0, 6))
        self.assertEqual(
            some_day.weekday(),
            get_day_of_the_week(
                some_day.day,
                some_day.month,
                some_day.year
            )
        )

    def test_get_day_of_the_week_ten_years_later(self):
        some_day = datetime.today() + timedelta(weeks=52 * 10)
        some_day += timedelta(days=random.randint(0, 6))
        self.assertEqual(
            some_day.weekday(),
            get_day_of_the_week(
                some_day.day,
                some_day.month,
                some_day.year
            )
        )