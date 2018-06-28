program_is_running = True
previous_commands = [".",".",".",".",".",".",".",".",".","."]
position = 0
while(program_is_running):
    print("To stop the program input: \"stop\"")
    print("To get previous input list: \"list\"")
    user_Command = input()
    print("")
    try:
        if(user_Command == "stop"):
            program_is_running =False
            break
        if(user_Command == "list"): 
            for x in range(0,10):
                print(x+1,previous_commands[x])
            print("Please select what command you wish to re-run [0] to cancel")
            print("")
            user_choice =input()

            if(int(user_choice)==0):
                continue
            user_Command = previous_commands[int(user_choice)-1]
        if(user_Command == "."):
            continue
        eval(user_Command)
        previous_commands[position] = user_Command
        position = (position +1) % 10
        print("")
    except:
        print("Error: unacceptable input.")