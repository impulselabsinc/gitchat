# Gitchat
## Small chat app to teach children how to use git

Watches for new and modified files under the 'messages' subdirectory
Any new or modified contents are published to the GUI. This is where
you add or update messages.

You then need to push the changes to github. Similarly you need to
pull messages from Github to see what others have written.

messages take the following format (colons are used as separators) -
```
name:message:formatColor
```

for example, the following message will highlight 'nikhil' in pink, followed by the message 'Elephants are oppressing the cheese curds'
```
nikhil:Elephants are oppressing the cheese curds:pink
```

the following message will display a smiley -
```
nikhil::happy
```
Only the following emotions are supported for now -
- creeper
- poo
- happy
- shrug
- smile

![Image of Gitchat](https://impulselabsinc.github.io/img/gitchat.png)


```
# Requires watchdog
sudo pip install watchdog

# Requires netifaces
sudo pip install netifaces

# Requires python-imaging and python-imaging-tk
sudo apt-get install python-imaging python-imaging-tk -y
```
