SIZE_OF_FIELD = 3
GAME_OVER = False
game_field = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
]

player_name = ['player 1st', 'player 2nd']

row_num = 0
col_num = 0



def show_game_rules():
    pass


def show_menu():
    pass


def show_player_message(plr_num : int):
    print()
    print(player_name[plr_num], 'symbol: ','X' if plr_num == 0 else '0')


def chk_cell(row_num : int, col_num : int, plr_sym : str):
    pass


def user_input(plr_num2 : int):
    global row_num
    global col_num

    if plr_num2 == 0:
        plr_sym = 'X'
    else:
        plr_sym = '0'

    row_num = int(input('Input row number from 0 to ' + str(SIZE_OF_FIELD-1) + ' Include: '))
    col_num = int(input('Input column number from 0 to ' + str(SIZE_OF_FIELD-1) + ' Include: '))
    chk_cell(row_num, col_num, plr_sym)


def show_field(sz : int):
    for row in range(sz):
        for col in range(sz):
            print(game_field[row][col], end='')
        print()


def game_field_change(plr_num3 : int):
    game_field[row_num][col_num] = 'X' if plr_num3 == 0 else '0'


def start_game(gsize : int):
    show_field(gsize)


def chk_winner(plr_num4 : int):
    global GAME_OVER
    if plr_num4 == 0:
        plr_sym = 'X'
    else:
        plr_sym = 'O'

    if game_field[0][0] == plr_sym and game_field[0][1] == plr_sym and game_field[0][2] == plr_sym:
        print('Player', plr_sym,' WIN')
        GAME_OVER = True
    if game_field[1][0] == plr_sym and game_field[1][1] == plr_sym and game_field[1][2] == plr_sym:
        print('Player', plr_sym,' WIN')
        GAME_OVER = True
    if game_field[2][0] == plr_sym and game_field[2][1] == plr_sym and game_field[2][2] == plr_sym:
        print('Player', plr_sym,' WIN')
        GAME_OVER = True
    # columns
    if game_field[0][0] == plr_sym and game_field[1][0] == plr_sym and game_field[2][0] == plr_sym:
        print('Player', plr_sym,' WIN')
        GAME_OVER = True
    if game_field[0][1] == plr_sym and game_field[1][1] == plr_sym and game_field[2][1] == plr_sym:
        print('Player', plr_sym,' WIN')
        GAME_OVER = True
    if game_field[0][2] == plr_sym and game_field[1][2] == plr_sym and game_field[2][2] == plr_sym:
        print('Player', plr_sym,' WIN')
        GAME_OVER = True

    # not optimal algorithm
    # TODO: two diagonals

def play_game():
    show_player_message(0)
    user_input(0)
    game_field_change(0)
    chk_winner(0)

    show_field(SIZE_OF_FIELD)

    show_player_message(1)
    user_input(1)
    game_field_change(1)
    chk_winner(1)

    show_field(SIZE_OF_FIELD)


def main(arguments):
    start_game(SIZE_OF_FIELD)
    while not GAME_OVER:
        play_game()
    print('GAME OVER')
    return 0 


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
