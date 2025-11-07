import glob
import os
files = glob.glob('/tmp/pigoutput110/part*')
for f in files:
    with open(f, 'rb') as of:
        print(of.readlines())