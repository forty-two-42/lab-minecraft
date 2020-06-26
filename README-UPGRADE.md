# Upgrade instructions

Also available on

https://github.com/miharothl/lab-minecraft/blob/master/README-UPGRADE.md

## Login to server
```
ssh app@games.rothl.com
```
## Stop the mincraft in minecraft

Check if game is still running using
```
ps a
```

Look for COMMAND `java -Xmx3G -Xms3G -jar craftbukkit.latest nogui` and get PID, for example `1205`
```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
app       1205 42.2 63.7 5926820 2538784 pts/0 Sl   08:07  11:41 java -Xmx3G -Xms3G -jar craftbukkit-1.15.2.jar nogui
```

Kill the process using
```
kill 1205
```

## Backup the game
Allways increase the number 01, 02, 03, etc.
```
cd /srv/minecraft
tar cpvf backup.rothl.01.tar rothl
```
Get URL of the last version of the game https://getbukkit.org/download/craftbukkit and download the game using curl
```
cd /srv/minecraft/rothl/
wget https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.1.jar
```
Point craftbucket.latest to latest version
```
ls -la
rm craftbukkit.latest
ls -s craftbukkit-1.16.1.jar craftbukkit.latest
```
Start the game and check the logs
```
./start.sh
tail -f minecraft.log
```

# Usefull commands

* `pwd` - print working directory
* `whoami` - to check what is my username


# Important directories

* `/home/app` - home for application user
* `/srv/minecraft` - that's where the mincraft game is stored



