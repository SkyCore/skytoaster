# Copyright (C) 2010 - SkyCore Project

# This lib is a small game implementation using SQLite3
# Also shows how to add your own functions on core

import sqlite3

COMMANDS = ["create", "help"]

class WorldHandler(GameMehanic):
    def __init__(self):
        self.playersOnWorld = []
        
    def DoPlayerOnWorldCheck(self):
        ''' Do a global check to see if we need to add any new player on world '''
        playerCompare = []
        size = len(self.playersOnWorld)
        self.CreateSQLConnection()
        try:
            self.c.execute("""select name from characters""")
            for row in self.c:
                _row = row[0]
                playerCompare.append(_row)
            
                
            if len(playerCompare) > len(self.playersOnWorld):
                for i in range(len(playerCompare) - len(self.playersOnWorld)):
                    self.playersOnWorld.append(playerCompare[size+i])
                

class GameMechanic:
    def __init__(self,dbloc,soc,channel):
        self.dbloc = dbloc #Location of Where the DB is
        self.soc   = soc   #Our socket data
        self.channel = channel
        
    def CreateSQLConnection(self):
        ''' Opens an SQL connection and creates a cursor '''
        self.sqlcon = sqlite3.connect(self.dbloc)
        self.c = self.sqlcon.cursor()
        
    def CloseSQLConnection(self):
        ''' Saves the work and close the SQL connection '''
        self.sqlcon.commit()
        self.c.close() #Close our cursor
        self.sqlcon.close()        
        
    def CreateNewPlayer(self,name):
        ''' Creates a new Player on DB and adds it onto world '''
        self.CreateSQLConnection()
        try:
            self.c.execute("select name from characters where name = ?", name)
            for row in self.c:
                _row = row #if it's empty the _row is not set
                
            if _row: #very bad way to check that
                self.soc.send("PRIVMSG "+ self.channel + " :Name already taken. Please try another one...\r\n")
                
        except:
            self.c.execute("insert into characters values (?,?,?,?,?,?,?)", [name,1,1,1,5,60,0])
            self.soc.send("PRIVMSG "+ self.channel +" :Character created sucessfully!\r\n")
            self.soc.send("PRIVMSG "+ self.channel +" :Adding character to world on next check...\r\n")
            
        self.CloseSQLConnection()
