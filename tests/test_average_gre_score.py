import unittest
import os
from apps.main import Admissions


class TestAverageGREScore(unittest.TestCase):
    """Test `average_salary_by_job_satisfaction()` method."""

    def setUp(self):
        """Create DevStats objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.adm_data_empty = Admissions(f'{data_dir}/adm_empty.csv')
        self.adm_data_5 = Admissions(f'{data_dir}/adm_five.csv')
        self.adm_data_10 = Admissions(f'{data_dir}/adm_last_ten.csv')
        self.adm_data_all = Admissions(f'{data_dir}/adm_data.csv')

    def test_average_multiple_entries(self):
        """Test case 1 using stats.txt."""
        actual_result = self.adm_data_all.average_value_calculation('GRE Score')
        expected_result = 316.8075
        self.assertEqual(actual_result, expected_result)

    def test_average_ten_entries(self):
        """Test case 2 using stats_10.txt with ten rows."""
        actual_result = self.adm_data_10.average_value_calculation('GRE Score')
        expected_result = 322.8
        self.assertEqual(actual_result, expected_result)

    def test_average_five_entries(self):
        """Test case 3 using stats_1.txt with one row."""
        actual_result = self.adm_data_5.average_value_calculation('GRE Score')
        expected_result = 322.6
        self.assertEqual(actual_result, expected_result)

    def test_average_zero_entries(self):
        """Test case 3 using stats_1.txt with one row."""
        actual_result = self.adm_data_empty.average_value_calculation('GRE Score')
        expected_result = None
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
