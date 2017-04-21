# -*- coding: utf-8 -*-
import Tkinter as tk

class Menu():
    def __init__(self, parent):
        # Create the Menu items for the app   

        # Create menu root
        menubar = tk.Menu(parent)
        parent.config(menu=menubar)

        # File menu
        fileMenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=fileMenu)

        # File -> Exit menu item
        fileMenu.add_command(label="Exit", command= lambda: self.onExit(parent)) 
        
        # Help menu
        helpmenu = tk.Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Help -> I want to send a message menu item
        helpmenu.add_command(label="I want to send a message", command=self.help_send)

        # Help -> I want to receive a message menu item
        helpmenu.add_command(label="I want to receive a message", command=self.help_receive)

        # Help -> About menu item
        helpmenu.add_command(label="About...", command=self.About)

    def onExit(self, parent):
        # Clean exit
        parent.destroy()

    def About(self):
        # Help menu item about the app
        about_message = "\nGitchat v0.1\n\n"
        about_message = about_message + "Gitchat was designed to help children learn to use Github\n\n"
        about_message = about_message + "https://github.com/impulselabsinc\n"
        
        top = tk.Toplevel()
        top.geometry("300x200")
        top.title("About Gitchat")
        msg = tk.Message(top, text=about_message, width=250, justify='center')
        msg.pack()
        button = tk.Button(top, text="Go away, silly message!", command=top.destroy)
        button.pack()

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

        top = tk.Toplevel()
        top.geometry("600x450")
        top.title("How to send a message")
        msg = tk.Message(top, text=send_message, width=580, justify='left')
        msg.pack()
        button = tk.Button(top, text="Go away, silly message!", command=top.destroy)
        button.pack()
        
    def help_receive(self):
        # Help menu item to help receive messages
        receive_message = "\n"
        receive_message = receive_message + "1.  Open a terminal window and type in the following commands\n"
        receive_message = receive_message + "     cd impulselabs\n"
        receive_message = receive_message + "     cd students\n"
        receive_message = receive_message + "     cd gitchat\n"
        receive_message = receive_message + "     cd messages\n"
        receive_message = receive_message + "     git pull\n"

        top = tk.Toplevel()
        top.geometry("600x200")
        top.title("How to send a message")
        msg = tk.Message(top, text=receive_message, width=580, justify='left')
        msg.pack()
        button = tk.Button(top, text="Go away, silly message!", command=top.destroy)
        button.pack()
