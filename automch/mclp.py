#!/usr/bin python3
import re, datetime, operator, os, time
from deathcauses import causes as deathcauseslist

deathsListRegString = '('+'|'.join(deathcauseslist)+')'
deathregex = re.compile(deathsListRegString)
# Read log file as it's being written. Thanks stackoverflow
def follow(thefile):
    thefile.seek(0,2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        yield line

path = open('logs/latest.log')
while(True):
    for line in follow(path):
        if deathregex.match(line):
            restart_server()
            break
    time.sleep(5)

def restart_server():
    # os.system(r"kill -9 ps aux | grep -i java | grep -v grep | awk '{print $2}'")
    # os.system(r"rm -r ./world")
    # os.system(r"rm -r ./logs")
    # os.system(r"java -Xmx1024M -Xms1024M -jar server.jar nogui")
    print("MUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\n")

