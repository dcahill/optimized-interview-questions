from random import choice

def reset_game():
    global cells
    global game_over
    cells = {'a1':'', 'b1':'', 'c1':'', 'd1':'',
             'a2':'', 'b2':'', 'c2':'', 'd2':'',
             'a3':'', 'b3':'', 'c3':'', 'd3':'',
             'a4':'', 'b4':'', 'c4':'', 'd4':''}
    cell_list = ['a1','a2','a3','a4','b1','b2','b3','b4','c1','c2','c3','c4','d1','d2','d3','d4']
    
    for i in range(2):
        random_cell = choice(cell_list)
        cells[random_cell] = 2
        cell_list.remove(random_cell)

    game_over = False


def display_board():        
    print(' --------------------------- ')
    print('|      |      |      |      |')
    print('| {:^4} | {:^4} | {:^4} | {:^4} |'.format(cells['a1'],cells['b1'],cells['c1'],cells['d1']))
    print('|      |      |      |      |')
    print('|------+------+------+------|')
    print('|      |      |      |      |')
    print('| {:^4} | {:^4} | {:^4} | {:^4} |'.format(cells['a2'],cells['b2'],cells['c2'],cells['d2']))
    print('|      |      |      |      |')
    print('|------+------+------+------|')
    print('|      |      |      |      |')
    print('| {:^4} | {:^4} | {:^4} | {:^4} |'.format(cells['a3'],cells['b3'],cells['c3'],cells['d3']))
    print('|      |      |      |      |')
    print('|------+------+------+------|')
    print('|      |      |      |      |')
    print('| {:^4} | {:^4} | {:^4} | {:^4} |'.format(cells['a4'],cells['b4'],cells['c4'],cells['d4']))
    print('|      |      |      |      |')
    print(' --------------------------- ')


def add_random_cell():
    cell_list = []
    for cell in cells:
        if cells[cell] == '':
            cell_list.append(cell)
    random_cell = choice(cell_list)
    cells[random_cell] = 2


# Check win
def check_win():
    if '2048' in cells:
        print('You won in %s turns!' % turns)
        game_over = True
        reset_game()


# Check loss
def check_lose():
    if '' not in cells:
        print('You lost in %s turns!' % turns)
        game_over = True
        reset_game()


# Detect matches and collisions
def check_move(move):
    if move.lower() in 'wasd': return True
    else: return False


# Move/Update cells
def move_cells(move):
    rows = [1,2,3,4]
    columns = ['a', 'b', 'c', 'd']

    if move.lower() == 'w':
        for i in range(3):
            for row in rows:
                for column in columns:
                    cell = column + str(row)
                    if row > 1:
                        if cells[cell] != '':
                            cell_above = column + str(row - 1)
                            if cells[cell_above] == '':
                                cells[cell_above] = cells[cell]
                                cells[cell] = ''
                            elif cells[cell_above] == cells[cell]:
                                cells[cell_above] = cells[cell] + cells[cell_above]
                                cells[cell] = ''
    elif move.lower() == 's':
        for i in range(3):
            for row in rows[::-1]:
                for column in columns:
                    cell = column + str(row)
                    if row < 4:
                        if cells[cell] != '':
                            cell_below = column + str(row + 1)
                            if cells[cell_below] == '':
                                cells[cell_below] = cells[cell]
                                cells[cell] = ''
                            elif cells[cell_below] == cells[cell]:
                                cells[cell_below] = cells[cell] + cells[cell_below]
                                cells[cell] = ''
    elif move.lower() == 'a':
        for i in range(3):
            for column in columns:
                for row in rows:
                    cell = column + str(row)
                    if column != 'a':
                        if cells[cell] != '':
                            if column == 'b': cell_left = 'a' + str(row)
                            elif column == 'c': cell_left = 'b' + str(row)
                            elif column == 'd': cell_left = 'c' + str(row)
                            if cells[cell_left] == '':
                                cells[cell_left] = cells[cell]
                                cells[cell] = ''
                            elif cells[cell_left] == cells[cell]:
                                cells[cell_left] = cells[cell] + cells[cell_left]
                                cells[cell] = ''        
    elif move.lower() == 'd':
        for i in range(3):
            for column in columns[::-1]:
                for row in rows:
                    cell = column + str(row)
                    if column != 'd':
                        if cells[cell] != '':
                            if column == 'c': cell_right = 'd' + str(row)
                            elif column == 'b': cell_right = 'c' + str(row)
                            elif column == 'a': cell_right = 'b' + str(row)
                            if cells[cell_right] == '':
                                cells[cell_right] = cells[cell]
                                cells[cell] = ''
                            elif cells[cell_right] == cells[cell]:
                                cells[cell_right] = cells[cell] + cells[cell_right]
                                cells[cell] = ''        


while True:
    reset_game()
    display_board()

    while game_over == False:
        valid_move = False
        while valid_move == False:
            check_win()
            check_lose() # NEEDS IMPROVEMENT, NOT JUST FULL DETECTION. SHOULD DETECT IF NO VALID MOVES ARE LEFT.
            move = input('Please enter direction to slide cells [W][A][S][D]: ')
            print('-'*32)
            valid_move = check_move(move)
        move_cells(move)

        #check_move(move)
        add_random_cell()
        display_board()
