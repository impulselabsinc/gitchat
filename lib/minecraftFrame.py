# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk as ttk
from tkFont import Font
from collections import namedtuple
import mcpi.minecraft as minecraft 
import mcpi.block as block

class MinecraftFrame(ttk.Frame):
    def __init__(self, parent):
        mcFrame = ttk.Frame(parent, width=200, height=100,)
        mcFrame.pack()

        # Add the frame to the notebook
        parent.add(mcFrame, text="Minecraft")

        #Status bar
        self.statusbar = StatusBar(mcFrame)
        self.statusbar.grid(row = 1, column = 4, padx = 5, pady = 5)
        self.statusbar.set('%s', 'Ready')

        # Labels
        # IP address
        lblIpAddress = tk.Label(mcFrame, text="IP Address: ")
        lblIpAddress.grid(row = 1, column = 1, padx = 5, pady = 5)

        # Sender name
        lblSender = tk.Label(mcFrame, text="Your Name: ")
        lblSender.grid(row = 2, column = 1, padx = 5, pady = 5)

        # Sender name
        lblMsg = tk.Label(mcFrame, text="Your Message: ")
        lblMsg.grid(row = 3, column = 1, padx = 5, pady = 5)
        

        # Text fields
        # IP Address
        self.varIpAddr = tk.StringVar()
        fldIpAddr = tk.Entry(mcFrame, textvariable=self.varIpAddr)
        fldIpAddr.insert(tk.END, '127.0.0.1')
        fldIpAddr.grid(row = 1, column = 2)

        # Sender name
        self.varSender = tk.StringVar()
        fldSender = tk.Entry(mcFrame, textvariable=self.varSender)
        fldSender.insert(tk.END, 'poopsie lala')
        fldSender.grid(row = 2, column = 2)

        # Chat message
        self.varMsg = tk.StringVar()
        fldMsg = tk.Entry(mcFrame, textvariable=self.varMsg)
        fldMsg.insert(tk.END, 'Hi')
        fldMsg.grid(row = 3, column = 2)

        # Chat message
        self.varMsg = tk.StringVar()
        fldMsg = tk.Entry(mcFrame, textvariable=self.varMsg)
        fldMsg.insert(tk.END, 'Hi')
        fldMsg.grid(row = 3, column = 2)


        # Buttons
        # Chat button
        btnPostToChat = tk.Button(mcFrame, text='Send', command=self.mcchat)
        btnPostToChat.grid(row = 3, column = 4, padx = 5, pady = 5)

        
    def mcchat(self):
        try:
            mc = minecraft.Minecraft.create(self.varIpAddr.get())
            mc.postToChat(self.varSender.get() + ' > ' + self.varMsg.get())
        except Exception, e:
            print e
            self.statusbar.set('%s', e)

class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
