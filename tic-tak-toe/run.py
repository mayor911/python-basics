from random import randint
from time import sleep
from os import system as sys

def create_board():
    spaced_line = ' | | \n'
    breaker = '-|-|-\n'
    n = '\n'
    board = n + spaced_line + breaker + spaced_line + breaker + spaced_line
    return board

def show_slots():
    print(create_board())

def get_slot(taken_slots):
    print('Choose slot (1-9): ', end=' ')
    try:
        try:
            slot = input().strip()
            if slot in '123456789' and int(slot) not in taken_slots:
                return int(slot)
            else:
                print("That's not a slot, choose again")
                return get_slot(taken_slots)
        except KeyboardInterrupt as e:
            print("Exiting program")
            exit(0)
        except:
            print("Please choose a vaccant slot")
            return get_slot(taken_slots)
    except:
        print('Game found glitch and exiting')
        exit(0)
        

def change_board(board, index_to_place, xter = 'z'):
    new_board = ''

    #for slot in slot_dict:
     #   if slot_dict[slot] == slot_no:

    for index in range(0, len(board)):
        if index == index_to_place:
            new_board += xter
        else:
            new_board += board[index]
    #print(f'Len of old board = {len(board)} and {len(new_board)} is of new one')
    return new_board

def check_winner(player_slots):
    ''' Takes in string of slots plater has placed'''
    # slots are mapped to indexes on board
    '''
    winning_lines = [[1,2,3], [4, 5, 6], [7, 8, 9],
                     [3,5,7],
                     [1, 4, 7], [2,5,8], [3,6,9],
                     [1,5,9]]

    '''
    winning_lines = [[1,3,5], [13, 15, 17], [25, 27, 29],
                     [5,15,25],
                     [1, 13, 25], [3,15,27], [5,17,29],
                     [1,15,29]]

    times_gotten = 0
    won = False
    for line in winning_lines:
        for slot in player_slots:
            if slot in line:
                times_gotten += 1
        if times_gotten == 3:
            won = True
            break
        else:
            times_gotten = 0
    '''
    if won:
        print('You win')
    else:
        print('You loose') 
    '''
    return won

def get_slot_indexes(board, xter = 'z'):
    indexes = []
    for index in range(0, len(board) -1):
        # Check if we reached last slot in board
        if index < len(board) - 1:
            reached_bar = board[index+1] == '|'  or board[index-1] == '|' 
            reached_space = board[index] != '-' and reached_bar 
        else:
            reached_space = True
        can_take_index = board[index] == xter
        if reached_space and can_take_index:
            indexes.append(index)
    return indexes

def map_slots_on_board(board, xter) -> dict:
    slot_dict = {}
    slot_list = get_slot_indexes(board, xter)
    for i in range(0, len(slot_list)):
        slot_dict[f'slot{i+1}'] = slot_list[i]
    return slot_dict


def playAgain() -> None:
    choice = input('Do you want to play again (yes/no): ')
    if choice.lower == 'yes' or choice.startswith('y'):
        clear_screen()
        run()
    else:
        print('\tThanks for playing with us,.... ByeBye!')
        exit(0)
def clear_screen():
    try:
        sys('clear')
    except:
        sys('cls')

def comp_choose_slot(taken_indexes):
    #print( end = ' ')
    slot = randint(1, 9)
    while slot in taken_indexes:
        slot = randint(1, 9)
    sleep(2)
    print(f'\tselected slot {slot}')
    return slot

def run():

    game_is_running = True
    player_is_user = True
    taken_slots = []
    turns_taken = 0
    board = create_board()
    all_slots = map_slots_on_board(board, ' ')
    print(board)
    while game_is_running:
        if player_is_user:
            choosen_slot = get_slot(taken_slots)
            xter = 'X'
        else:
            print("Computer's turn...")
            choosen_slot = comp_choose_slot(taken_slots)
            xter = 'O'
        index_to_place = 0
        for slot in all_slots:
            if slot == f'slot{choosen_slot}':
                index_to_place = all_slots[slot]
                break
            else:
                index_to_place = 0
        # check since no slot has index 0, let's compare against it
        if index_to_place > 0 and choosen_slot not in taken_slots:
            board = change_board(board, index_to_place, xter)
            taken_slots.append(choosen_slot)
            print(board)
        turns_taken += 1
        if turns_taken >= 3:
            if check_winner(get_slot_indexes(board, xter)):
                msg = "You win!" if player_is_user else "You loose!"
                print(msg)
                game_is_running = False
        elif turns_taken >= 9:
            print('Seems like a draw')
            game_is_running = False
        player_is_user = not player_is_user
    playAgain()
    #comp_slots = []
    #player_slots = []
    #player_is_user = True
    #game_ended = False
    #user_won = False
'''
    #while not game_ended:
    for i in range(0, 9):
        if player_is_user:
            slot = get_slot()
            while slot in comp_slots or slot in player_slots:
                slot = get_slot()
            player_slots.append(slot)
            xter = ''
        else:
            slot = randint(0, 9)
            while slot in comp_slots or slot in player_slots:
                slot = randint(0, 9)
            comp_slots.append(slot)
            xter = 'O'
        
        if not player_is_user:
            print("Comp is playing..")
        board = play(board, slot, xter)
        player_is_user = not player_is_user
        print(board)
        if i > 4:
            comp_current_slots = get_slot_indexes(board, 'O')
            user_current_slots = get_slot_indexes(board, 'X')
            if check_winner(comp_current_slots):
                print('You loose!!')
                break
            elif check_winner(user_current_slots):
                print('You win!!')
                break
'''
        

if __name__ == "__main__":
    run()
