row1 = ['1',  '2',  '3']
row2 = ['4',  '5',  '6']
row3 = ['7',  '8',  '9']
player_0 = "bob"
player_x = "jill"
player_x_counter = 4
player_0_counter = 4
player_x_score = 0
player_0_score = 0
player_0_counter_display = player_0_counter * "0"
player_x_counter_display = player_x_counter * "X"
taken_numbers = []
win = False
game_count = 0


def game_board():
    print(f"    {player_0}                             {player_x}")
    print(f"              {row1}                 ")
    print(f"     {player_0_score}        {row2}        {player_x_score}")
    print(f"              {row3}")
    print(f"   {player_0_counter_display}                            {player_x_counter_display}")


print(game_board())

