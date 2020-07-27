import random

# To add
# Pick X or O or Random
# Score tracker

def draw_board(cells):
    print('\n%s | %s | %s' % (cells[0], cells[1], cells[2]))
    print('---------------')
    print('%s | %s | %s' % (cells[3], cells[4], cells[5]))
    print('---------------')
    print('%s | %s | %s' % (cells[6], cells[7], cells[8]))

def check_winner(cells):
        # Horizontal
    if (all(x==cells[0] for x in cells[0:3]) or
        all(x==cells[3] for x in cells[3:6]) or
        all(x==cells[6] for x in cells[6:9]) or
        # Vertical
        all(x==cells[0] for x in (cells[0], cells[3], cells[6])) or
        all(x==cells[1] for x in (cells[1], cells[4], cells[7])) or
        all(x==cells[2] for x in (cells[2], cells[5], cells[8])) or
        # Diagonal
        all(x==cells[0] for x in (cells[0], cells[4], cells[8])) or
        all(x==cells[2] for x in (cells[2], cells[4], cells[6]))
        ):
        return True

def check_free(cell, cells):
    if cells[cell] != player_one and cells[cell] != player_two:
        return True
    else:
        return False

def find_move(cells):
    # I'm sure there's a much fancier way to do this with maths but I suck at maths so...
    # Here's every possible tic-tac-toe move and strategy that exists to ensure perfect play.
    
    # Determine other player
    if current_player == player_one:
        other_player = player_two
    else:
        other_player = player_one

    # Check if any player is 1 move away from winning
    for check_player in [other_player, current_player]:
        # Horizontal
        if all(x==check_player for x in (cells[0], cells[1])) and check_free(2, cells): return 2
        if all(x==check_player for x in (cells[1], cells[2])) and check_free(0, cells): return 0
        if all(x==check_player for x in (cells[3], cells[4])) and check_free(5, cells): return 5
        if all(x==check_player for x in (cells[4], cells[5])) and check_free(3, cells): return 3
        if all(x==check_player for x in (cells[6], cells[7])) and check_free(8, cells): return 8
        if all(x==check_player for x in (cells[7], cells[8])) and check_free(6, cells): return 6
        # Horizontal spaces
        if all(x==check_player for x in (cells[0], cells[2])) and check_free(1, cells): return 1
        if all(x==check_player for x in (cells[3], cells[5])) and check_free(4, cells): return 4
        if all(x==check_player for x in (cells[6], cells[8])) and check_free(7, cells): return 7    
        # Vertical
        if all(x==check_player for x in (cells[0], cells[3])) and check_free(6, cells): return 6
        if all(x==check_player for x in (cells[1], cells[4])) and check_free(7, cells): return 7
        if all(x==check_player for x in (cells[2], cells[5])) and check_free(8, cells): return 8
        if all(x==check_player for x in (cells[3], cells[6])) and check_free(0, cells): return 0
        if all(x==check_player for x in (cells[4], cells[7])) and check_free(1, cells): return 1
        if all(x==check_player for x in (cells[5], cells[8])) and check_free(2, cells): return 2
        # Vertical spaces
        if all(x==check_player for x in (cells[0], cells[6])) and check_free(3, cells): return 3
        if all(x==check_player for x in (cells[1], cells[7])) and check_free(4, cells): return 4
        if all(x==check_player for x in (cells[2], cells[8])) and check_free(5, cells): return 5
        # Diagonals
        if all(x==check_player for x in (cells[0], cells[4])) and check_free(8, cells): return 8
        if all(x==check_player for x in (cells[2], cells[4])) and check_free(6, cells): return 6
        if all(x==check_player for x in (cells[6], cells[4])) and check_free(2, cells): return 2
        if all(x==check_player for x in (cells[8], cells[4])) and check_free(0, cells): return 0
        # Diagonal spaces
        if all(x==check_player for x in (cells[0], cells[8])) and check_free(4, cells): return 4
        if all(x==check_player for x in (cells[2], cells[6])) and check_free(4, cells): return 4

    # Take middle always if available
    if check_free(4, cells): return 4

    # Then favor a corner (random)
    # Then favor a side (random)
    corner_moves = [0, 2, 6, 8]
    side_moves = [1, 3, 5, 7]
    random.shuffle(corner_moves)
    random.shuffle(side_moves)

    for x in corner_moves:
        if check_free(x, cells): return x
    
    for x in side_moves:
        if check_free(x, cells): return x

    print('No valid moves....something is wrong with the AI code...')

# Initialize variables
def reset_game():
    global player_one
    global player_two
    global current_player
    global turn
    global cells
    player_one = ' X '
    player_two = ' O '
    current_player = player_one
    turn = 0
    cells = ['[0]', '[1]', '[2]',
             '[3]', '[4]', '[5]',
             '[6]', '[7]', '[8]']
    print('-'*25)
    draw_board(cells)

# Main
reset_game()

while 1:
    
    if turn >= 9:
        print('\nTie!')
        reset_game()
        
    if check_winner(cells):
        print('\n' + current_player + ' is the Winner!')
        reset_game()
        
    if turn % 2 == 0:
        current_player = player_one
    else:
        current_player = player_two
        
    if current_player == player_two:
        ai_move = find_move(cells)
        cells[ai_move] = current_player
        turn += 1
        draw_board(cells)
    else:
        print('\n[' + current_player + '\'s turn ]')
        #print('AI suggested move is:', find_move(cells))
        prompt = input('Please select an empty cell or e[x]it: ')
        if str(prompt.lower()) == 'x': break
        prompt = int(prompt)
        if check_free(prompt, cells):
            cells[prompt] = current_player
            turn += 1
            draw_board(cells)
