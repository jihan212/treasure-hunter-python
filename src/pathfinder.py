"""
DFS pathfinding algorithm for the Treasure Hunter game.
"""
from typing import List, Tuple, Set, Optional
from collections import deque

class DFSPathfinder:
    def __init__(self):
        self.path: deque[Tuple[int, int]] = deque()
        self.visited: Set[Tuple[int, int]] = set()
        
    def find_path(self, start: Tuple[int, int], 
                 get_valid_moves: callable,
                 is_goal: callable) -> Optional[List[Tuple[int, int]]]:
        """
        Find path using DFS algorithm.
        
        Args:
            start: Starting position
            get_valid_moves: Function that returns valid moves from a position
            is_goal: Function that checks if a position is the goal
            
        Returns:
            List of positions forming path to goal, or None if no path exists
        """
        self.visited = set()
        self.path = deque([start])
        
        if self._dfs(start, get_valid_moves, is_goal):
            return list(self.path)
        return None
        
    def _dfs(self, pos: Tuple[int, int],
             get_valid_moves: callable,
             is_goal: callable) -> bool:
        """
        Recursive DFS implementation.
        Returns True if path to goal is found.
        """
        self.visited.add(pos)
        
        if is_goal(pos):
            return True
            
        for next_pos in get_valid_moves(pos):
            if next_pos not in self.visited:
                self.path.append(next_pos)
                if self._dfs(next_pos, get_valid_moves, is_goal):
                    return True
                self.path.pop()
                
        return False 