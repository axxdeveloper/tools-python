import os
import sys
import glob
import re
import itertools

if len(sys.argv) != 3:
    sys.exit("please specify filepath and search keyword. Ex. python print_previousline_by_keyword.py #{filepath} #{searchKeyword}")
    
filepath = sys.argv[1];
keyword = sys.argv[2]
print "search file:", filepath
print 'keyword:', keyword;     
 
foundKeyWords = set()
for subdir, dirs, filenames in os.walk(filepath):
    for filename in filenames:
        absoluteFilePath = os.path.join(subdir, filename)
        print('process:' + absoluteFilePath)

        with open(absoluteFilePath) as file:
            for line in file.readlines():
                m = re.search(keyword,line)
                if m != None:
                    foundKeyWords.add(m.group('keyword'))
            
for keyword in foundKeyWords:
    print keyword