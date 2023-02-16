from random import randint

from random import randint
def pencil_game(pencil_number: int, player: str) -> int:
    print("|" * pencil_number)
    print(f"{player}`s turn:")
    if player == "Jack":
        if pencil_number in boot_list:
            x = - 3
        elif pencil_number + 1 in boot_list:
            x =- 2
        elif pencil_number + 2 in boot_list:
            x= - 1
        elif pencil_number - 1 in boot_list:
            x= - randint(1, 3)
        #elif pencil_number == 1:
        else:
            x = - 1
        print(abs(x))
        return pencil_number_start +x
    else:
        while True:
            try:
                pencil_number_game = int(input(""))
                delta =pencil_number_start - pencil_number_game
                if pencil_number_game in range(1,4) and delta>=0:
                    return delta
                elif pencil_number_game not in range(1,4):
                    print("Possible values: '1', '2' or '3'")
                else:
                    print("Too many pencils were taken")
            except:
                print("Possible values: '1', '2' or '3'")

def get_pencil_number()-> int :
    while True:
        try:
            pencil_number_start = int(input("How many pencils would you like to use:"))
            if pencil_number_start > 0:
                return pencil_number_start
            elif pencil_number_start==0:
                print("The number of pencils should be positive")
            else:
                raise Exception
        except:
            print("The number of pencils should be numeric")

def get_first_player_name(names: tuple)-> int:
    while True:
        player_name = input(f"Who will be the first ({names[0]}, {names[1]}):\n")
        try:
            player_index = names.index(player_name)
            return player_index
        except:
            print(f"Choose between '{names[0]}' and '{names[1]}'")


if __name__ == "__main__":
    boot_list = [x * 4 for x in range(1, 200)]

    names = ("John","Jack")
    pencil_number_start= get_pencil_number()
    player_index = get_first_player_name(names)
    while pencil_number_start:
        pencil_number_start=pencil_game(pencil_number_start,names[player_index])
        if pencil_number_start<=0:
            break
        player_index^=1
    player_index ^= 1
    print(f"{names[player_index]} won!")
