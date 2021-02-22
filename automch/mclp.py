#!/usr/bin python3
import re, datetime, operator, os, time
from deathcauses import causes as deathcauseslist

def restart_server():
    print("Player death detected. Annihilating server.")
    os.system(r"kill -9 $(ps aux | grep -i java | grep -v grep | awk '{print $2}')")
    os.system(r"rm -r ./world")
    os.system(r"rm -r ./logs")
    os.system(r"java -Xmx1024M -Xms1024M -jar server.jar nogui &")
    # print("MUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\nMUCH DEAD VERY WOW\n")
    time.sleep(60)

deathsListRegString = r'^\[([0-2][0-9]):([0-9]{2}):([0-9]{2})\] \[Server thread/INFO\]: ('+'|'.join(deathcauseslist)+')'
deathregex = re.compile(deathsListRegString)
# Read log file as it's being written. Thanks stackoverflow
position = 0
def follow(thefile, position):
    thefile.seek(position) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        yield line

while(True):
    path = open('./logs/latest.log')
    for line in follow(path, position):
        # print(line)
        if deathregex.search(line):
            restart_server()
            break
    time.sleep(.1)
