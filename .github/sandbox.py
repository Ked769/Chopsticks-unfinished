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
                    if (cPos[1] + i) < 5:
                        allMoves.append(f"lh self {i}")
            #RIGHT HAND
            if Crh:
                for i in range(1,cPos[1]+1):
                    allMoves.append(f"rh rh {i}")
                    allMoves.append(f"rh lh {i}")
                    if (cPos[0] + i) < 5:
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
        
        print(allMoves)