# Copyright (C) 2010 - SkyCore Project

import socket
import string

class ircconnect:
    def __init__(self):
        self.pingcounter = 0
        self.joindftchan = False
        
    def DoCreateSocket(self):
        ''' Creates the Socket '''
        self.soc = socket.socket()
    
    def DoConnectToIRC(self,host,port):
        ''' We are going to enter into the IRC world '''
        self.soc.connect((host,port))
        
    def DoSendInformation(self,nick,ident,host,realname):
        ''' Sending to the server what it wants from us '''
        self.soc.send("NICK %s\r\n" % nick)
        self.soc.send("USER %s %s bla :%s\r\n" % (ident,host,realname))
        
    def DoJoinDefaultChannel(self,channel):
        ''' We are going to join the default channel '''
        if(self.pingcounter == 2 and self.joindftchan == False):
            self.soc.send("JOIN %s\r\n" % channel)
            self.joindftchan = True
        
    def DoAnswerPing(self):
        ''' PING? PONG! Also counts the ammount of pings'''
        ircbuffer = self.soc.recv(1024)
        _ircbuffer = string.split(ircbuffer, "\n")
        ircbuffer = _ircbuffer.pop()
        
        print ircbuffer
        
        for info in _ircbuffer:
            info = string.rstrip(info)
            info = string.split(info)
            print info
            try:
                if(info[0] == "PING"):
                    self.soc.send("PONG %s\r\n" % info[1])
                    self.pingcounter += 1
            except:
                print "Ignoring empty string"

