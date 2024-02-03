from model import *


class Main:
    camp = Camp(10, 9)


    last_y = 0
    for spot in camp.spots:
        if spot.y_axis != last_y:
            print("")
            last_y = spot.y_axis
        print(f'{spot.spot_id:02}', end=" ")
