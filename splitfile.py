import sys
import itertools

def writeFile(lines, outputFile):
    with open(outputFile, 'w') as file:
        file.writelines(lines);


if len(sys.argv) == 1:
    sys.exit("please specify filepath")
    
filepath = sys.argv[1];
print "split file:", filepath;    

fileCnt = 0;
with open(filepath) as file:
    readLines = [];
    with open(filepath):
        readLineCnt = 0;
        for line in file.readlines():
            readLines.append(line);
            if ( len(readLines) >= 100000 ):
                fileCnt += 1;
                suffix = filepath[filepath.rindex('.')+1: len(filepath)];
                prefix = filepath[0: filepath.rindex('.')];
                writeFile(readLines, prefix + "." + str(fileCnt) + "." + suffix);
                del readLines[:];
            
                
