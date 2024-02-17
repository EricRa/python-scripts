"""
Zip all files in the current directory using only the standard library.  Uses the LZMA compression algorithm.  



Usage:



"""

import os
import sys
import subprocess
import lzma

from icecream import ic

ic(os.listdir())

def zip_std():