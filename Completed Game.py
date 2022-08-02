row1 = ['1', '2', '3']
row2 = ['4', '5', '6']
row3 = ['7', '8', '9']
player_x_counter = 4
player_0_counter = 4
player_x_score = 0
player_0_score = 0
player_0_counter_display = player_0_counter * "0"
player_x_counter_display = player_x_counter * "X"
taken_numbers = []
win = False
game_count = 0
player_0 = "0"
player_x = "x"


def game_board():
    print(f"    {player_0}                             {player_x}")
    print(f"              {row1}                 ")
    print(f"     {player_0_score}        {row2}        {player_x_score}")
    print(f"              {row3}")
    print(f"   {player_0_counter_display}                           {player_x_counter_display}")


def game_board_edit():
    if int(choice) == 1:
        row1[0] = game_piece
    elif int(choice) == 2:
        row1[1] = game_piece
    elif int(choice) == 3:
        row1[2] = game_piece
    elif int(choice) == 4:
        row2[0] = game_piece
    elif int(choice) == 5:
        row2[1] = game_piece
    elif int(choice) == 6:
        row2[2] = game_piece
    elif int(choice) == 7:
        row3[0] = game_piece
    elif int(choice) == 8:
        row3[1] = game_piece
    elif int(choice) == 9:
        row3[2] = game_piece


def win_lines():
    win_line1 = [row1[0], row1[1], row1[2]]
    win_line2 = [row2[0], row2[1], row2[2]]
    win_line3 = [row3[0], row3[1], row3[2]]
    win_line4 = [row1[0], row2[0], row3[0]]
    win_line5 = [row1[1], row2[1], row3[1]]
    win_line6 = [row1[2], row2[2], row3[2]]
    win_line7 = [row1[0], row2[1], row3[2]]
    win_line8 = [row1[2], row2[1], row3[0]]
    all_win_lines = [win_line1, win_line2, win_line3, win_line4, win_line5, win_line6, win_line7, win_line8]
    for line in all_win_lines:
        target = []
        for item in line:
            target.append(item)
        if target == ["x", "x", "x"] or target == ["0", "0", "0"]:
            return True
        else:
            pass


command = ""
while command != "quit":
    game_ready = 0
    win = False
    command = input(f"Play or Quit?: ").lower()
    if command == "quit" and game_count >= 1:
        print("                              ")
        print(f"{player_0} - {player_0_score}")
        print(f"{player_x} - {player_x_score}")
        print("                              ")
        print("Thanks for playing")
        break
    elif command == "quit":
        print("                              ")
        print("Thanks for playing")
        break
    elif command == "play" and game_count == 0:
        player_0 = input(f"Enter player 0 name: ")
        if player_0 == "":
            player_0 = "0"
        player_x = input(f"Enter player x name: ")
        if player_x == "":
            player_x = "x"
        game_ready += 1
    elif command == "play" and game_count > 0:
        game_ready += 1
    else:
        print("Invalid Entry")

    if game_ready == 1:
        while game_ready == 1:
            game_piece = input(f"0 or X to go first? ")
            if game_piece == "0":
                player_0_counter = 5
                break
            elif game_piece.lower() == "x":
                player_x_counter = 5
                break
            else:
                print("Incorrect entry")

        player_0_counter_display = player_0_counter * "0"
        player_x_counter_display = player_x_counter * "X"

        while win == False:
            while player_x_counter + player_0_counter > 0:
                if game_piece == "0" and player_0_counter == player_x_counter:
                    game_piece = "x"
                elif game_piece.lower() == "x" and player_0_counter == player_x_counter:
                    game_piece = "0"
                if player_0_counter > player_x_counter:
                    game_piece = "0"
                elif player_x_counter > player_0_counter:
                    game_piece = "x"
                game_board()
                choice = "WRONG"
                acceptable_range = range(1, 10)
                within_range = False
                while choice.isdigit() == False or within_range == False:
                    choice = input(f"Player {game_piece}, Pick a square: ")
                    if not choice.isdigit():
                        print("Sorry that is not a number")
                    if choice.isdigit():
                        if int(choice) not in taken_numbers:
                            if int(choice) in acceptable_range:
                                within_range = True
                                taken_numbers.append(int(choice))
                                game_board_edit()
                            else:
                                print("Incorrect number entered")
                        else:
                            print("Sorry that number is already taken")
                            within_range = False

                if game_piece == "0":
                    player_0_counter -= 1
                    player_0_counter_display = player_0_counter * "0"
                elif game_piece == "x":
                    player_x_counter -= 1
                    player_x_counter_display = player_x_counter * "X"

                if win_lines():
                    winner = ""
                    if game_piece == "0":
                        player_0_score += 1
                        winner = player_0
                    elif game_piece == "x":
                        player_x_score += 1
                        winner = player_x
                    print(f"CONGRATULATIONS {winner}, you have won!")
                    game_board()
                    win = True
                    row1 = ['1', '2', '3']
                    row2 = ['4', '5', '6']
                    row3 = ['7', '8', '9']
                    player_x_counter = 4
                    player_0_counter = 4
                    game_piece = ""
                    player_0_counter_display = player_0_counter * "0"
                    player_x_counter_display = player_x_counter * "X"
                    taken_numbers = []
                    game_count += 1
                    break
                else:
                    pass

            if player_x_counter + player_0_counter == 0 and win == False:
                print("Out Of Moves!")
                win = True
                row1 = ['1', '2', '3']
                row2 = ['4', '5', '6']
                row3 = ['7', '8', '9']
                player_x_counter = 4
                player_0_counter = 4
                player_0_counter_display = player_0_counter * "0"
                player_x_counter_display = player_x_counter * "X"
                taken_numbers = []
                game_count += 1
                break
            elif player_x_counter + player_0_counter == 0 and win == True:
                if win_lines():
                    winner = ""
                    if game_piece == "0":
                        player_0_score += 1
                        winner = player_0
                    elif game_piece == "x":
                        player_x_score += 1
                        winner = player_x
                    print(f"CONGRATULATIONS {winner}, you have won!")
                    game_board()
                    win = True
                    row1 = ['1', '2', '3']
                    row2 = ['4', '5', '6']
                    row3 = ['7', '8', '9']
                    player_x_counter = 4
                    player_0_counter = 4
                    game_piece = ""
                    player_0_counter_display = player_0_counter * "0"
                    player_x_counter_display = player_x_counter * "X"
                    taken_numbers = []
                    game_count += 1
                    break
                else:
                    pass
            else:
                pass
    elif game_ready == 0:
        pass
