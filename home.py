from choice_module import ProcessData
from dxisplay_result import result
loop='a'
while loop !="q":
    player_choice=input("Your turn, S/P/R?\n")
    player_choice=player_choice.lower()

    processing=ProcessData(player_choice)
    machine_command=processing.generate_machine_command()
    who_win=result(player_choice,machine_command)

    if who_win.winner()!="Wrong Command":
        print("You choose : "+processing.show_player_command())
        print("Robo choose: "+machine_command)
        print("AND THE WINNER IS: "+who_win.winner())
    else:print("Wrong command.Press any key to retry OR")

    loop=input("Press Q to quit.\n")
    loop.title()