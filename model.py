import random as rd


class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


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

    def discover(self, spot: Spot):
        pass
