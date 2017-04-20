# -*- coding: utf-8 -*-

"""
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

```
# Requires watchdog
sudo pip install watchdog
```

"""

import sys
import Tkinter as tk
from tkFont import Font
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Queue import Queue
from PIL import Image, ImageTk


class CustomHandler(FileSystemEventHandler):
    # We only care about create and update events
    # This also means that if you use the same file
    # to send messages that everything will be repeated
    # unless uyou first delete the previous messages
    
    def __init__(self, app):
        FileSystemEventHandler.__init__(self)
        self.app = app

        
    def on_created(self, event):
        if event.is_directory:
            return None
        else:
            app.notify(event)
        
        
    def on_deleted(self, event):
        if event.is_directory:
            return None
        else:
            return None
        
        
    def on_modified(self, event):
        if event.is_directory:
            return None
        else:
            app.notify(event)
        
        
    def on_moved(self, event):
        if event.is_directory:
            return None
        else:
            return None

        

class App(object):
    def __init__(self):
        
        # Set up the fie watcher and path
        # you can also pass it a path from
        # the command line
        path = sys.argv[1] if len(sys.argv) > 1 else "./messages"
        handler = CustomHandler(self)
        self.observer = Observer()
        self.observer.schedule(handler, path, recursive=False)

        # Initialize line numbers so we know where to apply color tags
        self.lineNumber = 0

        # Limited de-duplication by keeping track of last change loaded
        self.previousFile = []

        # Initialize the queue that goes between the filewatcher and the GUI
        self.queue = Queue()

        # Initialize GUI root object
        self.root = tk.Tk()

        # Build the GUI
        self.initMenu()
        self.initUi(path)
        self.initImages()

        # Start watching files
        self.observer.start()

    def initUi(self, path):

        # Create and position horizontal and vertical scroll bars
        self.xscrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.yscrollbar = tk.Scrollbar(self.root)
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create text widget for the chat
        self.text = tk.Text(self.root,wrap=tk.NONE,
                            xscrollcommand=self.xscrollbar.set,
                            yscrollcommand=self.yscrollbar.set)

        # Increase the font size for the text widget
        myFont = Font(family="Helvetica", size=14)
        self.text.configure(font=myFont)

        # Set up loads of colored tags so the kids can have some fun
        # Red and black are restricted tags used for system messages
        # Secret will hide the text unless a resourceful soul figures out how to hack it
        self.text.tag_config("secret", background="white", foreground="white")
        self.text.tag_config("white", background="white", foreground="black")
        self.text.tag_config("black", background="black", foreground="white")
        self.text.tag_config("red", background="red", foreground="white")
        self.text.tag_config("yellow", background="yellow", foreground="black")
        self.text.tag_config("green", background="green", foreground="red")
        self.text.tag_config("blue", background="blue", foreground="yellow")
        self.text.tag_config("orange", background="orange", foreground="black")
        self.text.tag_config("pink", background="pink", foreground="blue")
        self.text.tag_config("cyan", background="cyan", foreground="black")
        self.text.tag_config("brown", background="brown", foreground="yellow")
        self.text.tag_config("aquamarine", background="aquamarine", foreground="black")
        self.text.tag_config("purple", background="purple", foreground="cyan")
        self.text.tag_config("honeydew", background="honeydew", foreground="brown")
        self.text.tag_config("rainbow_violet", background="#9400D3", foreground="white")
        self.text.tag_config("rainbow_indigo", background="#4B0082", foreground="pink")
        self.text.tag_config("rainbow_blue", background="#0000FF", foreground="yellow")
        self.text.tag_config("rainbow_green", background="#00FF00", foreground="blue")
        self.text.tag_config("rainbow_yellow", background="#FFFF00", foreground="brown")
        self.text.tag_config("rainbow_orange", background="#FF7F00", foreground="white")
        self.text.tag_config("rainbow_red", background="#FF0000", foreground="yellow")

        # Somewhat unnecessary dictionary so we can test for tags more easily
        # Any new color tags need to be added here
        self.allowed_tag_colors = {}
        self.allowed_tag_colors['white'] = 'white'
        self.allowed_tag_colors['yellow'] = 'yellow'
        self.allowed_tag_colors['green'] = 'green'
        self.allowed_tag_colors['blue'] = 'blue'
        self.allowed_tag_colors['orange'] = 'orange'
        self.allowed_tag_colors['pink'] = 'pink'
        self.allowed_tag_colors['cyan'] = 'cyan'
        self.allowed_tag_colors['brown'] = 'brown'
        self.allowed_tag_colors['aquamarine'] = 'aquamarine'
        self.allowed_tag_colors['purple'] = 'purple'
        self.allowed_tag_colors['honeydew'] = 'honeydew'
        self.allowed_tag_colors['rainbow_violet'] = 'rainbow_violet'
        self.allowed_tag_colors['rainbow_indigo'] = 'rainbow_indigo'
        self.allowed_tag_colors['rainbow_blue'] = 'rainbow_blue'
        self.allowed_tag_colors['rainbow_green'] = 'rainbow_green'
        self.allowed_tag_colors['rainbow_yellow'] = 'rainbow_yellow'
        self.allowed_tag_colors['rainbow_orange'] = 'rainbow_orange'
        self.allowed_tag_colors['rainbow_red'] = 'rainbow_red'

        # Position text widget and add scrolling
        self.text.pack(fill="both", expand=True)
        self.xscrollbar.config(command=self.text.xview)
        self.yscrollbar.config(command=self.text.yview)

        # Welcome message for Gitchat
        self.welcomeMsg = " " * 50 + "Welcome to Gitchat" + " " * 50
        self.lineNumber = self.lineNumber + 1
        self.text.insert(tk.INSERT, self.welcomeMsg + "\n")
        self.text.tag_add("red", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(self.welcomeMsg)))

        # Watched directory is displayed in GUI
        self.lineNumber = self.lineNumber + 1
        self.text.insert("end", "Watching %s...\n" % path)

        # Text widget is disabled so users cannot type into it and mess up the numbering for tags
        self.text.config(state=tk.DISABLED)

        # Have the GUI listen for shutdown events
        self.root.bind("<Destroy>", self.shutdown)

        # Subscribe the GUI to file watcher events
        self.root.bind("<<WatchdogEvent>>", self.handle_watchdog_event)

    def initImages(self):

        # Dictionary for image emojis
        self.emojicons = {}

        # Set the base size to 32 pixels
        # Calculate and proportionately
        # reduce image size

        # creeper emoji
        basewidth = 32
        buf = Image.open('./emojis/creeper.gif')
        wpercent = (basewidth/float(buf.size[0]))
        hsize = int((float(buf.size[1])*float(wpercent)))
        buf = buf.resize((basewidth,hsize), Image.ANTIALIAS)
        self.emojicons['creeper'] = ImageTk.PhotoImage(buf)

        # poo emoji
        basewidth = 32
        buf = Image.open('./emojis/poo.gif')
        wpercent = (basewidth/float(buf.size[0]))
        hsize = int((float(buf.size[1])*float(wpercent)))
        buf = buf.resize((basewidth,hsize), Image.ANTIALIAS)
        self.emojicons['poo'] = ImageTk.PhotoImage(buf)

        # happy emoji
        basewidth = 32
        buf = Image.open('./emojis/happy.gif')
        wpercent = (basewidth/float(buf.size[0]))
        hsize = int((float(buf.size[1])*float(wpercent)))
        buf = buf.resize((basewidth,hsize), Image.ANTIALIAS)
        self.emojicons['happy'] = ImageTk.PhotoImage(buf)


        # Dictionary for text emojis
        self.textemoji = {}

        # shrug emoji
        self.textemoji['shrug'] = """¯\_(ツ)_/¯"""

        # smile emoji
        self.textemoji['smile'] = """【ツ】"""

        
    def initMenu(self):
        # Create the Menu items for the app

        # Set window title
        self.root.title("Gitchat")    

        # Create menu root
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        fileMenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=fileMenu)

        # File -> Exit menu item
        fileMenu.add_command(label="Exit", command=self.onExit) 
        
        # Help menu
        helpmenu = tk.Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Help -> I want to send a message menu item
        helpmenu.add_command(label="I want to send a message", command=self.help_send)

        # Help -> I want to receive a message menu item
        helpmenu.add_command(label="I want to receive a message", command=self.help_receive)

        # Help -> About menu item
        helpmenu.add_command(label="About...", command=self.About)                              

        
    def handle_watchdog_event(self, event):
        # The heavy-lifting for the app
        # All events are handled here

        # Pick up watchdog events from the queue
        watchdog_event = self.queue.get()

        # Open the file that generated the event
        with open(watchdog_event.src_path) as f:
            
            # Read the entire file - probably
            lines = f.readlines()

            # Close the file after reaing it
            f.close()

            # Make the text widget writable again
            # Should really move this further down
            self.text.config(state=tk.NORMAL)

            # Simple deduping test to account for
            # new files generating both a create
            # event and an update event
            if self.previousFile == lines:
                return None
            else:

                # Store the current file for the next compare
                self.previousFile = lines

                # Process each line
                # First we tokenize on the colon (:)
                # We try to make an educated guess if we don't get back 3 parts
                # Missing names get 'poopsie lala' as a substitute
                # Missing tags get 'white' as a substitute
                for line in lines:
                    parts = line.split(":")
                    if len(parts) == 3:
                        myName = parts[0].strip()
                        myMsg = parts[1].strip()
                        myTag = parts[2].strip().lower()
                    elif len(parts) == 2:
                        myName = parts[0].strip()
                        myMsg = parts[1].strip()
                        myTag = "white"
                    elif len(parts) == 1:
                        myName = "poopsie lala"
                        myMsg = parts[0].strip()
                        myTag = "white"
                    else:
                        myName = "poopsie lala"
                        myMsg = line.strip()
                        myTag = "white"

                    # Array to cycle through for the 'rainbow' tag below
                    rainbowColors = []
                    rainbowColors.append("rainbow_violet")
                    rainbowColors.append("rainbow_indigo")
                    rainbowColors.append("rainbow_blue")
                    rainbowColors.append("rainbow_green")
                    rainbowColors.append("rainbow_yellow")
                    rainbowColors.append("rainbow_orange")
                    rainbowColors.append("rainbow_red")
                    
                    # Most tags will  highlight just the name in the desired color
                    if myTag in self.allowed_tag_colors:
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        self.text.tag_add(myTag, str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(myName)))

                    # Rainbow tags will color each character in the message a different color                                          
                    elif myTag == "rainbow":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("white", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        idx = 0
                        for character in range(nameLen + 3, len(myMsg) + nameLen, 5):
                            mycolor = rainbowColors[idx]
                            idx = (idx + 1) % len(rainbowColors)                               
                            self.text.tag_add(mycolor, str(self.lineNumber) + "." + str(character), str(self.lineNumber) + "." + str(character + 7))

                    # Secret will hide the contents of a message until a resourceful hacker can figure out how to hack it
                    elif myTag == "secret":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + " <---***Secret Message***" + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("white", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        self.text.tag_add("secret", str(self.lineNumber) + "." + str(nameLen + 3), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3))
                        self.text.tag_add("red", str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3 + 1), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3 + 24))

                    # Papaya has a 2-tone (orange/yellow) color combo for the name and the message
                    elif myTag == "papaya":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("orange", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        self.text.tag_add("yellow", str(self.lineNumber) + "." + str(nameLen + 3), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3))

                    # Pastel has a 2-tone (pink/aquamarine) color combo for the name and the message
                    elif myTag == "pastel":
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        nameLen = len(myName)
                        self.text.tag_add("pink", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(nameLen))
                        self.text.tag_add("aquamarine", str(self.lineNumber) + "." + str(nameLen + 3), str(self.lineNumber) + "." + str(len(myMsg) + nameLen + 3))

                    # Text emojis do not get color tags and the message payload is ignored. Just the emoji is displayed
                    elif myTag in self.textemoji:
                        self.lineNumber = self.lineNumber + 3
                        self.text.insert("end", "\n" + myName + " > " + self.textemoji[myTag] + "\n\n")

                    # Picture emojis do not get color tags and the message payload is ignored. Just the emoji is displayed
                    elif myTag in self.emojicons:
                        self.lineNumber = self.lineNumber + 3
                        self.text.insert("end", "\n" + myName + " > ")
                        self.text.image_create(tk.END,image=self.emojicons[myTag])
                        self.text.insert("end", "\n\n")

                    # Everything else is best-effort
                    else:
                        self.lineNumber = self.lineNumber + 1
                        self.text.insert("end", myName + " > " + myMsg + "\n")
                        self.text.tag_add("white", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(myName)))
                    self.text.see(tk.END)
                    
        self.text.config(state=tk.DISABLED)


    def shutdown(self, event):
        # Shuts down filewatcher 
        self.observer.stop()

    def mainloop(self):
        # Start the GUI loop
        self.root.mainloop()

    def notify(self, event):
        # Used by the file watcher to put events on the queue and to notify the GUI
        self.queue.put(event)
        self.root.event_generate("<<WatchdogEvent>>", when="tail")

    def onExit(self):
        # Clean exit
        self.observer.stop()
        self.root.destroy()

    def About(self):
        # Help menu item about the app
        about_message = "\nGitchat v0.1\n\n"
        about_message = about_message + "Gitchat was designed to help children learn to use Github\n\n"
        about_message = about_message + "https://github.com/impulselabsinc\n"
        
        self.top = tk.Toplevel()
        self.top.geometry("300x200")
        self.top.title("About Gitchat")
        msg = tk.Message(self.top, text=about_message, width=250, justify='center')
        msg.pack()
        self.button = tk.Button(self.top, text="Go away, silly message!", command=self.top.destroy)
        self.button.pack()

    def help_send(self):
        # Help menu item to help send messages
        send_message = "\n"
        send_message = send_message + "1.  Launch Python 2 (Raspberry Pi menu -> Programming -> Python 2)\n"
        send_message = send_message + "2.  Create a new file (File -> New)\n"
        send_message = send_message + "3.  Write your name and a message separated by a colon (:). For example -\n"
        send_message = send_message + "     sara:I like to stare rudely at spiders\n"
        send_message = send_message + "    (In America, you can type a colon (:) by keeping the 'Shift'\n"
        send_message = send_message + "    key pressed and pressing the key to the right of the 'L' key)\n"
        send_message = send_message + "4.  Save the file with your name and then 'chat.py' after it\n"
        send_message = send_message + "    So Sara's file would be called 'sarachat.py\n"
        send_message = send_message + "5.  Open a terminal window and type in the following commands\n"
        send_message = send_message + "     cd impulselabs\n"
        send_message = send_message + "     cd students\n"
        send_message = send_message + "     cd gitchat\n"
        send_message = send_message + "     cd messages\n"
        send_message = send_message + "     git pull\n"
        send_message = send_message + "     git add sarachat.py\n"
        send_message = send_message + '     git commit -m "I am sending a message"\n'
        send_message = send_message + "     git push\n"
        send_message = send_message + "6.  You will be asked for a username - type in the username and hit 'Enter'\n"
        send_message = send_message + "    (if you do not know your username ask one of your teachers)\n"
        send_message = send_message + "7.  Next, will be asked for a password - type in the password and hit 'Enter'\n"
        send_message = send_message + "    (if you do not know your password ask one of your teachers)\n"
        send_message = send_message + "    (your password is secret so you will not see anything on the screen when you type it)\n"

        self.top = tk.Toplevel()
        self.top.geometry("600x450")
        self.top.title("How to send a message")
        msg = tk.Message(self.top, text=send_message, width=580, justify='left')
        msg.pack()
        self.button = tk.Button(self.top, text="Go away, silly message!", command=self.top.destroy)
        self.button.pack()
        
    def help_receive(self):
        # Help menu item to help receive messages
        print "nothing to see here"
        receive_message = "\n"
        receive_message = receive_message + "1.  Open a terminal window and type in the following commands\n"
        receive_message = receive_message + "     cd impulselabs\n"
        receive_message = receive_message + "     cd students\n"
        receive_message = receive_message + "     cd gitchat\n"
        receive_message = receive_message + "     cd messages\n"
        receive_message = receive_message + "     git pull\n"

        self.top = tk.Toplevel()
        self.top.geometry("600x200")
        self.top.title("How to send a message")
        msg = tk.Message(self.top, text=receive_message, width=580, justify='left')
        msg.pack()
        self.button = tk.Button(self.top, text="Go away, silly message!", command=self.top.destroy)
        self.button.pack()

# App main
app = App()
app.mainloop()
