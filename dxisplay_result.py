class result():
    def __init__(self,player_command,machine_command):
        self.pl=player_command
        self.m=machine_command 
    def winner(self):
        if (self.pl=="s" and self.m=="p") or (self.pl=="p" and self.m=="r") or (self.pl=="r" and self.m=="s"):
            return "Player"
        elif (self.m=="s" and self.pl=="p") or (self.m=="p" and self.pl=="r") or (self.m=="r" and self.pl=="s"):
            return "machine"
        elif self.pl==self.m: return "Draw"
        else:return "Wrong Command"
    
