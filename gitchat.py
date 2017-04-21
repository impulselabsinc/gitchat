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
import ttk as ttk
import lib.menu as menu
import lib.chatFrame as chatframe
import lib.minecraftFrame as minecraftframe
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Queue import Queue


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
        self.path = sys.argv[1] if len(sys.argv) > 1 else "./messages"
        handler = CustomHandler(self)
        self.observer = Observer()
        self.observer.schedule(handler, self.path, recursive=False)

        # Initialize line numbers so we know where to apply color tags
        self.lineNumber = 0

        # Limited de-duplication by keeping track of last change loaded
        self.previousFile = []

        # Initialize the queue that goes between the filewatcher and the GUI
        self.queue = Queue()

        # Initialize GUI root object and set the window size (W x H)
        self.root = tk.Tk()
        self.root.geometry('600x400')

        # Build the GUI
        self.root.title("Gitchat") 
        self.menu = menu.Menu(self.root)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()
        self.chtframe = chatframe.ChatFrame(self.notebook)
        self.initChatUi()
        self.mcframe = minecraftframe.MinecraftFrame(self.notebook)

        # Start watching files
        self.observer.start()

        
    def initChatUi(self):

        # Welcome message for Gitchat
        welcomeMsg = " " * 50 + "Welcome to Gitchat" + " " * 50
        self.lineNumber = self.lineNumber + 1

        self.chtframe.text.insert(tk.INSERT, welcomeMsg + "\n")
        self.chtframe.text.tag_add("red", str(self.lineNumber) + ".0", str(self.lineNumber) + "." + str(len(welcomeMsg)))

        # Watched directory is displayed in GUI
        self.lineNumber = self.lineNumber + 1
        self.chtframe.text.insert("end", "Watching %s...\n" % self.path)

        # Text widget is disabled so users cannot type into it and mess up the numbering for tags
        self.chtframe.text.config(state=tk.DISABLED)

        # Have the GUI listen for shutdown events
        self.root.bind("<Destroy>", self.shutdown)

        # Subscribe the GUI to file watcher events
        self.root.bind("<<WatchdogEvent>>", self.handle_watchdog_event)

        
            
    def handle_watchdog_event(self, event):

        # Pick up watchdog events from the queue
        watchdog_event = self.queue.get()

        # Open the file that generated the event
        with open(watchdog_event.src_path) as f:
            
            # Read the entire file - probably
            lines = f.readlines()

            # Close the file after reaing it
            f.close()

            # Simple deduping test to account for
            # new files generating both a create
            # event and an update event
            if self.previousFile == lines:
                return None
            else:
                # Store the current file for the next compare
                self.previousFile = lines

                # Process each line
                # And keep track of the running total of lines for accurate tagging
                for line in lines:
                    tmpLineNumber = self.chtframe.chat_insert(line, self.lineNumber)
                    self.lineNumber = self.lineNumber + (tmpLineNumber - self.lineNumber)



    def shutdown(self, event):
        # Shuts down filewatcher
        print 'shutting down observer...'
        self.observer.stop()

    def mainloop(self):
        # Start the GUI loop
        self.root.mainloop()

    def notify(self, event):
        # Used by the file watcher to put events on the queue and to notify the GUI
        self.queue.put(event)
        self.root.event_generate("<<WatchdogEvent>>", when="tail")

# App main
app = App()
app.mainloop()
