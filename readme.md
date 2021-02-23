# Automatic Minecraft Hardcore
=====================
This is a simple tool for running automated Hardcore Minecraft Multiplayer servers.

Whenever someone dies in the game, the server restarts, the old world is deleted, and a new world is generated.

## Installation/Usage
For use with Linux-based Minecraft servers.

Installation:
 - After installing the repo, place your preferred server.jar within the repo.
 - For the first run, use `bash -c "java -Xmx1024M -Xms1024M -jar server.jar nogui &" && python3 automch/mclp.py`
 - After following first-run instructions given by server.jar, use ./start-server.jar
   - If you run into issues here, try `chmod +x ./start-server.jar && chmod +x ./kill-server.jar`
 - Your server is running! 

## **Warning**
As described, once someone dies in your world running with this tool, *that world will be deleted*.

