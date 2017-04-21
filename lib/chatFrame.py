# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk as ttk
from tkFont import Font
from PIL import Image, ImageTk
from collections import namedtuple

class ChatFrame(ttk.Frame):
    def __init__(self, parent):
        chatFrame = ttk.Frame(parent, width=200, height=100,)
        chatFrame.pack()

        # Create and position horizontal and vertical scroll bars
        xscrollbar = tk.Scrollbar(chatFrame, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        yscrollbar = tk.Scrollbar(chatFrame)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create text widget for the chat
        self.text = tk.Text(chatFrame, width=200, height=100, wrap=tk.NONE,
                            xscrollcommand=xscrollbar.set,
                            yscrollcommand=yscrollbar.set)

        # Increase the font size for the text widget
        myFont = Font(family="Helvetica", size=14)
        self.text.configure(font=myFont)
        self.text.pack()

        # Add the frame to the notebook
        parent.add(chatFrame, text="Chat")

        # Set all the color tags
        self.set_tags(self.text)

        # Position text widget and add scrolling
        self.text.pack(fill="both", expand=True)
        xscrollbar.config(command=self.text.xview)
        yscrollbar.config(command=self.text.yview)

        # Load emoji
        self.initImages()


    def set_tags(self, parent):
        # Set up loads of colored tags so the kids can have some fun
        # Red and black are restricted tags used for system messages
        # Secret will hide the text unless a resourceful soul figures out how to hack it
        parent.tag_config("secret", background="white", foreground="white")
        parent.tag_config("white", background="white", foreground="black")
        parent.tag_config("black", background="black", foreground="white")
        parent.tag_config("red", background="red", foreground="white")
        parent.tag_config("yellow", background="yellow", foreground="black")
        parent.tag_config("green", background="green", foreground="red")
        parent.tag_config("blue", background="blue", foreground="yellow")
        parent.tag_config("orange", background="orange", foreground="black")
        parent.tag_config("pink", background="pink", foreground="blue")
        parent.tag_config("cyan", background="cyan", foreground="black")
        parent.tag_config("brown", background="brown", foreground="yellow")
        parent.tag_config("aquamarine", background="aquamarine", foreground="black")
        parent.tag_config("purple", background="purple", foreground="cyan")
        parent.tag_config("honeydew", background="honeydew", foreground="brown")
        parent.tag_config("rainbow_violet", background="#9400D3", foreground="white")
        parent.tag_config("rainbow_indigo", background="#4B0082", foreground="pink")
        parent.tag_config("rainbow_blue", background="#0000FF", foreground="yellow")
        parent.tag_config("rainbow_green", background="#00FF00", foreground="blue")
        parent.tag_config("rainbow_yellow", background="#FFFF00", foreground="brown")
        parent.tag_config("rainbow_orange", background="#FF7F00", foreground="white")
        parent.tag_config("rainbow_red", background="#FF0000", foreground="yellow")

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

    def chat_insert(self, line, lineNumber):
        payload = self.clean_payload(line)

        # Array to cycle through for the 'rainbow' tag below
        rainbowColors = []
        rainbowColors.append("rainbow_violet")
        rainbowColors.append("rainbow_indigo")
        rainbowColors.append("rainbow_blue")
        rainbowColors.append("rainbow_green")
        rainbowColors.append("rainbow_yellow")
        rainbowColors.append("rainbow_orange")
        rainbowColors.append("rainbow_red")

        # Make the text widget writable again
        self.text.config(state=tk.NORMAL)

        # Most tags will  highlight just the name in the desired color
        if payload.tag in self.allowed_tag_colors:
            lineNumber = lineNumber + 1
            self.text.insert("end", payload.name + " > " + payload.message + "\n")
            self.text.tag_add(payload.tag, str(lineNumber) + ".0", str(lineNumber) + "." + str(len(payload.name)))

        # Rainbow tags will color each character in the message a different color                                          
        elif payload.tag == "rainbow":
            lineNumber = lineNumber + 1
            self.text.insert("end", payload.name + " > " + payload.message + "\n")
            nameLen = len(payload.name)
            self.text.tag_add("white", str(lineNumber) + ".0", str(lineNumber) + "." + str(nameLen))
            idx = 0
            for character in range(nameLen + 3, len(payload.message) + nameLen, 5):
                mycolor = rainbowColors[idx]
                idx = (idx + 1) % len(rainbowColors)                               
                self.text.tag_add(mycolor, str(lineNumber) + "." + str(character), str(lineNumber) + "." + str(character + 7))

        # Secret will hide the contents of a message until a resourceful hacker can figure out how to hack it
        elif payload.tag == "secret":
            lineNumber = lineNumber + 1
            self.text.insert("end", payload.name + " > " + payload.message + " <---***Secret Message***" + "\n")
            nameLen = len(payload.name)
            self.text.tag_add("white", str(lineNumber) + ".0", str(lineNumber) + "." + str(nameLen))
            self.text.tag_add("secret", str(lineNumber) + "." + str(nameLen + 3), str(lineNumber) + "." + str(len(myMsg) + nameLen + 3))
            self.text.tag_add("red", str(lineNumber) + "." + str(len(payload.message) + nameLen + 3 + 1), str(lineNumber) + "." + str(len(payload.message) + nameLen + 3 + 24))

        # Papaya has a 2-tone (orange/yellow) color combo for the name and the message
        elif payload.tag == "papaya":
            lineNumber = lineNumber + 1
            self.text.insert("end", payload.name + " > " + payload.message + "\n")
            nameLen = len(payload.name)
            self.text.tag_add("orange", str(lineNumber) + ".0", str(lineNumber) + "." + str(nameLen))
            self.text.tag_add("yellow", str(lineNumber) + "." + str(nameLen + 3), str(lineNumber) + "." + str(len(payload.message) + nameLen + 3))

        # Pastel has a 2-tone (pink/aquamarine) color combo for the name and the message
        elif payload.tag == "pastel":
            lineNumber = lineNumber + 1
            self.text.insert("end", payload.name + " > " + payload.message + "\n")
            nameLen = len(payload.name)
            self.text.tag_add("pink", str(lineNumber) + ".0", str(lineNumber) + "." + str(nameLen))
            self.text.tag_add("aquamarine", str(lineNumber) + "." + str(nameLen + 3), str(lineNumber) + "." + str(len(payload.message) + nameLen + 3))

        # Text emojis do not get color tags and the message payload is ignored. Just the emoji is displayed
        elif payload.tag in self.textemoji:
            lineNumber = lineNumber + 3
            self.text.insert("end", "\n" + payload.name + " > " + self.textemoji[payload.tag] + "\n\n")

        # Picture emojis do not get color tags and the message payload is ignored. Just the emoji is displayed
        elif payload.tag in self.emojicons:
            lineNumber = lineNumber + 3
            self.text.insert("end", "\n" + payload.name + " > ")
            self.text.image_create(tk.END,image=self.emojicons[payload.tag])
            self.text.insert("end", "\n\n")

        # Everything else is best-effort
        else:
            lineNumber = lineNumber + 1
            self.text.insert("end", payload.name + " > " + payload.message + "\n")
            self.text.tag_add("white", str(lineNumber) + ".0", str(lineNumber) + "." + str(len(payload.name)))

        # Lock the text widget again
        self.text.config(state=tk.DISABLED)

        # Autoscroll to the latest messages
        self.text.see(tk.END)

        # Return lineNumber so we don't lose track of the running count
        return lineNumber
        


    def clean_payload(self, line):
        payload = namedtuple('payload',['name','message','tag'])

        myName = ''
        myMsg = ''
        myTag = ''

        # First we tokenize on the colon (:)
        # We try to make an educated guess if we don't get back 3 parts
        # Missing names get 'poopsie lala' as a substitute
        # Missing tags get 'white' as a substitute
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

        return payload(myName,myMsg,myTag)
        
