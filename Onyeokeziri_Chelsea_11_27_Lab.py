#Chelsea Onyeokeziri 1570698
player_dict = {}

sorted_list_keys = []

def sort_dict_keys():

    sorted_list_keys = sorted(player_dict.keys())

    return sorted_list_keys

def output_roster():

    sorted_list_keys = sort_dict_keys()

    print("ROSTER")

    for i in sorted_list_keys:


        print("Jersey number: " + str(i)

              + ", Rating: " + str(player_dict[i]))

def add_player():

    print("Enter a new player's jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a new player's jersey number:")

        jersey_num = int(input())


    print("Enter the player's rating:")

    player_rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter the player's rating:")

        player_rating = int(input())


    player_dict.update({jersey_num: player_rating})


def remove_player():

    print("Enter a jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a jersey number:")

        jersey_num = int(input())


    if jersey_num in player_dict.keys():
        del player_dict[jersey_num]


def update_player():

    print("Enter a jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter a jersey number:")

        jersey_num = int(input())

    print("Enter a new rating for player:")

    player_rating = int(input())


    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter a new rating for player:")

        player_rating = int(input())

    player_dict[jersey_num] = player_rating


def output_player_above_rating():

    print("Enter a rating:")

    rating = int(input())

    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter a rating:")

        rating = int(input())

    print("ABOVE", rating)


    sorted_list_keys = sort_dict_keys()

    for i in sorted_list_keys:

        if (player_dict[i] > rating):

            print("Jersey number: " + str(i)

                  + ", Rating: " + str(player_dict[i]))


for i in range(1, 6):


    print("Enter player " + str(i) + "'s jersey number:")

    jersey_num = int(input())

    while ((jersey_num < 0) or (jersey_num > 99)):
        print("Invalid Jersey Number! Please " +

              "enter again!")

        print("Enter player " + str(i)

              + "'s jersey number:")

        jersey_num = int(input())


    print("Enter player " + str(i) + "'s rating:")

    player_rating = int(input())


    while ((player_rating < 1) or (player_rating > 9)):
        print("Invalid Rating! Please enter again!")

        print("Enter player " + str(i) + "'s rating:")

        player_rating = int(input())

    print()

    player_dict[jersey_num] = player_rating

output_roster()

print()


while (True):


    print("MENU")

    print("a - Add player")

    print("d - Remove player")

    print("u - Update player rating")

    print("r - Output players above a rating")

    print("o - Output roster")

    print("q - Quit")

    print()


    print("Choose an option:")

    user_choice = input()

    if (user_choice == 'a'):

        add_player()


    elif (user_choice == 'd'):

        remove_player()


    elif (user_choice == 'u'):

        update_player()


    elif (user_choice == 'r'):

        output_player_above_rating()


    elif (user_choice == 'o'):

        output_roster()


    elif (user_choice == 'q'):

        break

    print()