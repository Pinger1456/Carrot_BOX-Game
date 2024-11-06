"""This script initializes the game, gathers player information,
and manages the main game flow by interacting with the Game,
Player, and Display modules. It guides the players through
the game steps, including placing bets, viewing the boxes,
deciding whether to swap boxes, and determining the winner."""

from game import Game
from game import Player
from display import display_intro, display_boxes, get_player_choice


def main():
    """Display game introduction"""
    display_intro()
    input("Press Enter to continue...")

    # Get player names and initialize players
    p1_name = input("Player 1, enter your name: ")
    p2_name = input("Player 2, enter your name: ")
    player1 = Player(p1_name)
    player2 = Player(p2_name)

    # Initialize the game
    game = Game(player1, player2)

    # Display the boxes and get the player's choice
    display_boxes(f"{player1.name}    {player2.name}", "RED", "GOLD")
    if get_player_choice(player2):
        game.swap_boxes()

    # Determine and announce the winner
    winner = game.get_winner()
    print(f"The winner is {winner.name}!")
    print("Thanks for playing!")


if __name__ == '__main__':
    main()
