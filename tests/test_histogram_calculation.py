"""Test programming languages by country."""

import unittest
import os
from apps.main import Admissions


class TestHistogramCalculation(unittest.TestCase):
    """Test `programming_language_histogram()` method."""

    def setUp(self):
        """Create DevStats objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.adm_data_empty = Admissions(f'{data_dir}/adm_empty.csv')
        self.adm_data_5 = Admissions(f'{data_dir}/adm_five.csv')
        self.adm_data_10 = Admissions(f'{data_dir}/adm_last_ten.csv')
        self.adm_data_all = Admissions(f'{data_dir}/adm_data.csv')

    def test_histogram_multiple_entries(self):
        """Test case 1 using stats.txt."""
        actual_result = self.adm_data_all.histogram_calculation()
        expected_result = {
            4: [1, 2, 12, 13, 22, 33, 44, 50, 53, 54, 66, 70, 74, 82, 86, 90,
                96, 99, 107, 108, 112, 116, 118, 123, 125, 136, 144, 149, 151,
                165, 173, 174, 175, 176, 177, 186, 211, 212, 213, 215, 217,
                218, 219, 223, 230, 237, 246, 254, 255, 256, 259, 260, 269,
                270, 285, 289, 308, 310, 312, 313, 320, 329, 335, 336, 352,
                362, 366, 373, 383, 385, 393, 395, 398, 400],
            3: [3, 4, 7, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 32, 41, 49,
                51, 55, 56, 57, 62, 65, 67, 69, 75, 77, 81, 87, 89, 92, 95, 98,
                100, 101, 105, 106, 113, 115, 117, 124, 126, 127, 128, 129,
                137, 147, 148, 154, 155, 156, 157, 163, 164, 167, 168, 178,
                179, 180, 181, 184, 187, 195, 199, 200, 201, 205, 208, 210,
                220, 221, 222, 229, 231, 232, 239, 243, 244, 247, 249, 250,
                251, 257, 258, 262, 264, 266, 268, 276, 281, 282, 283, 284,
                290, 297, 298, 299, 300, 304, 306, 307, 309, 311, 314, 319,
                321, 322, 325, 326, 327, 331, 333, 334, 337, 341, 342, 343,
                350, 351, 354, 357, 361, 365, 367, 372, 374, 381, 382, 384,
                390, 392, 396, 397, 399],
            2: [5, 8, 28, 30, 31, 37, 40, 42, 43, 52, 58, 60, 61, 63, 64, 68,
                76, 78, 79, 88, 91, 93, 94, 97, 102, 103, 104, 114, 119, 138,
                139, 141, 142, 145, 146, 150, 158, 159, 169, 170, 171, 182,
                183, 185, 196, 197, 198, 202, 206, 207, 209, 224, 225, 226,
                227, 228, 233, 234, 242, 245, 248, 252, 253, 263, 265, 267,
                271, 272, 278, 279, 280, 291, 292, 293, 295, 296, 301, 302,
                303, 305, 315, 316, 317, 323, 324, 328, 330, 332, 344, 345,
                347, 353, 355, 356, 358, 359, 360, 364, 371, 375, 376, 377,
                387, 388, 389, 391, 394],
            5: [6, 23, 24, 25, 26, 27, 34, 35, 36, 45, 46, 47, 48, 71, 72, 73,
                83, 84, 85, 109, 110, 111, 120, 121, 122, 130, 131, 132, 133,
                134, 135, 143, 152, 153, 166, 172, 188, 189, 190, 191, 192,
                193, 194, 203, 204, 214, 216, 235, 236, 238, 261, 277, 286,
                287, 288, 338, 339, 340, 363, 386],
            1: [9, 29, 38, 39, 59, 80, 140, 160, 161, 162, 240, 241, 273, 274,
                275, 294, 318, 346, 348, 349, 368, 369, 370, 378, 379, 380]}
        self.assertDictEqual(actual_result, expected_result)

    def test_histogram_ten_entries(self):
        """Test case 2 using stats_10.txt with ten rows."""
        actual_result = self.adm_data_10.histogram_calculation()
        expected_result = {2: [391, 394], 3: [392, 396, 397, 399],
                           4: [393, 395, 398, 400]}
        self.assertDictEqual(actual_result, expected_result)

    def test_histogram_five_entries(self):
        """Test case 3 using s tats_1.txt with one row."""
        actual_result = self.adm_data_5.histogram_calculation()
        expected_result = {2: [5], 3: [3, 4], 4: [1, 2]}
        self.assertDictEqual(actual_result, expected_result)

    def test_histogram_zero_entries(self):
        """Test case 3 using stats_1.txt with one row."""
        actual_result = self.adm_data_empty.histogram_calculation()
        expected_result = {}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
