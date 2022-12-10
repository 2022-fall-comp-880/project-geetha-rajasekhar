"""Test gender frequency by country."""

import unittest
import os
from apps.main import Admissions


class TestProbabilityPrediction(unittest.TestCase):
    """Test gender_freq_by_country() method."""

    def setUp(self):
        """Create DevStats objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.adm_data_empty = Admissions(f'{data_dir}/adm_empty.csv')
        self.adm_data_5 = Admissions(f'{data_dir}/adm_five.csv')
        self.adm_data_10 = Admissions(f'{data_dir}/adm_last_ten.csv')
        self.adm_data_all = Admissions(f'{data_dir}/adm_data.csv')

    def test_probability_multiple_entries(self):
        """Test case 1 using stats.txt."""
        actual_result = self.adm_data_all.probability_prediction()
        expected_result = [(1, 337, 118), (4, 322, 110), (6, 330, 115),
                           (7, 321, 109), (10, 323, 108), (12, 327, 111),
                           (13, 328, 112), (19, 318, 110), (22, 325, 114),
                           (23, 328, 116), (24, 334, 119), (25, 336, 119),
                           (26, 340, 120), (27, 322, 109), (33, 338, 118),
                           (34, 340, 114), (35, 331, 112), (36, 320, 110),
                           (44, 332, 117), (45, 326, 113), (46, 322, 110),
                           (47, 329, 114), (48, 339, 119), (49, 321, 110),
                           (50, 327, 111), (53, 334, 116), (54, 324, 112),
                           (55, 322, 110), (65, 325, 111), (66, 325, 112),
                           (67, 327, 114), (69, 318, 109), (70, 328, 115),
                           (71, 332, 118), (72, 336, 112), (73, 321, 111),
                           (76, 329, 114), (77, 327, 112), (82, 340, 120),
                           (83, 320, 110), (84, 322, 115), (85, 340, 115),
                           (98, 331, 120), (99, 332, 119), (100, 323, 113),
                           (105, 326, 112), (107, 329, 111), (108, 338, 117),
                           (109, 331, 116), (112, 321, 109), (114, 320, 110),
                           (121, 335, 117), (122, 334, 119), (127, 323, 113),
                           (128, 319, 112), (129, 326, 112), (130, 333, 118),
                           (131, 339, 114), (134, 323, 112), (135, 333, 113),
                           (139, 326, 116), (140, 318, 109), (141, 329, 110),
                           (142, 332, 118), (143, 331, 115), (144, 340, 120),
                           (145, 325, 112), (146, 320, 113), (148, 326, 114),
                           (149, 339, 116), (151, 334, 114), (152, 332, 116),
                           (153, 321, 112), (155, 326, 108), (163, 318, 109),
                           (165, 329, 111), (166, 322, 110), (172, 334, 117),
                           (173, 322, 110), (174, 323, 113), (175, 321, 111),
                           (176, 320, 111), (177, 329, 119), (178, 319, 110),
                           (186, 327, 113), (188, 335, 118), (189, 331, 115),
                           (190, 324, 112), (191, 324, 111), (192, 323, 110),
                           (193, 322, 114), (194, 336, 118), (203, 340, 120),
                           (204, 334, 120), (211, 325, 108), (212, 328, 110),
                           (213, 338, 120), (214, 333, 119), (215, 331, 117),
                           (216, 330, 116), (217, 322, 112), (218, 321, 109),
                           (219, 324, 110), (223, 324, 113), (229, 318, 112),
                           (230, 324, 111), (235, 330, 113), (236, 326, 111),
                           (237, 325, 112), (238, 329, 114), (243, 324, 115),
                           (244, 325, 114), (246, 328, 110), (249, 324, 110),
                           (250, 321, 111), (254, 335, 115), (255, 321, 114),
                           (260, 331, 119), (261, 327, 108), (264, 324, 111),
                           (265, 325, 110), (269, 327, 113), (276, 322, 110),
                           (277, 329, 113), (282, 317, 110), (284, 321, 111),
                           (285, 340, 112), (286, 331, 116), (287, 336, 118),
                           (288, 324, 114), (298, 320, 120), (299, 330, 114),
                           (302, 319, 108), (306, 321, 109), (307, 323, 110),
                           (308, 325, 112), (312, 328, 108), (319, 324, 111),
                           (320, 327, 113), (326, 326, 116), (329, 324, 112),
                           (331, 327, 113), (334, 319, 108), (336, 325, 111),
                           (337, 319, 110), (338, 332, 118), (339, 323, 108),
                           (342, 326, 110), (352, 325, 110), (357, 327, 109),
                           (361, 322, 110), (362, 334, 116), (363, 338, 115),
                           (366, 330, 114), (372, 324, 110), (373, 336, 119),
                           (374, 321, 109), (383, 324, 110), (385, 340, 113),
                           (386, 335, 117), (390, 320, 108), (393, 326, 112),
                           (395, 329, 111), (396, 324, 110), (398, 330, 116),
                           (400, 333, 117)]
        self.assertListEqual(actual_result, expected_result)

    def test_probability_ten_entries(self):
        """Test case 2 using stats_10.txt with ten rows."""
        actual_result = self.adm_data_10.probability_prediction()
        expected_result = [(393, 326, 112), (395, 329, 111), (396, 324, 110),
                           (398, 330, 116), (400, 333, 117)]
        self.assertListEqual(actual_result, expected_result)

    def test_probability_five_entries(self):
            """Test case 3 using s tats_1.txt with one row."""
            actual_result = self.adm_data_5.probability_prediction()
            expected_result = [(1, 337, 118)]
            self.assertListEqual(actual_result, expected_result)

    def test_probability_zero_entries(self):
            """Test case 3 using stats_1.txt with one row."""
            actual_result = self.adm_data_empty.probability_prediction()
            expected_result = []
            self.assertListEqual(actual_result, expected_result)



    def test_probability_zero_entries(self):
        """Test case 3 using stats_1.txt with one row."""
        actual_result = self.adm_data_empty.probability_prediction()
        expected_result = []
        self.assertListEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()
