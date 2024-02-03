from model import *
from model import Colors

CAMP_SIZE: int = 9
BOMB_QUANTITY: int = 10
SEPARADOR = "  "
COVERED_SYMBOL = "*"
BOMB_SYMBOL = "💣"

game_over = False
camp = Camp(BOMB_QUANTITY, CAMP_SIZE)
range_camp_size = range(0, CAMP_SIZE)
view_y_axis = [str(i + 1) for i in range_camp_size]
view_x_axis = [chr(i + 65) for i in range_camp_size]


def show_camp():
    global spot
    print(f'\n     {"  ".join(view_x_axis)}\n')
    for y in range_camp_size:
        print(f'{view_y_axis[y]}    ', end="")
        for x in range_camp_size:
            spot = [spot for spot in camp.spots if spot.y_axis == y if spot.x_axis == x][0]
            if spot.is_covered:
                print(COVERED_SYMBOL, end=SEPARADOR)
            else:
                print(spot.neighbours_bombs)

        print()

def ask_coordinates():
    coordinates = input('Enter the coordinates, for example, A1: ')
    coordinate_x = view_x_axis.index(coordinates[:1])
    coordinate_y = view_y_axis.index(coordinates[1:2])
    spot = [spot for spot in camp.spots if spot.y_axis == coordinate_y if spot.x_axis == coordinate_x][0]
    camp.discover(spot)


while not game_over:
    show_camp()
    ask_coordinates()



print('\n\n\n')
last_y = 0
for spot in camp.spots:
    if spot.y_axis != last_y:
        print("")
        last_y = spot.y_axis
    print(f'{Colors.RED if spot.is_bomb else ""}{spot.neighbours_bombs:02}{Colors.ENDC if spot.is_bomb else ""}',
          end=" ")
