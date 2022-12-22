
# Project Report
* Authors: Geethanjali, Rajashekar
## 1. Purpose
* Author : Geethanjali
### What does the program do? 
* Data that is maintained include student demographic data, academic test scores (TOEFL, GRE, etc.), grade point averages, (GPAs) and all transcript information. One of the difficult task to handle the admission process for universities and the colleges This project help the universities to given admissions based on average scores.
* The dataset is taken from kaggle `https://www.kaggle.com/datasets/akshaydattatraykhare/data-for-admission-in-the-university`.
* The dataset is created by `Akshay Dattatray`.
* The dataset was updated two months ago.
* The `Data for Admission in the University` dataset contains 9 columns and 400 rows.
* The Columns or Attributes in the dataset are:
- Serial No: It is the serial number allocated to each university.
- GRE Score : The GRE score required to get admission in that university.
- TOEFL Score: The TOEFL score required to get admission in that university.
- University Rating: Ratings given to each university.
- SOP: Sop rating required to get admission in that university.
- LOR: LOR rating required to get admission in that university.
- CGPA: CGPA rating required to get admission in that university.
- Research: tells weather research option is present in that particular university. If research option is present then 1 is given, if not 0 is given.
- Chance of Admit: Chance of getting admission in that university.
* Investigative Questions:
- 1.What are the average scores of all the universities GRE and TOEFL scores?
- 2.Which universities stand above the average score of both GRE and TOEFL? 
- 3.Which University got what rating?

## 2. Approach 
* Author: Geethanjali
### What are the average scores of all the universities GRE and TOEFL scores?
* With the help of the `Data for Admission in the University` we have created a dictionary called `data_dict`.
* We are using exception handling incase there is any problem with the code.
* An Accumulator called `Sum` is initialized with zero at the start.
* Using for loop each value can be added to the `Sum` by gradually iterating each value of `data_dict`.
* The value in the `sum` will be transformed with each for loop iteration adding the value at that index of the `data_dict`
* The value in the `sum` is divided by the length of the `data_dict` to get the average values.
* The Return value for this method is a float value.
### Which universities stand above the average score of both GRE and TOEFL? 
* The data form `data_dict` is used in this question to get the university score which are greater than the average scores.
* an empty list called `out` is used as an accumulator.
* for loop is used to iterate through each value of the `data_dict`.
* The condition for the first key in the `data_dict` is checked because it is a string and cannot be compared with integer values.
* Using the Average scores from the previous question, The average values are compared with the university values using an if statement.
* Only if Both the GRE and TOEFL values are more than the average values then only the value is added to the `out` list.
* Using values as the indexes the values are added.
* the return value is a list of tuples, Containing the serial num, GRE score, and TOEFL scores of the universities greater than the average value.
### 3.Which University got what rating?
* An accumulator called `out` is initialized with an empty dictionary.
* a for loop is used to iterate through each value of `data_dict`.
* Because we want to exclude the first row of `data_dict`, reason being it contains the Attribute names and not the data.
* a variable called `temp` is used to store a particular iteration values from the `data_dict`.
* if statement is used to check if the key of the rating is already present in the `out` dictionary, If the key is present then the University Serial number is added as value to that particular key.
* if the key is not present then a new key is created and the serial number is then added.
* The return value is a dictionary with key as rating and value as a list of university serial numbers with that particular rating.
## 3. Testing 
* `unittest` module is imported to write testcases and evaluate the result using assert statements.
* `os` module is used to create the file paths.
## class TestAverageGREScore(unittest.TestCase):
Writer: Geethanjali
* This class is created to test the `average_value_calculation('GRE Score')` method in the `Admissions` class .
### def test_average_multiple_entries(self):
* In this method the data in `adm_data.csv'` file is tested.
* The `actual_result` is calculated by calling `average_value_calculation('GRE Score')` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.
### def test_average_zero_entries(self):
* In this method the data in `adm_empty.csv` file is tested.
* The `actual_result` is calculated by calling `average_value_calculation('GRE Score')` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.
### test_average_five_entries(self):
* In this method the data in `adm_five.csv'` file is tested.
* The `actual_result` is calculated by calling `average_value_calculation('GRE Score')` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.
### def test_average_ten_entries(self):
* In this method the data in `adm_ten.csv'` file is tested.
* The `actual_result` is calculated by calling `average_value_calculation('GRE Score')` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.

## class TestProbabilityPrediction(unittest.TestCase):
* Author: Geethanjali
* This class is created to test the `probability_prediction()` method in the `Admissions` class .
### def test_average_multiple_entries(self):
* In this method the data in `adm_data.csv'` file is tested.
* The `actual_result` is calculated by calling `probability_prediction()` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.
### def test_average_zero_entries(self):
* In this method the data in `adm_empty.csv` file is tested.
* The `actual_result` is calculated by calling `probability_prediction()` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.
### test_average_five_entries(self):
* In this method the data in `adm_five.csv'` file is tested.
* The `actual_result` is calculated by calling `probability_prediction()` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.
### def test_average_ten_entries(self):
* In this method the data in `adm_ten.csv'` file is tested.
* The `actual_result` is calculated by calling `probability_prediction()` method of the `Admissions ` class with the field GRE Score.
* The `expected_result` is precalculated using pandas.
* Using the assertEqual statement the `actual_result` and `expected_result` is compared.
* if the contents are equal then the testcase will pass.



