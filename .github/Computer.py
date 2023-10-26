#Same as player class except input is got from pred.py
class Computer:
    def __init__(self,player):
        global opp
        self.lh = 1
        self.rh = 1
        self.op = [self.lh, self.rh]
        self.lh.live = self.rh.live = True
        opp = player
        self.win = []
        self.drw = [[[1,1],[1,1],0], [[1,1],[1,1],1]]
    
    def checkvals(self):
        if self.lh == 0 or self.lh == 5:
            self.lh.live = False
            self.lh = 0
        else:
            self.lh.live = True
        if self.rh == 0 or self.rh == 5:
            self.rh.live = False
            self.rh = 0
        else:
            self.lh.live = True
        if self.lh == self.rh == 0:
            return "LOST"
        else:
            return "ALIVE"
        

    def rearrange(self, h1, h2, n):
        # Takes 3 values h1, h2, n
        # Moves n values from h1 to h2
        if h1 - n >= 0:
            h2 = h2 + n
            h1 = h1 - n
            if self.op.index(h1):
                self.op = [h1, h2]  # If index of h1 is True i.e. index == 1, h1 is right hand
                # And hence h2 is left hand
            else:
                self.op = [h2, h1]
            self.checkvals()
        elif h1 == 0:
            self.movefail("Not enough points in hand to give!")

    def moveFail(self, msg):
        global opp
        print("Encountered an error!\n", msg)
        self.getinp(self,opp)

    def getInp(self):
        global opp
        h1, h2, n = self.Calculate([self.op, opp.op],1)
        n = int(n)
        if n == 0:
            self.moveFail("Can't move 0 chopstics!")
        if h2 == "self":
            if h1 == "l":
                self.rearrange(self,self.lh,self.rh,n)
            if h1 == "r":
                self.rearrange(self,self.rh,self.lh,n)
            self.op = [self.lh,self.rh]
        elif h2 == "l":
            if h1 == "l":
                if self.lh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.lh += n
            else:
                if self.rh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.lh += n
        else: # h2 == "r"
            if h1 == "l":
                if self.lh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.rh += n
            else:
                if self.rh - n < 0:
                    self.moveFail("Not enough!")
                else:
                    opp.rh += n
        return self.checkvals()
    
    def moves(pos,n): #If n == 1, computer is playing. Else, player is playing
        cPos, pPos = pos[0], pos[1]
        Crh, Clh, Prh, Plh = not cPos[1]==0, not cPos[0]==0, not pPos[1]==0, not pPos[0]==0
        allMoves = []
        
        if n == 1:
            #LEFT HAND
            if Clh:
                for i in range(1,cPos[0]+1):
                    allMoves.append(f"lh rh {i}")
                    allMoves.append(f"lh lh {i}")
                    if cPos[1] + i < 5:
                        allMoves.append(f"lh self {i}")
            #RIGHT HAND
            if Crh:
                for i in range(1,cPos[1]+1):
                    allMoves.append(f"rh rh {i}")
                    allMoves.append(f"rh lh {i}")
                    if cPos[0] + i < 5:
                        allMoves.append(f"rh self {i}")

        if n == 0:
            if Plh:
                for i in range(1,pPos[0]+1):    
                    allMoves.append(f"lh rh {i}")
                    allMoves.append(f"lh lh {i}")
                    if pPos[1] + i < 5:
                        allMoves.append(f"lh self {i}")
            #RIGHT HAND
            if Prh:
                for i in range(1,pPos[1]+1):
                    allMoves.append(f"rh rh {i}")
                    allMoves.append(f"rh lh {i}")
                    if pPos[0] + i < 5:
                        allMoves.append(f"rh self {i}")
        return allMoves
    
    def processC(self,move,pos):
        h1,h2,n = move.split(" ")
        crh,clh,prh,plh = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
        if h2 == "self":
            if h1 == "lh":
                crh += n
                clh -= n
            else:
                crh -= n
                clh += n
        elif h2 == "lh":
            plh += n
        else:
            prh += n
    
    def processP(self,move,pos):
        h1,h2,n = move.split(" ")
        crh,clh,prh,plh = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
        if h2 == "self":
            if h1 == "lh":
                prh += n
                plh -= n
            else:
                prh -= n
                plh += n
        elif h2 == "lh":
            clh += n
        else:
            crh += n     
    
    def Calculate(self,pos,n): # if n == 1, computer move. Else, player move.
        pPos, cPos = pos # Computer Hands, Player Hands
        for i in self.moves(pos,1): # ex : i = "lh rh 1"
            j = self.process(i,pos)     # ex : j = [[1,1], [1,1], 0]
            if j in self.drw:
                pass
            elif j in self.win:
                return i.split(" ")
