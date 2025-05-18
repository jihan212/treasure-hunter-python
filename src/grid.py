"""
Grid system for the Treasure Hunter game.
Handles the game board, walls, player position, and treasure location.
"""
import random
from typing import List, Tuple, Set

class Grid:
    def __init__(self, width: int, height: int, wall_density: float = 0.2):
        """
        Initialize the game grid.
        
        Args:
            width (int): Width of the grid
            height (int): Height of the grid
            wall_density (float): Percentage of cells that should be walls (0.0 to 1.0)
        """
        self.width = width
        self.height = height
        self.walls: Set[Tuple[int, int]] = set()
        self.player_pos = (0, 0)  # Start at top-left
        self.treasure_pos = (width - 1, height - 1)  # Place treasure at bottom-right
        self.visited: Set[Tuple[int, int]] = set()
        
        # Generate walls randomly
        self._generate_walls(wall_density)
        
        # Ensure start and end positions are not walls
        self.walls.discard(self.player_pos)
        self.walls.discard(self.treasure_pos)
        
        # Mark starting position as visited
        self.visited.add(self.player_pos)

    def _generate_walls(self, density: float) -> None:
        """Generate random walls in the grid."""
        num_walls = int(self.width * self.height * density)
        possible_positions = [(x, y) for x in range(self.width) 
                            for y in range(self.height)]
        wall_positions = random.sample(possible_positions, num_walls)
        self.walls = set(wall_positions)

    def get_valid_moves(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Return list of valid moves from current position."""
        x, y = pos
        possible_moves = [
            (x + 1, y),  # right
            (x - 1, y),  # left
            (x, y + 1),  # down
            (x, y - 1)   # up
        ]
        
        return [move for move in possible_moves
                if self.is_valid_position(move)]

    def is_valid_position(self, pos: Tuple[int, int]) -> bool:
        """Check if a position is valid (in bounds and not a wall)."""
        x, y = pos
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                pos not in self.walls)

    def move_player(self, new_pos: Tuple[int, int]) -> bool:
        """
        Move player to new position if valid.
        Returns True if move was successful.
        """
        if self.is_valid_position(new_pos):
            self.player_pos = new_pos
            self.visited.add(new_pos)
            return True
        return False

    def is_treasure_found(self) -> bool:
        """Check if player has found the treasure."""
        return self.player_pos == self.treasure_pos 