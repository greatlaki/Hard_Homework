'''
Стартовые требования.

Есть класс Банкомат у него есть
* Словарь с купюрами вида: {номинал: количество, . . . }
* Ф-ция выдачи, то есть мы вызываем эту ф-цию Банкомат.ф-ия(сумма) и нам выводит словарь с купюрами равными этой сумме.
Например:
Ввели 485
Вывело {100:3, 50:3, 20:1, 10:1, 5:1}

Продвинутые требования:

Разработать алгоритм расчета оставшихся купюр так что бы в банкомате их оставалось
оптимальное количество(примерно одинаковое количество номиналов)

Максимальные требования:

Интегрировать в наш банкомат счета пользователей.
Авторизацию.
Процент снимаемый банком.
Разные валюты.
И ± все возможности обычных банкоматов.

Бонусом.

Добавить интерфейс с помощью любых библиотек.
Добавить инкассаторов, то есть добавить возможность наполнять и очищать банкомат.
Выбор языка интерфейса.
Деньги выдаются с задержкой в зависимости от суммы.
Добавить блокировку аккаунта с возможностью разблокировки.
Если пинкод введён задом наперед - тревожная кнопка, аккаунт блокируется.
Возможность смены пароля.
Если пинкод вводится дольше 10 сек - аккаунт блокируется.
Любые нештяки которые придумаете.
'''


class Atm:
    cash_in_atm = {
        1000: 100,
        500: 100,
        200: 100,
        100: 100,
        50: 100,
        20: 100,
        10: 100,
        5: 100,
        1: 100,
    }
    clients = {
        5555: {
            'password': 1111,
            'account': 12000,
            'name': 'Vasia'
        },
        4444: {
            'password': 2222,
            'account': 1200,
            'name': 'Petia'
        },
    }

    def __init__(self, number_card) -> None:
        self.number_card = number_card
        self.__verification()

    def __command(self) -> None:
        print('Command:\n'
              '1. .withdrawal(cash) - withdraw money\n'
              '2. .check_balance() - display your balance\n'
              '3. .change_password() - create new password')

    def __verification(self) -> None:
        '''Function that verifying the card number and password for authenticity'''
        if self.number_card in self.clients:
            self.__check_password()
        else:
            print('This card is not valid!')
            self.number_card = int(input('Please, insert a valid card.\n'))
            return self.__verification()

    def __check_password(self) -> None:
        '''Function proof password'''

        self.passward = int(input('Enter the password: '))

        if self.passward == self.clients[self.number_card]['password']:
            print(f'Welcome, Dear {self.clients[self.number_card]["name"]}!')

        else:
            print('Password is incorrect!\nPlease, enter correct password.')
            return self.__check_password()

    def withdrawal(self, cash: int) -> None:
        '''Function allows you to withdraw money from the card!'''

        nominal_cash = {}
        save_cash = cash
        if self.__proof_enough_cash_Atm(cash) and self.__proof_enough_balance(cash):

            for key_nominal, value_nominal in self.cash_in_atm.items():

                if cash >= key_nominal and self.cash_in_atm[key_nominal] > 0:
                    count_nominal = cash // key_nominal
                    self.cash_in_atm[key_nominal] -= count_nominal
                    nominal_cash[key_nominal] = count_nominal
                    cash %= key_nominal

            self.clients[self.number_card]['account'] -= save_cash
            print(f"Success!  Withdrawal by {save_cash} denomination {nominal_cash}.")
            self.check_balance()

        self.__command()

    def __proof_enough_balance(self, cash: int) -> bool:
        if cash <= self.clients[self.number_card]['account']:
            return True
        else:
            print("There are not enough cash in the account.")
            return False

    def __proof_enough_cash_Atm(self, cash: int) -> bool:
        if cash <= self.__check_cash_in_atm():
            return True
        else:
            print("There are not enough cash in the ATM.")
            return False

    def __check_cash_in_atm(self) -> int:
        proof_cash = 0
        for key_nominal, value_nominal in self.cash_in_atm.items():
            proof_cash += key_nominal * value_nominal
        return proof_cash

    def check_balance(self) -> None:
        print(f'Your balance is {self.clients[self.number_card]["account"]}.')

    def change_password(self) -> None:
        self.__check_password()
        new_password = int(input('Enter new password: '))
        self.clients[self.number_card]["password"] = new_password


card = Atm(5555)     # password 1111
card.withdrawal(2247)

