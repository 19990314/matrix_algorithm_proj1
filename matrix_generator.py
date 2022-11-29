# ------------------------------------------------------------------------
# This module is used for generating testing cases.
#
# Author: Shuting Chen
# Date Created: 09/22/2022
# Date Last Modified: 09/25/2022
# ------------------------------------------------------------------------

import random

# modify n here
n = 128
for i in range(0,n*2):
    line = ""
    for j in range(0, n):
        line += str(random.randint(-5, 11))+ " "
    print(line)