"""
Represents a data-set of Admissions

Authors:Geethanjali Allam, Rajasekhar Dasari
"""


class Admissions:
    """
     Represents a dataset of Admission of a few universities.
     Attributes:
     filename: string
     """

    def __init__(self, filename: str):
        """
        Initialize instance variables.

        Parameters:
            filename: string
        """
        self.filename = filename

    def read_to_list(self, value):
        """
        Reads data from a csv file to the list.
        Return: List
        """

    def average_value_calculation(self):
        """
        Calculates Average values for GRE and TOEFL scores with the help of a dataset.

        Creates and returns a float value as average GRE and TOEFL scores

        Return: float
        """

    def probability_prediction(self) -> list:
        """ Creates a list With the probability weather the student can get admission in  the university or not.

        gets average values from average_value_calculation() method and compares them with individual university scores.

        Returns : List
        """

    def histogram_Calculation(self) -> dict:
            """
             Create a dictionary of university serial number with a particular rating.

             Returns:
                dictionary
                    keys : integer, rating
                    values : list of integers, representing a particular university
            """

def main():
        """Run code to check basic functionality."""
