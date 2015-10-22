# tools-python
## pingservers.py
Ping specified IPs, send mail when IPs were down.<br />
Ex. <br />
python pingservers.py 192.168.0.1,192.168.0.2 <br/>
## splitfile.py
Split large file to smaller ones, every smaller file contains 100000 lines.<br /><br />
Ex. <br />
python splitfile.py D:\largefile.log<br />
largefile.log will be splitted to<br />
largefile.1.log<br />
largefile.2.log<br />
largefile.3.log<br />
largefile.4.log<br />
largefile.5.log<br />
...etc<br />
## print_previousline_by_keyword.py
Iterate a path to find a keyword.<br />
Print the found line and previous line<br />
Ex. <br />
python print_previousline_by_keyword.py D:\logs\ Exception<br />
