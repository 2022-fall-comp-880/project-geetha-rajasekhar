# DESIGN DOCUMENT

## Investigative Question 1:
**What are the average TOEFL and GRE score of all students in this university?**
*  The input for this question will be the TOEFL and GRE columns from the dataset.
* the input is used to create an average by getting the data from the file as a list.
* An accumulator called `sumg` is used to get the sum of the Gre score. At first the accumulator is initialized with zero.
* An accumulator called `sumt` is used to get the sum of TOEFL scores.At first the accumulator is initialized with zero.
* for loop is used to create the sum by iterating through the both lists.
* after obtaining the sums average is created by dividing the `sumg` and `sumt` with the number of values in the list.
* the outcome for this question will be a float with the average scores.

## Investigative Question 2:
*What is the probability of getting admission in the university based on average scores?*
* The inputs for this question is a list of GRE and a list of TOEFL scores from the dataset and the average values of `sumg` and `sumt`.
* Each  individual scores are compared with the average scores to determine weather the students have a chance of getting into the university.
* Using if else statement the comparison can be done between the average scores and the actual scores.
* The outcome for this question would be a list of scores.

## Investigative Question 3:
**What is the list of universities that got a particular rating.**
*  A histogram of score ratings and university serial number.
* The inputs for this Questions will be the ratings and Serial No from the dataset.
* An accumulator called `hist` is initialized to an empty dictionary.
* using for loop the input list can be transversed and then the ratings can be checked with the help of an if else statement.
* The output for this method will be a dictionary with key as rating value and value will be a list of serial numbers of colleges.

## Class Admissions:
* the class `Admission` will have three methods each to represent each Investigative questions and a constructor method.
* The names of the methods would be average_value_calculation, probability_prediction and histogram_Calculation.
* These methods can be used to answer the investigative questions through a program.
* main method can be used to print the results using objects.


