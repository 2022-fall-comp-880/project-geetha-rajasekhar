"""
Represents a data-set of Admissions

Authors:Geethanjali Allam, Rajasekhar Dasari
"""
import os
import csv


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

    def __str__(self):
        """Convert to string representation."""
        return str(self.filename)

    def csv_to_dict(self):
        """ Reading data from adm_data.csv file into a dictionary called df."""
        try:
            df = {}
            with open(self.filename, encoding='utf-8', newline='') as csv_file:
                reader = csv.reader(csv_file)
                for count, row in enumerate(reader):
                    df[count] = row
            return df
        except Exception:
            return None

    def average_value_calculation(self, field):
        """
        Calculates Average values for GRE and TOEFL scores with the help of a dataset.

        Creates and returns a float value as average GRE and TOEFL scores

        Return: float

        Writer: Rajasekar
        Reviewer: Geethanjali
        """
        try:
            Sum = 0
            df = self.csv_to_dict()
            index_of_field = df[0].index(field)
            for i in df:
                if i != 0:
                    Sum += int(df[i][index_of_field])
            return Sum / (len(df) - 1)
        except Exception:
            return None

    def probability_prediction(self) -> list:
        """ Creates a list With the probability weather the student can get admission in  the university or not.

        gets average values from average_value_calculation() method and compares them with individual university scores.

        Returns : List of tuples.
        """


    def histogram_calculation(self) -> dict:
        """
             Create a dictionary of university serial number with a particular rating.

             Returns:
                dictionary
                    keys : integer, rating
                    values : list of integers, represening a particular university
             Writer: Geethanjali
             Reviewer: Rajasekar
            """
        try:
            out = {}
            df = self.csv_to_dict()
            for i in df:
                if i != 0:
                    temp = df[i]
                    if int(temp[3]) in out:
                        out[int(temp[3])].append(int(temp[0]))
                    else:
                        out[int(temp[3])] = [int(temp[0])]
            return out
        except Exception:
            return None


def main():
    """Run code to check basic functionality."""
    data_dir = os.path.dirname(__file__) + "/../data"
    out = Admissions(f'{data_dir}/adm_data.csv')
    print(out.average_value_calculation("GRE Score"))
    print(out.average_value_calculation("TOEFL Score"))
    print(out.histogram_calculation())


if __name__ == '__main__':
    main()
