class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return max(moves.count("L"), moves.count("R"))+moves.count("_") - min(moves.count("L"), moves.count("R"))
