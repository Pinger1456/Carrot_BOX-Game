# Carrot in a Box Game

"Carrot in a Box" is a fun bluffing game for two human players, inspired by a traditional game where players try to guess if an item (in this case, a carrot) is hidden in a box. This project is written in Python and provides a simple, interactive game experience in the console.

## Table of Contents

- [About the Game](#about-the-game)
- [Game Rules](#game-rules)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

## About the Game

In **Carrot in a Box**, two players are given boxes. One of these boxes has a carrot, and only one player gets to see inside their box. The player who peeks into their box can then choose to bluff by stating whether the carrot is inside or not. The second player must then decide if they want to swap boxes, and the goal is to end up with the box that contains the carrot.

## Game Rules

1. **Setup**: Each player receives a box — one red and one gold.
2. **Peeking**: Player 1 looks inside their box, while Player 2 keeps their eyes closed.
3. **Bluffing**: Player 1 can choose to bluff, stating whether they have the carrot in their box or not.
4. **Decision**: Player 2 then decides if they want to swap boxes with Player 1.
5. **Reveal**: The boxes are opened, and the winner is revealed based on who has the carrot.

## Features

- Interactive console prompts for easy gameplay.
- Simple and fun bluffing mechanics.
- Structured, modular codebase for easy modification and extension.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Pinger1456/Carrot_BOX-Game.git
   cd Carrot_BOX-Game
   ```

2. **Run the game**:
   Ensure you have Python 3 installed, then start the game with:
   ```bash
   python main.py
   ```

## Usage

1. Follow the console prompts to enter player names and start the game.
2. Player 1 will peek inside their box, and Player 2 will decide whether to swap boxes.
3. The game will reveal which player ends up with the carrot.

## Project Structure

Here's an overview of the files in the project:

- **main.py**: The entry point of the game, which initiates gameplay and orchestrates interactions between the other modules.
- **game.py**: Contains the `Game` class, which manages the main game logic, such as determining the carrot’s location and deciding the winner.
- **player.py**: Defines the `Player` class, representing each player in the game and holding their name.
- **display.py**: Manages all the console output, including prompts, game instructions, and the graphical display of the boxes.

## Future Improvements

Possible enhancements to the game could include:

- **Adding scoring**: Track multiple rounds and calculate the final winner based on total scores.
- **Multiplayer support**: Allow multiple rounds with different players joining in.
- **Graphical Interface**: Move from console-based to a graphical interface using a library like `pygame`.
- **Sound Effects**: Add sound effects to enhance the game experience.

## Credits

This game is based on the original idea by Al Sweigart, with modifications and extensions for improved modularity and interactive experience.

---

Enjoy playing Carrot in a Box, and may the best bluffer win!
```
