# Errors that are raised during the game's setup fase
class SetupError(Exception):
    pass

class UndefinedGame(SetupError):
    pass

# Errors that are raised during gameplay
class GameError(Exception):
    pass

class InvalidMove(GameError):
    pass

# Errors that come from the pieces files.
# This includes only invalid characteristics for the moment
class PieceError(Exception):
    pass

class InvalidRank(PieceError):
    pass

class InvalidFile(PieceError):
    pass

class InvalidColor(PieceError):
    pass