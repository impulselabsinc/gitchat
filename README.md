# students

## Using the Terminal
You can launch the terminal from the Raspberry Pi menu on the top left and going into 'Accessories'

Here are a list of useful commands that you can use within the terminal(_Linux commands are always all lower case_)
```sh
# You can see who you are logged in as 
whoami

# The directory you are currently in is called your 'working directory'. The 'print working directory' shows you where you are.
# 'Directory' is another word for 'folder'
pwd

# To list the contents of your working directory
ls

# To list the contents of your working directory in long format use the following command
# Any line that begins with a 'd' is a directory
# Any line that begins with a '-' is a file
# Any line that begins with a 'l' is a link to another file or directory
ls -l

# To list hidden files or directories in your working directory
# Hidden files and folders begin with a dot '.' in front of their names
ls -al

# Every directory always has at least 2 hidden directories
# A single dot '.' is the reference to the directory itself
# Two dots '..' represent the directory that is one level up
# So if I am in this directory - /buttons/blue/ and I do an 'ls -al'
# '.' will refer to the directory called 'blue' 
# '..' will refer to the directory called 'buttons'
# A directory path is the name of all the directories and sub-directories separated by a forward slash '/'
# All directory paths always begin with a forward slash '/'
# This is the starting directory on Linux computers and is also called the 'root' directory
# There are no directories above the root directory

# To list files and directories in the root directory, use 
ls -al /

# To list the files and directories in a specific folder add the name of the directory at the end of the list command 
ls -al /buttons/blue/

# To change your working directory use the change directory command
# If I want to change to the root directory I can use 
cd /

# If I want to change to any directory add the name of that directory to the end of the cd command
cd /buttons/red/

# You can also change to a directory one level up by using
cd ..

# Two levels up
cd ../..

# And so on
cd ../../..

# To copy a file use the copy command
cp redButton.py redButtonCopy.py

# To copy a file to a different directory 
# These commands will create copies so you will have the same file in 2 locations
cp /buttons/blue/redButton.py /buttons/red/

# To move a file use the move command
# The move command removes the file from the original location 
mv /buttons/blue/redButton.py /buttons/red/

# You can also use the move command to rename a file or directory 
mv redFile.py betterRedFile.py

# You can move and rename a file at the same time
mv /buttons/blue/redButton.py /buttons/red/newRedButton.py

# To delete a file use the remove command
rm myBadFile.py

# To delete a directory you can use the remove command with -r
rm -r folderName
```

## Using Git 

Change into the folder where all your files are stored
```sh
cd ~/impulselabs/students/2017/coop/
cd ~/impulselabs/students/2017/ps11/
```

Pull down the latest changes. 
_Always do this before you do anything else_
```sh
git pull
```

Add files that you have created or changed to github.
_Adding a dot (.) will add all the files in that directory to github_
```sh
git add /path/to/file.py
git add /path/to/all/files/in/folder/.
```

Commit your changes to git
```sh
git commit -m "first commit or some other reason"
```

Push your changes to github
enter the username and password you were given
```sh
git push
```

Check the status of all your files
This will show you which files have been added but not pushed and files that have not yet been committed
```sh
git status
```

This is what I would do to create a directory calld toot where I can also save code Minecraft
```sh
cd ~/impulselabsinc/students/2017/ps11/
git pull
mkdir toot
cd toot
ln -s ../../../mcpi mcpi
git add .
git commit -m "created a new folder calld toot"
git push

```

This is what I would do to push a file called myPythonFile.py up to Github
```sh
cd ~/impulselabsinc/students/2017/ps11/toot/
git add myPythonFile.py
git commit -m "added my python file that does something cool"
git push

```

If you experience the following error, it is because there is a missing name configuration
```sh
fatal: empty ident name (for <pi@raspberrypi.(none)>) not allowed
```

You can fix this error by using the following command to add a name
```sh
git config user.name "imp2"
```

If you experience the following error, it is because there is a missing e-mail configuration
```sh
fatal: unable to auto-detect email address (got 'pi@raspberrypi.(none)')
```

You can fix this error by using the following command to add an e-mail address
```sh
git config user.email "imp2@impulselabs.io"
```
