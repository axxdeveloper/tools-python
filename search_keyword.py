import os
import sys
import glob
import re
import itertools
import tempfile

if len(sys.argv) != 4:
    sys.exit('please specify filepath and search keyword. Ex. python search_keyword.py D:\logs\ \"BasePlayValidateFilter.* clientJID=(?P<keyword1>.+)/.+\" \"play\\. .+clientJID:(?P<keyword2>.+)/.+\"')
    
filepath = sys.argv[1];
keyword1 = sys.argv[2]
keyword2 = sys.argv[3]
print "search file:", filepath
print 'keyword1:', keyword1;     
print 'keyword2:', keyword2;
 
keyword1file = tempfile.NamedTemporaryFile(delete=False)
for subdir, dirs, filenames in os.walk(filepath):
    for filename in filenames:
        absoluteFilePath = os.path.join(subdir, filename)
        print('process:' + absoluteFilePath)

        previousLine = ''
        with open(absoluteFilePath) as file:
            for line in file:
                m = re.search(keyword1,line)
                if m != None:
                    print(previousLine),
                    print(line),
                    keyword1file.write(m.group('keyword1') + '\n')
                previousLine = line
print keyword1file.name
keyword1file.flush()
    
for subdir, dirs, filenames in os.walk(filepath):
    for filename in filenames:
        absoluteFilePath = os.path.join(subdir, filename)
        print('process:' + absoluteFilePath)
        with open(absoluteFilePath) as file:
            for line in file:   
                m = re.search(keyword2,line)
                if m == None:
                    continue;
                keyword1file.seek(0,0)
                for keyword1 in keyword1file:
                    if keyword1.strip() == m.group('keyword2').strip():
                        print(line),
    
keyword1file.close()

