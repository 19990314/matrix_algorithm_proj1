
*************************************************************************************
************************************ README *****************************************
*************************************************************************************

Files overview:
This project is implemented in a folder called Project1_ShutingChen.
Project1_ShutingChen/
	test_cases/
	bad_input_cases/
	outputs/
	main.py
	matrix_multiply.py
	IO_tools.py
	result_check.py
	matrix_generator.py

test_cases/: all the test case of input files
bad_input_cases/: all the bad inputs I generated for testing
outputs/: sample outputs, including the output I used for analysis
main.py: the main steps of matrix calculation and analysis.
matrix_multiply.py: supporting matrix multiplication by Strassen's algorithm the ordinary multiplication method
IO_tools.py: handle I/O functions
result_check.py: 
rmatrix_generator.py: used as my self testing of I/O issues and the algorithm's correctness.

************************************************************************************

Compile the program:

This program is written in python3.10. Please run it through command line in this format:

python3 main.py input verbose_flag

Other packages:
package    version
---------- -------
numpy      1.23.3


************************************************************************************

Parameters:
	main.py: python main file.
	input: the input file name containing your matrices of interest
	verbose_flag: this is an optional parameter declaring the output verbose or not. Only when you declare 0, the output will be simplified, which is printing the statistics about the multiplication counts by each strategy. Otherwise, the normal output would contain the input matrices, the result matrix, and corresponding statistics.


[Example]:
python3 main.py test_cases/LabStrassenInput.txt > outputs/out_LabStrassenInput.txt
It will print the full outputs.

python3 main.py test_cases/LabStrassenInput.txt > outputs/out_LabStrassenInput.txt 0
It will print the only the statistics.


************************************************************************************

Input:

A correct input format, referring to project rubric, is: the first line should contain the order of the matrix, then the first matrix, in row major order, then the second matrix. This is followed by a blank line, then the order of the next matrix pair and so on. You need to collect enough data to have a meaningful comparison of the theoretical efficiency to the observed efficiency.

Here are some potential input errors which has been handled in this project:

[File issues]:
File is empty.
File does not exist.
File path is wrong.

[Format issues]:
Missing a column.
Missing a row.
Missing an item.
Missing the n value.
N value not consistent to the matrices.
Missing the blank line between the input sets.
Extra space between matrix elements.
Non-integer elements in the matrix.
************************************************************************************

Output:

./test_cases/test_n.txt:
This file contains matrix inputs which n = 2,4,8,16,32,64,128.

python: python3.10

Output:
python3 main.py test_cases/LabStrassenInput.txt > outputs/out_LabStrassenInput.txt

python3.10 main.py test_cases/test_n.txt  > outputs/out_test_n.txt


*************************************************************************************
