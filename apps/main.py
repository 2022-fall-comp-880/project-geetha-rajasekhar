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
        Writer: rajshekar
        """
        self.filename = filename

    def __str__(self):
        """Convert to string representation."""
        return str(self.filename)

    def csv_to_dict(self):
        """
         Reading data from adm_data.csv file into a dictionary called df.
         Parameters: self
         use try and except block incase the file is not found
         accumulator data_dict is used to accumulate each row from the dataset as the value for dictionary.
         use with open method to open the file and read data from the file.
         using for loop to get the data directly using enumerate method.
         Returns: a dictionary with key as row number and values as list of contents in that row.
         Writer: Geethanjali

        """
        try:
            data_dict = {}
            with open(self.filename, encoding='utf-8', newline='') as csv_file:
                reader = csv.reader(csv_file)
                for count, row in enumerate(reader):
                    data_dict[count] = row
            return data_dict
        except Exception:
            return None

    def average_value_calculation(self, field):
        """
        Calculates Average values for GRE and TOEFL scores with the help of a dataset.
        Parameters: self, field
        accumulator called sum is used to calculate the sum of the row given in the field.
        using for loop each value is iterated and added to the sum.
        sum is divided by the length of the list to get the average
        returns: Average value of the field.

        Creates and returns a float value as average GRE and TOEFL scores

        Return: float


        Writer: Rajasekhar
        Reviewer: Geethanjali
        """
        try:
            Sum = 0
            data_dict = self.csv_to_dict()
            index_of_field = data_dict[0].index(field)
            for value in data_dict:
                if value != 0:
                    Sum += int(data_dict[value][index_of_field])
            return Sum / (len(data_dict) - 1)
        except Exception:
            return None

    def probability_prediction(self):
        """ Creates a list With the probability weather the student can get admission in  the university or not.

        Parameters: self
        gets average values from average_value_calculation() method and compares them with individual university scores.
        an empty list called out is used as accumulator to compare the data of different universities with average values.
        for loop is used to iterate through the data_dict.
        comparing each univercites score with the average score by calling the average_value_calculation() meathod.
        Returns : List of tuples.

        writer: Rajshekar , Geethanjali
        """
        try:
            out = []
            data_dict = self.csv_to_dict()
            for value in data_dict:
                if value != 0:
                    if self.average_value_calculation('GRE Score') < int(
                        data_dict[value][1]) and self.average_value_calculation(
                         'TOEFL Score') < int(data_dict[value][2]):
                        out.append(
                            (int(data_dict[value][0]), int(data_dict[value][1]), int(data_dict[value][2])))
            return out
        except Exception:
            return None

    def histogram_Calculation(self):
        """
             Create a dictionary of university serial number with a particular rating.
             using out as an accumulator by initializing it with an empty dictionary.
             using for loop to iterate through the data_dict.
             creating a variable called temp and assigning each iteration vales of data_dict to it.
             if the rating is already persent in the dictionary then append the serial num to the list.
             else create a new key with that rating and add that serial number as value.

             Returns:
                dictionary
                    keys : integer, rating
                    values : list of integers, representing a particular university

             Writer: Geethanjali
             Reviewer: Rajasekhar
        """
        try:
            out = {}
            data_dict = self.csv_to_dict()
            for value in data_dict:
                if value != 0:
                    temp = data_dict[value]
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
    print(out.csv_to_dict())
    print(out.average_value_calculation("GRE Score"))
    print(out.average_value_calculation("TOEFL Score"))
    print(out.histogram_Calculation())
    print(out.probability_prediction())


if __name__ == '__main__':
    main()
