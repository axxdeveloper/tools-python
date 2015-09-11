import sys
import itertools

def writeFile(lines, outputFile):
    print 'writeFile:', outputFile
    with open(outputFile, 'w') as file:
        file.writelines(lines);

def getOutputFilename(origFileNamem, fileCnt):
    suffix = filepath[filepath.rindex('.')+1: len(filepath)];
    prefix = filepath[0: filepath.rindex('.')];
    return prefix + "." + str(fileCnt) + "." + suffix
    
if len(sys.argv) == 1:
    sys.exit("please specify filepath")
    
filepath = sys.argv[1];
print "split file:", filepath;    

fileCnt = 0;
with open(filepath) as file:
    readLines = [];
    with open(filepath):
        readLineCnt = 0;
        for line in file:
            readLines.append(line);
            if ( len(readLines) >= 100000 ):
                suffix = filepath[filepath.rindex('.')+1: len(filepath)];
                prefix = filepath[0: filepath.rindex('.')];
                writeFile(readLines, getOutputFilename(filepath, fileCnt));
                fileCnt += 1;
                del readLines[:];
    writeFile(readLines, getOutputFilename(filepath, fileCnt));
    del readLines[:];
            
                
