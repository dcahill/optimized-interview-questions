def draw_board(cells):
    print('%s | %s | %s' % (cells[0], cells[1], cells[2]))
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

# Initialize variables
player_one = ' X '
player_two = ' O '
current_player = player_one
turn = 0
cells = ['[0]', '[1]', '[2]',
         '[3]', '[4]', '[5]',
         '[6]', '[7]', '[8]']

# Main
while 1:
    draw_board(cells)
    if turn >= 9:
        print('Tie!')
        break
    if check_winner(cells):
        print('Winner!')
        break
    if turn % 2 == 0:
        current_player = player_one
    else:
        current_player = player_two
    print(current_player + '\'s turn')
    prompt = int(input('Please select an empty cell:'))
    if cells[prompt] != player_one and cells[prompt] != player_two:
        cells[prompt] = current_player
        turn += 1
