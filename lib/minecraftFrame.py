# -*- coding: utf-8 -*-
import Tkinter as tk
import ttk as ttk
from tkFont import Font
from collections import namedtuple
import mcpi.minecraft as minecraft 
import mcpi.block as block
from sys import platform
import netifaces as ni
try:
    from netifaces import AF_INET, AF_INET6, AF_LINK
except Exception, e:
    pass

class MinecraftFrame(ttk.Frame):
    def __init__(self, parent):

        
        mcFrame = ttk.Frame(parent, width=200, height=100,)
        mcFrame.pack()

        localIpAddr = 'unknown'
        if platform == "linux" or platform == "linux2":
            # linux
            try:
                localIpAddr = ni.ifaddresses('wlan0')[AF_INET][0]['addr']
            except Exception, e:
                pass
        elif platform == "darwin":
            # OS X
            try:
                localIpAddr = ni.ifaddresses('en0')[AF_INET][0]['addr']
            except Exception, e:
                pass
        elif platform == "win32":
            # Windows...
            localIpAddr = 'win32.unknown'

        # Add the frame to the notebook
        parent.add(mcFrame, text="Minecraft")

        #Status bar
        lblStatus = tk.Label(mcFrame, bg='gray90', text="Status: ")
        lblStatus.grid(row = 0, column = 1, padx = 5, pady = 5, sticky=tk.E)
        self.statusbar = StatusBar(mcFrame)
        self.statusbar.grid(row = 0, column = 2, sticky=tk.W)
        self.statusbar.set('%s', 'Ready')

        # Labels
        # To IP address
        lblIpAddress = tk.Label(mcFrame, bg='gray90', text="To IP Address: ")
        lblIpAddress.grid(row = 1, column = 1, padx = 5, pady = 5, sticky=tk.E)

        # Sender name
        lblSender = tk.Label(mcFrame, bg='gray90', text="Your Name: ")
        lblSender.grid(row = 2, column = 1, padx = 5, pady = 5, sticky=tk.E)

        # Chat message
        lblMsg = tk.Label(mcFrame, bg='gray90', text="Your Message: ")
        lblMsg.grid(row = 3, column = 1, padx = 5, pady = 5, sticky=tk.E)

        # Player position
        lblPlayerPos = tk.Label(mcFrame, bg='gray90', text="Player Position: ")
        lblPlayerPos.grid(row = 4, column = 1, padx = 5, pady = 5, sticky=tk.E)

        # Local IP address
        lblYourIp = tk.Label(mcFrame, bg='gray90', text="Your IP Address: ")
        lblYourIp.grid(row = 5, column = 1, padx = 5, pady = 5, sticky=tk.E)
        

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

        # Player position
        self.varPlayerPos = tk.StringVar()
        fldPlayerPos = tk.Label(mcFrame, bg='lemon chiffon', fg='black', width=20, textvariable=self.varPlayerPos)
        fldPlayerPos.grid(row = 4, column = 2, sticky=tk.W)

        # Local IP Address
        self.varYourIp = tk.StringVar()
        fldYourIp = tk.Label(mcFrame, bg='lemon chiffon', fg='black', width=20, textvariable=self.varYourIp)
        self.varYourIp.set(localIpAddr)
        fldYourIp.grid(row = 5, column = 2, sticky=tk.W)


        # Buttons
        # Chat button
        btnPostToChat = tk.Button(mcFrame, width=8, text='Send', command=self.mcChat)
        btnPostToChat.grid(row = 3, column = 4, padx = 5, pady = 5)

        # Player Position button
        btnPlayerPos = tk.Button(mcFrame, width=8, text='Get Position', command=self.mcPlayerPos)
        btnPlayerPos.grid(row = 4, column = 4, padx = 5, pady = 5)

        
    def mcChat(self):
        try:
            mc = minecraft.Minecraft.create(self.varIpAddr.get())
            mc.postToChat(self.varSender.get() + ' > ' + self.varMsg.get())
            self.statusbar.set('%s', 'Sent')
        except Exception, e:
            print e
            self.statusbar.set('%s', e)

    def mcPlayerPos(self):
        try:
            mc = minecraft.Minecraft.create(self.varIpAddr.get())
            pos = mc.player.getTilePos()
            self.varPlayerPos.set('x=' + str(pos.x) + ', y=' + str(pos.y) + ', z=' + str(pos.z))
            self.statusbar.set('%s', 'Retrieved position')
        except Exception, e:
            print e
            self.statusbar.set('%s', e)

class StatusBar(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, bd=1, anchor=tk.W, bg='light cyan')
        self.label.pack(fill=tk.X)

    def set(self, format, *args):
        self.label.config(width=20,text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
