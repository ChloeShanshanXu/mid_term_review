from unittest import TestCase
from classes_and_test import Pizza

class TestPizza(TestCase):
    def test_get_total_price(self):
        # Arrange
        expected_result = 16.5

        # Act
        nice = Pizza(['pineapple', 'ham', 'mushrooms'], 3)
        actual_result = nice.get_total_price()

        # Assert
        self.assertEqual(expected_result, actual_result)
