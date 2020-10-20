class tick_tack:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.step_counter = 0
        self.current_player = player1_name
        self.last_step_sign = ''
        self.game_field = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
            ]
        print(player1_name, ' - ходит первым, используя знак ', 'x')

    def step_o(self, coordinate_1, coordinate_2):
        self.game_field[coordinate_1][coordinate_2] = 'o'
        self.step_counter += 1
        self.last_step_sign = 'o'

    def step_x(self, coordinate_1, coordinate_2):
        self.game_field[coordinate_1][coordinate_2] = 'x'
        self.step_counter += 1
        self.last_step_sign = 'x'

    def check_end(self):
        example_of_end = [['x', 'x', 'x'], ['o', 'o', 'o']]
        current_field_string = ['', '', '']
        for string_number in range(3):
            if self.game_field[string_number] == example_of_end[0] or self.game_field[string_number] == example_of_end[1]:
                return 'end'
        for column_number in range(3):
            for string_number in range(3):
                current_field_string[string_number] = self.game_field[string_number][column_number]
            if current_field_string == example_of_end[0] or current_field_string == example_of_end[1]:
                return 'end'
        for string_number in range(3):
            current_field_string[string_number] = self.game_field[string_number][2-string_number]
        if current_field_string == example_of_end[0] or current_field_string == example_of_end[1]:
            return 'end'
        for string_number in range(3):
            current_field_string[string_number] = self.game_field[2-string_number][string_number]
        if current_field_string == example_of_end[0] or current_field_string == example_of_end[1]:
            return 'end'
        return 'continue'

    def who_won(self):
        if (self.check_end() == 'end') & (self.last_step_sign == 'x'):
            return self.player1
        elif (self.check_end() == 'end') & (self.last_step_sign == 'o'):
            return self.player2
        else:
            return 'nobody won'

    def print_game_field(self):
        for string_number in range(3):
            print(self.game_field[string_number])


if __name__ == '__main__':
    game = tick_tack('vasya', 'petya')
    game.print_game_field()
    game.step_x(0, 1)
    game.print_game_field()
    game.step_o(1, 2)
    game.print_game_field()
    game.step_x(1, 1)
    game.print_game_field()
    game.step_o(0, 2)
    game.print_game_field()
    game.step_x(2, 1)
    game.print_game_field()
    print(game.who_won())