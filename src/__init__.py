"""
Treasure Hunter main package.
A game that uses DFS to find treasure in a maze.
"""

from .game import TreasureHunter, main
from .grid import Grid
from .pathfinder import DFSPathfinder

__all__ = ['TreasureHunter', 'Grid', 'DFSPathfinder', 'main'] 