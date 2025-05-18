# Treasure Hunter

A Python game that uses Depth-First Search (DFS) algorithm to find treasure in a maze-like environment.

## Game Description

In this game, a player (red square) automatically navigates through a grid to find a treasure (pulsing yellow square) using the DFS algorithm. The game visualizes how DFS works by showing:

-   Player's current position (red square)
-   Walls (gray squares)
-   Visited paths (blue squares)
-   Treasure location (pulsing yellow square)

The player starts from the top-left corner and tries to reach the treasure in the bottom-right corner, avoiding walls along the way.

## Features

-   Automatic pathfinding using DFS algorithm
-   Visual representation of the search process
-   Random wall generation
-   Path visualization
-   Smooth player movement
-   Pulsing treasure effect

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

-   Windows:

```bash
.\venv\Scripts\activate
```

-   Unix/MacOS:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Game

After setting up, you can run the game using:

```bash
python -m src.game
```

## Game Controls

-   The game runs automatically - no player input needed
-   Close the window or press Alt+F4 to exit the game

## Game Elements

-   🟥 Red Square: Player
-   🟨 Yellow Square (Pulsing): Treasure
-   ⬜ Gray Squares: Walls
-   🟦 Blue Squares: Visited paths

## Technical Details

-   Grid Size: 15x15 cells
-   Movement Speed: 500ms between moves
-   Wall Density: 20% of the grid
-   Algorithm: Depth-First Search (DFS)
-   Framework: Pygame

## Project Structure

```
treasure_hunter/
├── src/               # Source code
│   ├── __init__.py   # Package initialization
│   ├── game.py       # Main game logic and visualization
│   ├── grid.py       # Grid system and game board
│   └── pathfinder.py # DFS algorithm implementation
├── tests/             # Test files
│   └── __init__.py
├── venv/              # Virtual environment
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Dependencies

-   pygame==2.6.1 - Game framework
-   pytest==7.4.3 - Testing framework
-   black==23.11.0 - Code formatter
-   flake8==6.1.0 - Code linter

## How It Works

1. The game initializes a grid with random walls
2. The DFS algorithm starts from the player's position
3. For each step:
    - The algorithm explores possible moves
    - Marks visited cells
    - Backtracks when it reaches a dead end
    - Continues until it finds the treasure
4. The player follows the path found by DFS
5. The game ends when the player reaches the treasure

## Customization

You can modify these parameters in `src/game.py`:

-   Grid size: Change `width` and `height` in `TreasureHunter.__init__`
-   Movement speed: Adjust `move_delay` (in milliseconds)
-   Cell size: Modify `cell_size` for larger/smaller grid cells

In `src/grid.py`:

-   Wall density: Adjust `wall_density` parameter (0.0 to 1.0)
