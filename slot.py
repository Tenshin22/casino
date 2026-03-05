# импорты
import random
import os


file_path_1 = "user_names.txt"
file_path_2 = "users_coins.txt"

if not os.path.exists(file_path_1) or not os.path.exists(file_path_2):
    open(file_path_1, mode="w", encoding="utf-8").close()
    open(file_path_2, mode="w", encoding="utf-8").close()


DEBUG = False

# списки
symbols = [
    "💎",
    "🍒",
    "🏆",
]
list_droppeds_symbols_1 = []
list_droppeds_symbols_2 = []
list_droppeds_symbols_3 = []


# выподение символов
def symbols_cosino(symbols, droppeds_symbols):
    number = 1
    while number <= 3:
        random_sheble = random.choice(symbols)
        droppeds_symbols.append(random_sheble)

        print(random_sheble, end=" ")

        number += 1
    print()

    return droppeds_symbols


# проверка на выйгрыш по гаризонтали
def check_on_win(droppeds_symbols):
    if (
        droppeds_symbols[0] == droppeds_symbols[1]
        and droppeds_symbols[0] == droppeds_symbols[2]
    ):
        coins = 20
    elif droppeds_symbols[0] == droppeds_symbols[1]:
        coins = 5
    elif droppeds_symbols[2] == droppeds_symbols[1]:
        coins = 5
    else:
        coins = 0

    return coins


# проверка на выйгрыш по диагонали
def check_diagonally(droppeds_symbols_1, droppeds_symbols_2, droppeds_symbols_3):
    if (
        droppeds_symbols_1[2] == droppeds_symbols_2[1]
        and droppeds_symbols_1[2] == droppeds_symbols_3[0]
    ):
        coins = 30
    elif (
        droppeds_symbols_1[0] == droppeds_symbols_2[1]
        and droppeds_symbols_1[0] == droppeds_symbols_3[2]
    ):
        coins = 30
    else:
        coins = 0

    return coins


# проверка на выйгрыш по вертикали
def check_vertically(droppeds_symbols_1, droppeds_symbols_2, droppeds_symbols_3):
    if (
        droppeds_symbols_1[0] == droppeds_symbols_2[0]
        and droppeds_symbols_1[0] == droppeds_symbols_3[0]
    ):
        coins = 25
    elif (
        droppeds_symbols_1[1] == droppeds_symbols_2[1]
        and droppeds_symbols_1[1] == droppeds_symbols_3[1]
    ):
        coins = 25
    elif (
        droppeds_symbols_1[2] == droppeds_symbols_2[2]
        and droppeds_symbols_1[2] == droppeds_symbols_3[2]
    ):
        coins = 25
    else:
        coins = 0

    return coins


def show_spin_result(coins):
    print(f"+{coins}💸")


# игра
def play(
    coins,
    symbols,
    list_droppeds_symbols_1,
    list_droppeds_symbols_2,
    list_droppeds_symbols_3,
    user_name,
):
    droppeds_symbols_1 = symbols_cosino(
        symbols, droppeds_symbols=list_droppeds_symbols_1
    )
    droppeds_symbols_2 = symbols_cosino(
        symbols, droppeds_symbols=list_droppeds_symbols_2
    )
    droppeds_symbols_3 = symbols_cosino(
        symbols, droppeds_symbols=list_droppeds_symbols_3
    )

    prize = check_on_win(droppeds_symbols=droppeds_symbols_1)
    show_spin_result(coins=prize)
    coins += prize
    prize = check_on_win(droppeds_symbols=droppeds_symbols_2)
    show_spin_result(coins=prize)
    coins += prize
    prize = check_on_win(droppeds_symbols=droppeds_symbols_3)
    show_spin_result(coins=prize)
    coins += prize

    prize = check_diagonally(droppeds_symbols_1, droppeds_symbols_2, droppeds_symbols_3)
    show_spin_result(coins=prize)
    coins += prize

    prize = check_vertically(droppeds_symbols_1, droppeds_symbols_2, droppeds_symbols_3)
    show_spin_result(coins=prize)
    coins += prize

    print(f"{user_name} у вас {coins}")

    return coins


