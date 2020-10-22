class TickTackToe:
    """Класс для одной партии игры крестики-нолики с полем 3х3. Игроки ходят символами 'x' и 'o'. Начальная координата
    находится в точке (0, 0)

    Attributes
    ----------
    player1_name: имя первого игрока
    player2_name: имя второго игрока
    step_counter: счетчик ходов
    current_player: имя игрока, который сейчас ходит
    last_step_sign: символ, которым походил один из игроков
    game_field: игровое поле 3х3

    Methods
    -------
    step_o: походить знаком 'o'
    step_x: походить знаком 'x'
    check_end: говорит окончена ли игра
    who_won: говорит победителя, если игра закончена
    print_game_field: печатает игровое поле
    """
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.step_counter = 0
        self.current_player = player1_name
        self.last_step_sign = ''
        self.game_field = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
            ]
        print(player1_name, ' - ходит первым, используя знак x')

    def step_o(self, coordinate_1, coordinate_2):
        """ Ходит знаком 'o' в клетку с укзанными координатми и говорит, если ход сделать нельзя

        :param coordinate_1: номер строки
        :param coordinate_2: номер столбца
        :return: ничего
        """
        if self.last_step_sign != 'o':
            if self.game_field[coordinate_1][coordinate_2] == '':
                self.last_step_sign = 'o'
                self.game_field[coordinate_1][coordinate_2] = 'o'
                self.step_counter += 1
            else:
                print('В данной клетке уже поставлен ', self.game_field[coordinate_1][coordinate_2])
        else:
            print('Нельзя ходить два раза подряд.')

    def step_x(self, coordinate_1, coordinate_2):
        """Ходит знаком 'x' в клетку с укзанными координатми и говорит, если ход сделать нельзя

        :param coordinate_1: номер строки
        :param coordinate_2: номер столбца
        :return: ничего
        """
        if self.last_step_sign != 'x':
            if self.game_field[coordinate_1][coordinate_2] == '':
                self.last_step_sign = 'x'
                self.game_field[coordinate_1][coordinate_2] = 'x'
                self.step_counter += 1
            else:
                print('В данной клетке уже поставлен ', self.game_field[coordinate_1][coordinate_2])
        else:
            print('Нельзя ходить два раза подряд.')

    def check_end(self):
        """Проверяет окончена ли игра путем поиска трех одинаковых знаков, стоящих подряд, и проверки счетчика.

        :return: 'end' - возвращает, если игра окончена. 'continue' - возвращает, если игра не окончена.
        """
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
        """Возвращает имя игрока, который победил или строку 'nobody won'

        :return: 'nobody won', если никто не победил или имя победившего игрока.
        """
        if (self.check_end() == 'end') & (self.last_step_sign == 'x'):
            return self.player1_name
        elif (self.check_end() == 'end') & (self.last_step_sign == 'o'):
            return self.player2_name
        else:
            return 'nobody won'

    def print_game_field(self):
        """Печатает игровое поле

        :return: ничего
        """
        for string_number in range(3):
            print(self.game_field[string_number])


if __name__ == '__main__':
    game = TickTackToe('vasya', 'petya')
    game.step_x(0, 1)
    game.step_o(1, 2)
    game.print_game_field()
    game.step_x(1, 1)
    game.step_x(1, 1)
    game.step_o(0, 2)
    game.print_game_field()
    game.step_x(0, 1)
    game.step_x(2, 1)
    game.print_game_field()
    print(game.who_won())