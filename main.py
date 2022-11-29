# ------------------------------------------------------------------------
# This module is the main file for Project 1, providing the main steps of
# matrix calculation and analysis.
#
# Author: Shuting Chen
# Date Created: 09/22/2022
# Date Last Modified: 09/25/2022
# ------------------------------------------------------------------------

import sys
import os
from matrix_multiply import *
from IO_tools import *

if __name__ == "__main__":
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
    with open(sys.argv[1], encoding='utf8') as f:
        size_flag = False
        input = []
        # process matrix line by line
        for line in f:
            try:
                line = line.strip(" ")
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
                exit(0)
        matrices_set = matrices_set_reader(n, input)
        matrices_container.append(matrices_set)

    # complete multiplication by both the the ordinary and Strassen's strategies
    job_index = 0
    for i in matrices_container:
        job_index += 1
        try:
            C, ct_strassen = strassen_multiply(i["A"],i["B"])
            C, ct_ordinary = ordinary_multiply(i["A"], i["B"])
        except ValueError as ve:
            print('Error! Check your matrix dimension.')
            exit()
        print("=================Matrix Multiplication Set #" + str(job_index) + "=================")
        output_generator(C, i, [ct_ordinary, ct_strassen], output=verbose)
