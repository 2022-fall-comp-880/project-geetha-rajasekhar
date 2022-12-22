# DESIGN DOCUMENT

## Investigative Question 1:
**What are the average TOEFL and GRE score of all students in this university?**
*  The input for this question will be the TOEFL and GRE columns from the dataset.
* the input is used to create an average by getting the data from the file as a list.
* An accumulator called `sum` is used to get the sum of the Gre score. At first the accumulator is initialized with zero.
* for loop is used to create the sum by iterating through the both lists.
* after obtaining the sums average is created by dividing the `sum` with the number of values in the list.
* the outcome for this question will be a float with the average scores.

## Investigative Question 2:
*What is the probability of the university Score being more than the average scores?*
* With the help of the `Data for Admission in the University` we have created a dictionary called `data_dict`.
* We are using exception handling incase there is any problem with the code.
* An Accumulator called `Sum` is initialized with zero at the start.
* Using for loop each value can be added to the `Sum` by gradually iterating each value of `data_dict`.
* The value in the `sum` will be transformed with each for loop iteration adding the value at that index of the `data_dict`
* The value in the `sum` is divided by the length of the `data_dict` to get the average values.
* The Return value for this method is a float value.
## Investigative Question 3:
**What is the list of universities that got a particular rating.**
*  A histogram of score ratings and university serial number.
* The inputs for this Questions will be the ratings and Serial No from the dataset.
* An accumulator called `out` is initialized to an empty dictionary.
* using for loop the input list can be transversed and then the ratings can be checked with the help of an if else statement.
* The output for this method will be a dictionary with key as rating value and value will be a list of serial numbers of colleges.

## Class Admissions:
* the class `Admission` will have three methods each to represent each Investigative questions and a constructor method.
* The names of the methods would be average_value_calculation, probability_prediction and histogram_Calculation.
* These methods can be used to answer the investigative questions through a program.
* main method can be used to print the results using objects.
### def __init__(self, filename: str):
* This method is constructor method used to initialize the instance variables such as filename.
### def __str__(self):
* This method is used to format the strings.
### def csv_to_dict(self):
* In this method is used to read data from the csv file into a dictionary.
* Using with open method to read data as filename from a csv file.
* using for loop the data is iterated from an enumerate function to get the index values as well
* returning that `data_dict`.
### def main():
* This method is used to call all the meathods of `Admission class` with the help of an object called `out`.


