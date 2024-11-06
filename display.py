"""This file responding for showing objects in the console"""


def display_intro():
    """Showing introducing"""
    print('''Carrot in a Box Game

This is a bluffing game for two players. Each player has a box.
One box has a carrot. To win, you need to have the box with the carrot.

Press Enter to begin...
''')


def display_boxes(player_names, first_box, second_box):
    """Display boxes"""
    print(f'''HERE ARE TWO BOXES:

 /         /|   /         /|
+---------+ |  +---------+ |
|  {first_box}  | |  |  {second_box}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
{player_names}
''')


def get_player_choice(player):
    """Picking choice"""
    print(f"{player.name}, do you want to swap boxes? (YES/NO)")
    while True:
        response = input('> ').upper()
        if response in ('YES', 'NO'):
            return response == 'YES'
        print(f"{player.name}, please enter 'YES' or 'NO'.")
