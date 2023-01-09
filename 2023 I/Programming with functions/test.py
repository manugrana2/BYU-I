
import math
import os
import random
import re
import sys
from datetime import datetime
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s="07:05:45PM"):
    time = datetime.strptime(s, "%I:%M:%S%p")
    result = datetime.strftime(time, "%H:%M:%S%p")
    return(result)



print((timeConversion("07:05:45PM")))
