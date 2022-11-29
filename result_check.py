# ------------------------------------------------------------------------
# This module is using for testing project I/O issues and the algorithm's
# correctness.
#
# Author: Shuting Chen
# Date Created: 09/22/2022
# Date Last Modified: 09/25/2022
# ------------------------------------------------------------------------

import sys
import os
from matrix_multiply import *
from IO_tools import *
import numpy as np  # only used as a double-check for my strassen's algorithm

# check if file is empty
try:
    if os.stat(sys.argv[1]).st_size == 0:
        print("Empty File! Please check file content.")
        exit(0)
    else:
        verbose = True
        if len(sys.argv) > 2:
            if sys.argv[2] == "0":
                verbose = False
except FileNotFoundError as file_error:
    print("Cannot find the File! Please check file path.")
    exit(0)

# read input file, save matrices into matrices_container
matrices_container = []
with open('./test_cases/test_n.txt', encoding='utf8') as f:
    size_flag = False
    input = []
    # process matrix line by line
    for line in f:
        try:
            line = line.strip("\n")
            if size_flag == False:
                n = int(line)
                size_flag = True
                continue
            elif line == "":
                matrices_set = matrices_set_reader(n, input)
                matrices_container.append(matrices_set)
                size_flag = False
                input = []
            else:
                input.append(line)
        except ValueError as ve:
            print('Error! Check your input format.')
            print('Error line:' + line)
            exit(0)
    matrices_set = matrices_set_reader(n, input)
    matrices_container.append(matrices_set)

# complete multiplication by both the the ordinary and Strassen's strategies
job_index = 0
for i in matrices_container:
    job_index += 1
    C_strassen, ct_strassen = strassen_multiply(i["A"], i["B"])
    C_ordinary, ct_ordinary = ordinary_multiply(i["A"], i["B"])
    C_numpy = np.dot(i["A"], i["B"])
    print("============= " + str(i["n"]) + " * " + str(i["n"]) + " Matrix Multiplication" + " =============")
    if np.array_equal(C_strassen, C_numpy) == True:
        print("Strassen's method correctness [PASS]")
    else:
        print("Strassen's method [FAILED]")
    if np.array_equal(C_ordinary, C_numpy) == True:
        print("Ordinary method correctness [PASS]")
    else:
        print("Ordinary method correctness [FAILED]")
    output_generator(C_strassen, i, [ct_ordinary, ct_strassen], output=verbose)
