# Gitchat
## Hackable chat app to teach children how to use git and program Minecraft

This app allows students to send messages to each other via git push and git pull.

This app has two tabs called 'chat' and 'minecraft'. Students can change the behaviour of both tabs through code in a variety of ways - 
- change the layout
- add tags that allow the text to be formatted differently 
- add their own emojis
- add minecraft controls
- change the layout of the GUI

This app is written in Python and uses Tkinter to build the GUI. 

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

![Image of Gitchat Minecraft](https://impulselabsinc.github.io/img/gitchatmc.png)

```
# Requires watchdog
sudo pip install watchdog

# Requires netifaces
sudo pip install netifaces

# Requires python-imaging and python-imaging-tk
sudo apt-get install python-imaging python-imaging-tk -y
```
