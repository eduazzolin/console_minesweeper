from model import *
from model import Colors


class Main:
    def __init__(self, CAMP_SIZE: int = 9, BOMB_QUANTITY: int = 10):
        """
        The main class

        :param CAMP_SIZE: the amount of rows in the camp
        :param BOMB_QUANTITY: the amount of bombs in the camp
        :atributes COVERED_SYMBOL: the symbol to show a covered spot
        :atributes BOMB_SYMBOL: the symbol to show a bomb
        :atributes game_state: the state of the game [WIN, GAME_OVER, RUNNING]
        :atributes camp: the camp object
        :atributes range_camp_size: the range of the camp size
        :atributes view_y_axis: the labels for the y axis
        :atributes view_x_axis: the labels for the x axis
        """
        self.CAMP_SIZE = CAMP_SIZE
        self.BOMB_QUANTITY = BOMB_QUANTITY
        self.COVERED_SYMBOL = f'{Colors.B_GRAY}{Colors.F_BLACK} + {Colors.RESET}'
        self.BOMB_SYMBOL = f'{Colors.B_RED}{Colors.F_WHITE} * {Colors.RESET}'

        self.game_state = 'RUNNING'
        self.camp = Camp(self.BOMB_QUANTITY, self.CAMP_SIZE)
        self.range_camp_size = range(0, self.CAMP_SIZE)
        self.view_y_axis = [str(i + 1) for i in self.range_camp_size]
        self.view_x_axis = [chr(i + 65) for i in self.range_camp_size]

    def show_camp(self, mode: str = 'NORMAL'):
        """
        Print the camp in the console

        :param mode: the mode to show the camp [NORMAL, ID]
        """
        print(f'\n     {"  ".join(self.view_x_axis)}\n')
        for y in self.range_camp_size:
            print(f'{self.view_y_axis[y]}    ', end="")
            for x in self.range_camp_size:
                spot = [spot for spot in self.camp.spots if spot.y_axis == y if spot.x_axis == x][0]
                if spot.is_covered:
                    if mode == 'NORMAL':
                        print(self.COVERED_SYMBOL, end="")
                    if mode == 'ID':
                        print(
                            f'{Colors.F_RED if spot.is_bomb else ""}{spot.spot_id:02}{Colors.RESET if spot.is_bomb else ""}',
                            end=" ")
                else:
                    if spot.is_bomb:
                        print(self.BOMB_SYMBOL, end="")
                    else:
                        print(
                            f'{Colors.NEIGHBOUR_BOMBS_COLORS[spot.neighbours_bombs]}{Colors.F_BLACK} {spot.neighbours_bombs} {Colors.RESET}',
                            end="")

            print()

    @staticmethod
    def clear_console():
        """
        Clear the console

        """
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


    def ask_coordinates(self):
        """
        Ask the user for the coordinates and return the spot
        :return: the spot that the user wants to discover
        """
        while True:
            try:
                coordinates = input('\nEnter the coordinates, for example, A1: ')
                coordinate_x = self.view_x_axis.index(coordinates[:1].upper())
                coordinate_y = self.view_y_axis.index(coordinates[1:2])
                return self.camp.get_spot(coordinate_x, coordinate_y)
            except Exception as e:
                print('Invalid coordinates!')

    def discover(self, spot: Spot):
        """
        Discover a spot and its neighbours if it is a zero

        :param spot: the spot to be discovered
        """
        spot = self.camp.discover_spot(spot)
        if spot.neighbours_bombs == 0:
            self.camp.discover_neighbour_zeroes(spot)

    def check_game_state(self):
        """
        Check if the game is over or if the player won
        # WIN: all the spots that are not bombs are discovered
        # GAME_OVER: a bomb is discovered
        # RUNNING: the game is still running

        :return: the game state
        """
        for spot in self.camp.spots:
            if spot.is_bomb and not spot.is_covered:
                return 'GAME_OVER'

        for spot in self.camp.spots:
            if not spot.is_bomb and spot.is_covered:
                return 'RUNNING'

        return 'WIN'  # WIN

    def end_game(self, game_state):
        """
        Reveal the camp and print a message when the game is over

        :param game_state: WIN or GAME_OVER
        """
        print('\n\n')
        self.camp.reveal_camp()
        self.show_camp()

        if game_state == 'WIN':
            print('\n you won!')
        if game_state == 'GAME_OVER':
            print('\n game over!')

if __name__ == '__main__':
    main = Main(CAMP_SIZE=9, BOMB_QUANTITY=10)

    while main.game_state == 'RUNNING':
        main.show_camp(mode='NORMAL')
        main.discover(main.ask_coordinates())
        main.game_state = main.check_game_state()
        main.clear_console()

    main.end_game(main.game_state)