# запись ника пользывателя
def recording_names(user_name, list_users_names):
    if user_name not in list_users_names:
        with open("user_names.txt", mode="a", encoding="utf-8") as f:
            user_name = user_name + "\n"
            f.write(user_name)
    else:
        return


# запись выйгрыша пользывателя
def recording_coins(coins, list_users_coins, list_users_names, user_name):

    if user_name not in list_users_names:
        with open("users_coins.txt", mode="a", encoding="utf-8") as f:
            coins = str(coins) + "\n"
            f.write(coins)
    else:
        coins_play = coins
        i = list_users_names.index(user_name)

        if DEBUG:
            print("индекс где находится имя:", i)
            print("list_users_coins", list_users_coins)
            print("list_users_coins", list_users_names)

        previous_coins = int(list_users_coins[i])

        if coins_play > previous_coins:
            coins_play = str(coins_play)

            list_users_coins[i] = coins_play
            print(list_users_coins)

            index = 0

            with open("users_coins.txt", mode="w", encoding="utf-8") as f:
                while index <= len(list_users_coins) - 1:
                    coins = list_users_coins[index] + "\n"
                    f.write(coins)

                    index += 1
        else:

            return


# открываем имена пользывателя
def get_users_names() -> list[str]:
    with open("user_names.txt", mode="r", encoding="utf-8") as f:
        temporary_list = f.readlines()

        list_users_names = []
        index = 0
        while index <= len(temporary_list) - 1:
            list_users_names.append(temporary_list[index].replace("\n", ""))

            index += 1

        return list_users_names


# открываем выйгрыш пользывателей
def get_users_coins() -> list[str]:
    with open("users_coins.txt", mode="r", encoding="utf-8") as f:
        temporary_list = f.readlines()

        print("temporary_list:", temporary_list)
        list_users_coins = []
        index = 0
        while index <= len(temporary_list) - 1:
            print("цикл работает")
            list_users_coins.append(temporary_list[index].replace("\n", ""))

            index += 1

        return list_users_coins


# переменные
coins = 50
COST = 15
end_reason = None  # "cashout" | "bust"


# пользыватель вводит свой ник
user_name = input("Введите свой ник: ")


# читаем фаил с именами и получаем их список
list_users_names: list[str] = get_users_names()


if user_name in list_users_names:
    print("Вы ветеран-лудаман")
else:
    print("Новичок не связывайся с казино")


# цикл игры
while True:
    list_droppeds_symbols_1.clear()
    list_droppeds_symbols_2.clear()
    list_droppeds_symbols_3.clear()

    # 1) Жёсткое правило: если денег меньше стоимости попытки — конец, меню не показываем
    if coins < COST:
        coins = 0  # по твоим правилам "всё потерял"
        end_reason = "bust"
        break

    cmd = input(f"Попытка {COST}💸. Enter — крутить, $ — забрать: ").strip()

    if cmd == "$":
        end_reason = "cashout"
        break

    if cmd != "":
        print("Нужно нажать Enter (крутить) или ввести $ (забрать).\n")
        continue

    coins -= COST
    coins = play(
        coins,
        symbols,
        list_droppeds_symbols_1,
        list_droppeds_symbols_2,
        list_droppeds_symbols_3,
        user_name,
    )

# 2) ЕДИНСТВЕННОЕ место финализации
if end_reason == "cashout":
    print(f"{user_name}, вы забрали выигрыш: {coins}")

    list_users_coins: list[str] = get_users_coins()
    recording_names(user_name, list_users_names)
    recording_coins(coins, list_users_coins, list_users_names, user_name)

elif end_reason == "bust":
    print(f"{user_name}, денег меньше {COST} — вы не успели забрать и потеряли")
