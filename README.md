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

Watches for new and modified files in the '../gitchat-messages' directory(one level up)
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

To pull new messages and to add messages use the following git commands
```
# pulls latest changes from Github. Always pull before you do anything else so you are working with the latest changes
git pull

# shows you which files have been modified or need to be added to Github
git status

# add a file that you want to save on Github
git add filename.txt

# finalize the change - the comment is required
git commit -m "May the source be with you"

# send the files to Github
git push

```

If someone else made changes before you pushed your changes to Github, you may see a terminal editor window open asking you for a merge comment - you can either type 'Ctrl + X' or ':wq' to exit out of the screen and try pushing your changes again

![Image of Gitchat](https://impulselabsinc.github.io/img/gitchat.png)

![Image of Gitchat Minecraft](https://impulselabsinc.github.io/img/gitchatmc.png)

```
# Requires pillow, watchdog and netifaces
sudo pip install watchdog netifaces pillow

# Requires python-imaging and python-imaging-tk
sudo apt-get install python-imaging python-imaging-tk -y
```
- The lib directory also has a soft link to mcpi. If you do not use Linux or MacOS, you will need to download mcpi to /lib

### Git commands
- You should create your branch before you start working or your changes may be lost
- You cannot make any changes to the 'master' branch
- These commands need to be run from the directory that the code is in
- Open a terminal and go to the directory the code is in
```
cd ~/impulselabs/gitchat
```

- 'git branch' shows you available branches as well as which branch you are on (marked with an asterisk)
```
git branch
```

- 'git branch gitchat-<yourName>' creates a new branch for you to work on. There should be no spaces in the name
```
git branch gitchat-poopsie
```

- 'git checkout <branchName>' will switch you to any branch you want
- You can even switch to a friend's branch to see the code they created
- Be sure to checkout your own branch again so you do not accidentally change your friend's code
```
git checkout gitchat-poopsie
```

- After you create your branch and checkout, you need to push it to Github before you start working on it
- If you do not push your branch to Github, you will not be able to share your changes with others and you may lose your work
```
git push --set-upstream origin gitchat-poopsie
```

- Make sure you pull down any changes before you add any files to git
```
git pull
```

- After you make changes to a file you must add it to git
- You must add it again even if it was added before 
```
git add gitchat.py
git add lib/minecraftFrame.py
```

- After you add all the files you have created or changed, you must commit them
- You have to add a comment in quotes after the '-m' describing the changes 
- you have made or you will not be able to save your work
```
git commit -m 'added a new emoji'
```

- You are now ready to push your changes to github
- you will be prompted for a username and password
- If you do not know the username and password, ask your instructor
- You will be able to see your username but you will not see anything when you type your password
```
git push

```




