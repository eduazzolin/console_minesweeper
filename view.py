


class View:
    pass

"""    def __init__(self, model: Model):
        self.model = model
        self.str_bomb_camp = self.generate_str_bomb_camp()
        self.range_camp_size = range(0, self.model.camp_size)
        self.y_axis = [str(i+1) for i in self.range_camp_size]
        self.x_axis = [chr(i+65) for i in self.range_camp_size]
    def generate_str_bomb_camp(self):
        str_rows = []
        for row in self.model.bomb_camp:
            str_rows.append([str(place) for place in row])
        return str_rows

    def show_camp(self):

        print(f'\n    {" ".join(self.x_axis)}\n')
        for i in self.range_camp_size:
            print(f'{self.y_axis[i]}   {" ".join(self.str_bomb_camp[i])}')"""
