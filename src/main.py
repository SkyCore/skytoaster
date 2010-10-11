# Copyright (C) 2010 - SkyCore Project

import time
#import Threading
from conlib import *


## Config stays here for now ##

BOTNAME = "SkyToaster"
IDENT   = "toaster"
REALNAME= "skytoaster"
DFTCHAN = "#skycore"
HOST    = "irc.rizon.net"
PORT    = 6667

## End of Config ##



## Program Variables ##

RECONNECTS = 0
COMMANDTRIGGER "!"

while True:
    irc = ircconnect()
    soc = irc.DoCreateSocket()
    irc.DoConnectToIRC(HOST,PORT)
    irc.DoSendInformation(BOTNAME,IDENT,IDENT,REALNAME)
       
    while True:
        irc.DoAnswerPing()
        irc.DoJoinDefaultChannel(DFTCHAN)
        


    print "Waiting 30 seconds to reconnect."
    time.sleep(30)
    
    RECONNECTS += 1
