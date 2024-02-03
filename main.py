from model import *
from model import Colors

GAME_STATES = ['RUNNING', 'WIN', 'GAME_OVER']
CAMP_SIZE: int = 9
BOMB_QUANTITY: int = 20
COVERED_SYMBOL = f'{Colors.B_GRAY}{Colors.F_BLACK} + {Colors.RESET}'
BOMB_SYMBOL = f'{Colors.B_RED}{Colors.F_WHITE} * {Colors.RESET}'

game_state = 'RUNNING'
camp = Camp(BOMB_QUANTITY, CAMP_SIZE)
range_camp_size = range(0, CAMP_SIZE)
view_y_axis = [str(i + 1) for i in range_camp_size]
view_x_axis = [chr(i + 65) for i in range_camp_size]


def show_camp(mode: str = 'NORMAL'):
    print(f'\n     {"  ".join(view_x_axis)}\n')
    for y in range_camp_size:
        print(f'{view_y_axis[y]}    ', end="")
        for x in range_camp_size:
            spot = [spot for spot in camp.spots if spot.y_axis == y if spot.x_axis == x][0]
            if spot.is_covered:
                if mode == 'NORMAL':
                    print(COVERED_SYMBOL, end="")
                if mode == 'ID':
                    print(
                        f'{Colors.F_RED if spot.is_bomb else ""}{spot.spot_id:02}{Colors.RESET if spot.is_bomb else ""}',
                        end=" ")
            else:
                if spot.is_bomb:
                    print(BOMB_SYMBOL, end="")
                else:
                    print(
                        f'{Colors.NEIGHBOUR_BOMBS_COLORS[spot.neighbours_bombs]}{Colors.F_BLACK} {spot.neighbours_bombs} {Colors.RESET}',
                        end="")

        print()


def clear_console():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def get_spot(coordinate_x, coordinate_y):
    return [spot for spot in camp.spots if spot.y_axis == coordinate_y if spot.x_axis == coordinate_x][0]


def ask_coordinates():
    while True:
        try:
            coordinates = input('\nEnter the coordinates, for example, A1: ')
            coordinate_x = view_x_axis.index(coordinates[:1].upper())
            coordinate_y = view_y_axis.index(coordinates[1:2])
            return get_spot(coordinate_x, coordinate_y)
        except Exception as e:
            print('Invalid coordinates!')

def discover(spot: Spot):
    spot = camp.discover_spot(spot)
    if spot.neighbours_bombs == 0:
        camp.discover_neighbour_zeroes(spot)


def check_game_state():
    for spot in camp.spots:
        if spot.is_bomb and not spot.is_covered:
            return GAME_STATES[2]  # GAME_OVER

    for spot in camp.spots:
        if not spot.is_bomb and spot.is_covered:
            return GAME_STATES[0]  # RUNNING

    return GAME_STATES[1]  # WIN


def end_game(game_state):
    print('\n\n')
    camp.reveal_camp()
    show_camp()

    if game_state == GAME_STATES[1]:
        print('\n you won!')
    if game_state == GAME_STATES[2]:
        print('\n game over!')


while game_state == GAME_STATES[0]:
    show_camp(mode='NORMAL')
    discover(ask_coordinates())
    game_state = check_game_state()
    clear_console()

end_game(game_state)
