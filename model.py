import random as rd


class Colors:
    # https://github.com/eduazzolin/python_ansi_color_sheethttps://github.com/eduazzolin/python_ansi_color_sheet

    # Variables for ANSI escape codes for font colors
    F_RED = '\033[38;2;255;0;0m'
    F_GREEN = '\033[38;2;0;255;0m'
    F_BLUE = '\033[38;2;0;0;255m'
    F_YELLOW = '\033[38;2;255;255;0m'
    F_PURPLE = '\033[38;2;128;0;128m'
    F_ORANGE = '\033[38;2;255;165;0m'
    F_CUSTOM = '\033[38;2;211;211;211m'  # Custom color (e.g., light gray)
    F_CYAN = '\033[38;2;0;255;255m'
    F_PINK = '\033[38;2;255;192;203m'
    F_BROWN = '\033[38;2;139;69;19m'
    F_GRAY = '\033[38;2;128;128;128m'
    F_BLACK = '\033[38;2;0;0;0m'
    F_WHITE = '\033[38;2;255;255;255m'
    F_MAROON = '\033[38;2;128;0;0m'
    F_OLIVE = '\033[38;2;128;128;0m'
    F_TEAL = '\033[38;2;0;128;128m'
    F_NAVY = '\033[38;2;0;0;128m'
    F_SILVER = '\033[38;2;192;192;192m'
    F_GOLD = '\033[38;2;255;215;0m'
    F_INDIGO = '\033[38;2;75;0;130m'
    F_ORCHID = '\033[38;2;218;112;214m'
    F_DARKGREEN = '\033[38;2;0;100;0m'
    F_TURQUOISE = '\033[38;2;64;224;208m'
    F_FIREBRICK = '\033[38;2;178;34;34m'
    F_SEASHELL = '\033[38;2;255;245;238m'

    # Variables for ANSI escape codes for background colors
    B_RED = '\033[48;2;255;0;0m'
    B_GREEN = '\033[48;2;0;255;0m'
    B_BLUE = '\033[48;2;0;0;255m'
    B_YELLOW = '\033[48;2;255;255;0m'
    B_PURPLE = '\033[48;2;128;0;128m'
    B_ORANGE = '\033[48;2;255;165;0m'
    B_CUSTOM = '\033[48;2;211;211;211m'  # Custom color (e.g., light gray)
    B_CYAN = '\033[48;2;0;255;255m'
    B_PINK = '\033[48;2;255;192;203m'
    B_BROWN = '\033[48;2;139;69;19m'
    B_GRAY = '\033[48;2;230;230;230m'
    B_BLACK = '\033[48;2;0;0;0m'
    B_WHITE = '\033[48;2;255;255;255m'
    B_MAROON = '\033[48;2;128;0;0m'
    B_OLIVE = '\033[48;2;128;128;0m'
    B_TEAL = '\033[48;2;0;128;128m'
    B_NAVY = '\033[48;2;0;0;128m'
    B_SILVER = '\033[48;2;192;192;192m'
    B_GOLD = '\033[48;2;255;215;0m'
    B_INDIGO = '\033[48;2;75;0;130m'
    B_ORCHID = '\033[48;2;218;112;214m'
    B_DARKGREEN = '\033[48;2;0;100;0m'
    B_TURQUOISE = '\033[48;2;64;224;208m'
    B_FIREBRICK = '\033[48;2;178;34;34m'
    B_SEASHELL = '\033[48;2;255;245;238m'

    # Variables for ANSI escape codes for text effects
    ITALIC = '\033[3m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    RESET = '\033[0m'

    NEIGHBOUR_BOMBS_COLORS = {
        0: B_WHITE,
        1: '\033[48;2;179;255;179m',
        2: '\033[48;2;255;255;153m',
        3: '\033[48;2;255;191;128m',
        4: '\033[48;2;255;133;102m',
        5: '\033[48;2;255;133;102m',
        6: '\033[48;2;255;133;102m',
        7: '\033[48;2;255;133;102m',
        8: '\033[48;2;255;133;102m',
    }



class Spot:
    def __init__(self, spot_id: int, y_axis: int, x_axis: int, is_bomb: bool, is_covered: bool = True):
        self.spot_id = spot_id
        self.y_axis = y_axis
        self.x_axis = x_axis
        self.is_bomb = is_bomb
        self.is_covered = is_covered
        self.neighbours_ids: list[int] = []
        self.neighbours_bombs: int = 0
        self.neighbours_zeroes_ids: list[int] = []


class Camp:
    def __init__(self, bomb_quantity: int, camp_size: int):
        self.bomb_quantity = bomb_quantity
        self.camp_size = camp_size
        self.bomb_ids: list[int] = []
        self.spots: list[Spot] = []

        self.generate_bomb_ids()
        self.generate_spots()
        self.generate_neighbours_ids()
        self.generate_neighbours_zeroes_ids()

    def generate_bomb_ids(self):
        bomb_locations_temp = set()
        while len(bomb_locations_temp) < self.bomb_quantity:
            bomb_locations_temp.add(rd.randint(1, (self.camp_size ** 2)))
        self.bomb_ids = list(bomb_locations_temp)

    def generate_spots(self):
        spot_id = 1
        for y_axis in range(0, self.camp_size):
            for x_axis in range(0, self.camp_size):
                self.spots.append(Spot(
                    spot_id=spot_id,
                    y_axis=y_axis,
                    x_axis=x_axis,
                    is_bomb=True if spot_id in self.bomb_ids else False,
                ))
                spot_id += 1

    def generate_neighbours_ids(self):
        for spot in self.spots:
            for neighbour in self.spots:
                if (
                        abs(neighbour.y_axis - spot.y_axis) <= 1 and
                        abs(neighbour.x_axis - spot.x_axis) <= 1 and
                        neighbour.spot_id != spot.spot_id
                ):
                    spot.neighbours_ids.append(neighbour.spot_id)
                    if neighbour.is_bomb: spot.neighbours_bombs += 1

    def generate_neighbours_zeroes_ids(self):
        for spot in self.spots:
            for neighbour in self.spots:
                if neighbour.spot_id in spot.neighbours_ids and neighbour.neighbours_bombs == 0:
                    spot.neighbours_zeroes_ids.append(neighbour.spot_id)

    def discover_spot(self, spot: Spot):
        spot.is_covered = False
        return spot


    def discover_neighbour_zeroes(self, spot: Spot):
        sid = spot.spot_id
        if len(spot.neighbours_zeroes_ids) > 0:
            neighbour_spots_zeroes = [neighbour for neighbour in self.spots if
                                      neighbour.spot_id in spot.neighbours_zeroes_ids if
                                      neighbour.is_covered]
            for neighbour in neighbour_spots_zeroes:
                self.discover_spot(neighbour)
                self.discover_neighbour_zeroes(neighbour)

    def reveal_camp(self):
        for spot in self.spots:
            spot.is_covered = False
