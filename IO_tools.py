# ------------------------------------------------------------------------
# This module handle I/O functions and issues of matrix input and output for Project 1.
#
# Author: Shuting Chen
# Date Created: 09/22/2022
# Date Last Modified: 09/25/2022
# ------------------------------------------------------------------------

def matrix_print(m):
    """
            print a matrix.

            m: 2D matrix as output
            Return:
                None
    """
    for i in range(0, len(m)):
        line = ""
        for j in range(0, len(m[i])):
            line += str(m[i][j]) + "  "
        print(line)


def dimension_check(input_set):
    """
        Check the dimension of matrix.

        input_set: input matrix store in 2D array
        Return:
            -1: matrix fails to pass dimension check
            0: matrix pass dimension check
    """
    if len(input_set['A']) != input_set['n'] or len(input_set['B']) != input_set['n']:
        return -1
    for i in range(0, input_set['n']):
        if len(input_set['A'][i]) != input_set['n'] or len(input_set['B'][i]) != input_set['n']:
            return -1
    return 0


def matrices_set_reader(n, input):
    """
        Read lines from the file input into a dictionary

        input_set:
            n:  the row/column length of the matrix
            input: input matrix store in 2D array

        Return:
            input_set: a dictionary which contains the matrices and n
    """
    input_set = {}
    input_set['n'] = n
    input_set['A'] = []
    input_set['B'] = []
    try:
        for i in range(0, n):
            row = list(map(int, input[i].split(" ")))
            input_set['A'].append(row)
        for i in range(0, n):
            row = list(map(int, input[n + i].split(" ")))
            input_set['B'].append(row)
    except ValueError as ve:
        print('Error! Check your input file.')
        print('Error line:' + str(input))
        print('Referring input rubric: The first line should contain the order of the '
              'matrix, then the first matrix, in row major order, then the second '
              'matrix. This is followed by a blank line, then the order of the next '
              'matrix pair and so on. You need to collect enough data to have a meaningful '
              'comparison of the theoretical efficiency to the observed efficiency.')
        exit()
    except IndexError as ie:
        print('Error! Your matrices has inconsistent dimensions.')
        print(input)
        exit()

    # check matrix's dimensions
    if dimension_check(input_set) != 0:
        print("Error! Your matrices has inconsistent dimensions.")
        print('Error line:' + str(input))
        print("Please make sure: 1. n is power of two; 2. Two matrices are both n*n.")
        exit()
    return input_set


def output_generator(result, inputs, stas, output):
    """
            Generate outputs after multiplication is done

            input_set:
                result:  the result matrix C
                inputs: input matrices
                stats: count of multiplications
                output: a boolean which identifies if the user want
                        to print out the matrices, or just the statistics

            Return: none
        """
    if output == True:
        print("Input Matrices:")
        for i in range(0, inputs["n"]):
            print(f'{str(inputs["A"][i]): <{inputs["n"] * 4}}' + " | " + str(inputs["B"][i]))
        print("Product:")
        matrix_print(result)
    print("Numer of multiplications by Ordinary Matrix Multiplication: " + str(stas[0]))
    print("Numer of multiplications by Strassen's Algorithm: " + str(stas[1]))
    print("\n")
