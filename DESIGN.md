# DESISIGN DOCUMENT

## Investigative Question 1:
**What are the average TOEFL and GRE score of all students in this university?**
*  The input for this question will be the TOEFL and GRE columns from the dataset.
* the input is used to create an average by getting the data from the file as a list.
* An accumulator called `sumg` is used to get the sum of the Gre score. At first the accumulator is initialized with zero.
* An accumulator called `sumt` is used to get the sum of TOEFL scores.At first the accumulator is initialized with zero.
* for loop is used to create the sum by iterating through the both lists.
* after obtaining the sums average is created by dividing the `sumg` and `sumt` with the number of values in the list.
* the outcome for this question will be a float with the average scores.
## Investigative Question 3:
**What is the list of universities that got a particular rating.**
*  A histogram of score ratings and university serial number.
* The inputs for this Questions will be the ratings and Serial No from the dataset.
* An accumulator called `hist` is initialized to an empty dictionary.
* using for loop the input list can be transversed and then the ratings can be checked with the help of an if else statement.
* The output for this method will be a dictionary with key as rating value and value will be a list of serial numbers of colleges.


