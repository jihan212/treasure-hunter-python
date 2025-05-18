"""
Main game module for Treasure Hunter.
Implements the game loop and visualization using Pygame.
"""
import pygame
import sys
from typing import Optional, List, Tuple
from .grid import Grid
from .pathfinder import DFSPathfinder

class TreasureHunter:
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    
    def __init__(self, width: int = 15, height: int = 15, cell_size: int = 40):
        """Initialize the game."""
        pygame.init()
        
        # Game state
        self.grid = Grid(width, height)
        self.pathfinder = DFSPathfinder()
        self.current_path: Optional[List[Tuple[int, int]]] = None
        self.move_delay = 500  # milliseconds between moves
        self.last_move_time = 0
        
        # Display settings
        self.cell_size = cell_size
        self.screen_width = width * cell_size
        self.screen_height = height * cell_size
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Treasure Hunter - DFS Edition")
        
        # Find initial path
        self._find_path()
        
    def _find_path(self) -> None:
        """Find path to treasure using DFS."""
        self.current_path = self.pathfinder.find_path(
            self.grid.player_pos,
            self.grid.get_valid_moves,
            lambda pos: pos == self.grid.treasure_pos
        )
        
    def _draw_cell(self, pos: Tuple[int, int], color: Tuple[int, int, int]) -> None:
        """Draw a cell at the given position with the specified color."""
        x, y = pos
        rect = pygame.Rect(
            x * self.cell_size,
            y * self.cell_size,
            self.cell_size,
            self.cell_size
        )
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, self.BLACK, rect, 1)
        
    def _draw_grid(self) -> None:
        """Draw the game grid."""
        # Fill background
        self.screen.fill(self.WHITE)
        
        # Draw walls
        for wall in self.grid.walls:
            self._draw_cell(wall, self.GRAY)
            
        # Draw visited cells
        for visited in self.grid.visited:
            if visited not in self.grid.walls:
                self._draw_cell(visited, self.BLUE)
        
        # Draw treasure with pulsing effect
        treasure_color = self.YELLOW
        if pygame.time.get_ticks() % 1000 < 500:  # Simple pulse effect
            treasure_color = (255, 200, 0)
        self._draw_cell(self.grid.treasure_pos, treasure_color)
        
        # Draw player
        self._draw_cell(self.grid.player_pos, self.RED)
        
    def update(self) -> None:
        """Update game state."""
        current_time = pygame.time.get_ticks()
        
        # Move player along path
        if (self.current_path and 
            current_time - self.last_move_time >= self.move_delay):
            next_pos = self.current_path.pop(0)
            self.grid.move_player(next_pos)
            self.last_move_time = current_time
            
            # If path is exhausted, find new path
            if not self.current_path:
                self._find_path()
    
    def run(self) -> None:
        """Main game loop."""
        clock = pygame.time.Clock()
        
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Update game state
            self.update()
            
            # Draw everything
            self._draw_grid()
            pygame.display.flip()
            
            # Cap frame rate
            clock.tick(60)
            
            # Check win condition
            if self.grid.is_treasure_found():
                pygame.time.wait(1000)  # Show final state briefly
                pygame.quit()
                sys.exit()

def main():
    """Entry point for the game."""
    game = TreasureHunter()
    game.run()

if __name__ == "__main__":
    main() 