import os
import sys
import glob
import re
import itertools

if len(sys.argv) != 3:
    sys.exit("please specify filepath and search keyword. Ex. python print_previousline_by_keyword.py #{filepath} #{searchKeyword1}")
    
filepath = sys.argv[1];
keyword = sys.argv[2]
print "search file:", filepath
print 'keyword:', keyword;     
 
for subdir, dirs, filenames in os.walk(filepath):
    for filename in filenames:
        absoluteFilePath = os.path.join(subdir, filename)
        print('process:' + absoluteFilePath)

        previousLine = ''
        with open(absoluteFilePath) as file:
            for line in file.readlines():
                if keyword in line:
                    print previousLine
                    print line
                    print '============================================'
                previousLine = line
            
                