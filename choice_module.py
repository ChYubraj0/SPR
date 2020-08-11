import random



class ProcessData():
    

    def __init__(self,player_command):
        self.player_command=player_command
    def show_player_command(self):
        x= self.player_command
        return x
    def generate_machine_command(self):
        y=random.choice(('s','p','r'))
        return y