# Description: This file contains the Janngi game piece class. This class creates game peice objects that can be used by
# the JanngiGame class in order to play Janngi.

class GamePiece:
    """This class creates game piece objects to be used in the JanggiGame. Each object holds a value for its current
    position, its piece type, and the name of the specific piece. There are get methods for each of the attributes, but
    but only a set method for position, because once the piece is created its piece type and name should not be changed.
    """

    def __init__(self, position, piece, name):
        """This method is the initializer that holds all the private data members. The position variable initializes the
        position of the piece on the board. The piece is initialized to hold what type of piece the object is. It
        is passed a string. The name variable initializes to the name of the specific piece. Should be the team and type
        of piece. It is passed a string. The name variable is also used for printing the piece to the board."""

        self._position = position
        self._piece = piece
        self._name = name

    def get_position(self):
        """This method returns the current board position of a piece"""
        return self._position

    def get_piece(self):
        """This method returns what type of piece the game piece object is"""
        return self._piece

    def get_name(self):
        """This method returns the specific name of the object piece"""
        return self._name

    def set_position(self, new_position):
        """This method sets the piece to a new position. It takes the new position as an argument and changes the
        position variable to the new position."""
        self._position = new_position
