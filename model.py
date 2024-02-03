import random as rd


class Spot:
    def __init__(self, spot_id: int, y_axis: int, x_axis: int, is_bomb: bool, is_discovered: bool):
        self.spot_id = spot_id
        self.y_axis = y_axis
        self.x_axis = x_axis
        self.is_bomb = is_bomb
        self.is_discovered = is_discovered
        self.touches_ids: list[int] = []


class Camp:
    def __init__(self, bomb_quantity: int, camp_size: int):
        self.bomb_quantity = bomb_quantity
        self.camp_size = camp_size
        self.bomb_ids: list[int] = []
        self.spots: list[Spot] = []

        self.generate_bomb_ids()
        self.generate_spots()
        self.generate_spot_touches()

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
                    is_discovered=False
                ))
                spot_id += 1

    def generate_spot_touches(self):
        for spot in self.spots:
            for colleague in self.spots:
                if abs(colleague.y_axis - spot.y_axis) <= 1 and abs(colleague.x_axis - spot.x_axis) <= 1:
                    spot.touches_ids.append(colleague.spot_id)
