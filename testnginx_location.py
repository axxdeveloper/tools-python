import httplib
import sys

if len(sys.argv) == 1:
    sys.exit("Ex: python testnginx_location.py /test");
    
location = str(sys.argv[1])    
conn = httplib.HTTPConnection("localhost",80)
print "location:", location
conn.request("GET",location)
r1 = conn.getresponse()
print r1.read()
conn.close()