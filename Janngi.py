# Description: This file contains contains the class which checks move logic, a players turns, and if a player has won.
# The JanggiGame class creates a board and holds all the logic for the Janggi game. The Janggi Game class uses the
# GamePiece class to initialize and create the game piece objects used to play the game. Janggi is Korean Chess and this
# file holds all the logic needed to play the game.

from GamePiece import GamePiece


class JanggiGame:
    """This class holds the board and all the rules for Korean Chess, also known as Janggi. The class does not create
    the pieces and relies on the class GamePiece to create the piece objects. The class creates the game pieces using
    GamePiece and stores them all within this class as private data members. This class also has methods for making
    moves, the move rules of each piece, checking the game state, checking if the either team is in check and many
    helper functions."""

    def __init__(self):
        """This method holds all the private data members. It holds the board which is represented by a list of lists.
        This method also initializes by creating them and assigning them to a private data member. The board is also
        initialized here as well. It also holds two separate lists that hold all the game piece objects of the different
        teams that are still in play. It is initialized with all pieces in play. Lastly it has a private data member
        holding an integer that keeps track of players turns, and some constants that represent game states."""

        self._board = [["RedChariot", "RedElephant", "RedHorse", "RedGuard", "        ",
                        "RedGuard", "RedElephant", "RedHorse", "RedChariot"],
                       ["        ", "        ", "        ", "        ", "RedGeneral",
                        "        ", "        ", "        ", "        "],
                       ["        ", "RedCannon", "        ", "        ", "        ",
                        "        ", "        ", "RedCannon", "        "],
                       ["RedSoldier", "        ", "RedSoldier", "        ",
                        "RedSoldier", "        ", "RedSoldier", "        ", "RedSoldier"],
                       ["        ", "        ", "        ", "        ", "        ",
                        "        ", "        ", "        ", "        "],
                       ["        ", "        ", "        ", "        ",
                        "        ", "        ", "        ", "        ", "        "],
                       ["BlueSoldier", "        ", "BlueSoldier", "        ",
                        "BlueSoldier", "        ", "BlueSoldier", "        ", "BlueSoldier"],
                       ["        ", "BlueCannon", "        ", "        ", "        ",
                        "        ", "        ", "BlueCannon", "        "],
                       ["        ", "        ", "        ", "        ", "BlueGeneral",
                        "        ", "        ", "        ", "        "],
                       ["BlueChariot", "BlueElephant", "BlueHorse", "BlueGuard", "        ",
                        "BlueGuard", "BlueElephant", "BlueHorse", "BlueChariot"]]
        self._red_general = GamePiece([1, 4], "General", "RedGeneral")
        self._red_chariot1 = GamePiece([0, 0], "Chariot", "RedChariot")
        self._red_chariot2 = GamePiece([0, 8], "Chariot", "RedChariot")
        self._red_elephant1 = GamePiece([0, 1], "Elephant", "RedElephant")
        self._red_elephant2 = GamePiece([0, 6], "Elephant", "RedElephant")
        self._red_horse1 = GamePiece([0, 2], "Horse",  "RedHorse")
        self._red_horse2 = GamePiece([0, 7], "Horse", "RedHorse")
        self._red_guard1 = GamePiece([0, 3], "Guard", "RedGuard")
        self._red_guard2 = GamePiece([0, 5], "Guard", "RedGuard")
        self._red_cannon1 = GamePiece([2, 1], "Cannon", "RedCannon")
        self._red_cannon2 = GamePiece([2, 7], "Cannon", "RedCannon")
        self._red_soldier1 = GamePiece([3, 0], "Soldier", "RedSoldier")
        self._red_soldier2 = GamePiece([3, 2], "Soldier", "RedSoldier")
        self._red_soldier3 = GamePiece([3, 4], "Soldier", "RedSoldier")
        self._red_soldier4 = GamePiece([3, 6], "Soldier", "RedSoldier")
        self._red_soldier5 = GamePiece([3, 8], "Soldier", "RedSoldier")
        self._blue_general = GamePiece([8, 4], "General", "BlueGeneral")
        self._blue_chariot1 = GamePiece([9, 0], "Chariot", "BlueChariot")
        self._blue_chariot2 = GamePiece([9, 8], "Chariot", "BlueChariot")
        self._blue_elephant1 = GamePiece([9, 1], "Elephant", "BlueElephant")
        self._blue_elephant2 = GamePiece([9, 6], "Elephant", "BlueElephant")
        self._blue_horse1 = GamePiece([9, 2], "Horse", "BlueHorse")
        self._blue_horse2 = GamePiece([9, 7], "Horse", "BlueHorse")
        self._blue_guard1 = GamePiece([9, 3], "Guard", "BlueGuard")
        self._blue_guard2 = GamePiece([9, 5], "Guard", "BlueGuard")
        self._blue_cannon1 = GamePiece([7, 1], "Cannon", "BlueCannon")
        self._blue_cannon2 = GamePiece([7, 7], "Cannon", "BlueCannon")
        self._blue_soldier1 = GamePiece([6, 0], "Soldier", "BlueSoldier")
        self._blue_soldier2 = GamePiece([6, 2], "Soldier", "BlueSoldier")
        self._blue_soldier3 = GamePiece([6, 4], "Soldier", "BlueSoldier")
        self._blue_soldier4 = GamePiece([6, 6], "Soldier", "BlueSoldier")
        self._blue_soldier5 = GamePiece([6, 8], "Soldier", "BlueSoldier")
        self._red_pieces = [self._red_general, self._red_chariot1, self._red_chariot2,
                            self._red_elephant1, self._red_elephant2, self._red_horse1,
                            self._red_horse2, self._red_guard1, self._red_guard2,
                            self._red_cannon1, self._red_cannon2, self._red_soldier1,
                            self._red_soldier2, self._red_soldier3, self._red_soldier4,
                            self._red_soldier5]
        self._blue_pieces = [self._blue_general, self._blue_chariot1, self._blue_chariot2,
                             self._blue_elephant1, self._blue_elephant2, self._blue_horse1,
                             self._blue_horse2, self._blue_guard1, self._blue_guard2,
                             self._blue_cannon1, self._blue_cannon2, self._blue_soldier1,
                             self._blue_soldier2, self._blue_soldier3, self._blue_soldier4,
                             self._blue_soldier5]
        self._player_turn = 3
        self._unfinished = "UNFINISHED"
        self._red_won = "RED_WON"
        self._blue_won = "BLUE_WON"

    def print_board(self):
        """This method prints out each row of the game board as a list when called."""
        for val in self._board:
            print(val)

    def make_move(self, current_pos, new_pos):
        """This method takes the current position of a piece as the first argument and then position the piece should
        be moved to as the second argument. It takes the letter and number string values and turns them into numbers
        to match the integer values of the board grid. It then validates if the values are within the board range.
        Next the method decides the turn and validate if the piece to be moved is from the correct player. If it is, the
        method calls the method corresponding to the piece type in order to see if the move is a valid move for that
        piece type. It then checks to see if the move would cause a check to the players own general and it checks to
        see if an enemy piece should be removed. Returns true if any the move is valid and False if it was not. Nothing
        changes for a False move and the player must go again. If the game has finished and a player has won the method
        will always return false as no more moves can be played."""

        if self.is_checkmate() is True:
            return False

        # taking the strings given for moves and turning them into integers to use
        # initialize the coordinate variables
        current_col = None
        current_row = None
        new_row = None
        new_col = None
        if len(current_pos) == 3:
            current_col = current_pos[0]
            current_row = current_pos[1] + current_pos[2]
        if len(current_pos) == 2:
            current_col = current_pos[0]
            current_row = current_pos[1]
        # value of the current space expressed in a integer coordinate format
        current_space = [int(current_row) - 1, self.letter_converter(current_col)]
        if len(new_pos) == 2:
            new_col = new_pos[0]
            new_row = new_pos[1]
        if len(new_pos) == 3:
            new_col = new_pos[0]
            new_row = new_pos[1] + new_pos[2]
        # value of the new space expressed in a integer coordinate format
        new_space = [int(new_row) - 1, self.letter_converter(new_col)]

        # Making sure each move is within range of the board
        if current_space[0] < 0 or current_space[0] > 9:
            return False
        if current_space[1] < 0 or current_space[1] > 8:
            return False
        if new_space[0] < 0 or new_space[0] > 9:
            return False
        if new_space[1] < 0 or new_space[1] > 8:
            return False

        # blue player moves
        if self._player_turn % 2 != 0:
            if self.position_search(self._red_pieces, current_space) is True:  # making sure not calling red piece
                return False
            if self.position_search(self._blue_pieces, current_space) is False:  # making sure space is held by blue
                return False
            if current_space == new_space:  # used if the player doesn't want to move their pieces for their turn
                if self.is_in_check("blue") is False:
                    self._player_turn += 1
                    return True
            # making sure not being moved to same position as team piece
            if self.position_search(self._blue_pieces, new_space) is True:
                return False

            # finding and using the logic of piece type, to see if move is valid for that piece
            move_piece = self.return_object(self._blue_pieces, current_space)
            if move_piece.get_piece() == "General":
                if self.move_blue_palace_piece(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Chariot":
                if self.move_chariot(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Elephant":
                if self.move_elephant(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Horse":
                if self.move_horse(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Guard":
                if self.move_blue_palace_piece(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Cannon":
                if self.move_cannon(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Soldier":
                if self.move_blue_soldier(current_space, new_space) is False:
                    return False

            # updating the piece current space / eliminating any team pieces
            temp_space = None
            if self.position_search(self._red_pieces, new_space) is True:  # checking to see if opposing piece is there
                temp_space = self.return_object(self._red_pieces, new_space)  # saving in case of check
                self._red_pieces.remove(temp_space)
            move_piece.set_position(new_space)
            if self.is_in_check("blue") is True:  # if the move exposes the own players general, makes invalid.
                move_piece.set_position(current_space)
                if temp_space is not None:
                    self._red_pieces.append(temp_space)
                return False
            self._board[current_space[0]][current_space[1]] = "        "
            self._board[move_piece.get_position()[0]][move_piece.get_position()[1]] = move_piece.get_name()
            if self.is_checkmate() is True:
                return True
            self._player_turn += 1
            return True

        # red player moves
        if self._player_turn % 2 == 0:
            if self.position_search(self._blue_pieces, current_space) is True:  # making sure not calling blue piece
                return False
            if self.position_search(self._red_pieces, current_space) is False:  # making sure space is held by red
                return False
            if current_space == new_space:  # used if the player doesn't want to move their pieces for their turn
                if self.is_in_check("red") is False:
                    self._player_turn += 1
                    return True
            # making sure not being moved to same position as team piece
            if self.position_search(self._red_pieces, new_space) is True:
                return False

            # finding and using the logic of piece type, to see if move is valid for that piece
            move_piece = self.return_object(self._red_pieces, current_space)
            if move_piece.get_piece() == "General":
                if self.move_red_palace_piece(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Chariot":
                if self.move_chariot(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Elephant":
                if self.move_elephant(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Horse":
                if self.move_horse(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Guard":
                if self.move_red_palace_piece(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Cannon":
                if self.move_cannon(current_space, new_space) is False:
                    return False
            if move_piece.get_piece() == "Soldier":
                if self.move_red_soldier(current_space, new_space) is False:
                    return False

            # updating the piece current space / eliminating any team piece
            temp_space = None
            if self.position_search(self._blue_pieces, new_space) is True:  # checking to see if opposing piece is there
                temp_space = self.return_object(self._blue_pieces, new_space)  # saving in case of check
                self._blue_pieces.remove(temp_space)
            move_piece.set_position(new_space)
            if self.is_in_check("red") is True:    # if the move exposes the own players general, makes invalid.
                move_piece.set_position(current_space)
                if temp_space is not None:
                    self._blue_pieces.append(temp_space)
                return False
            self._board[current_space[0]][current_space[1]] = "        "
            self._board[move_piece.get_position()[0]][move_piece.get_position()[1]] = move_piece.get_name()
            if self.is_checkmate() is True:
                return True
            self._player_turn += 1
            return True

    def is_checkmate(self):
        """This method first checks to see if either player is in check. If not it returns False.
        If either player is in check it will then go through a list of possible moves for that team to see if there is a
         way to end the check. If there is not a move to be made the the function will return True, indicating there is
         a checkmate. If there is not a checkmate for either team the method will return False."""

        if self.is_in_check("blue") is False and self.is_in_check("red") is False:
            return False

        if self.is_in_check("blue") is True:
            for piece in self._blue_pieces:
                for val in range(10):
                    for space in range(9):
                        current_pos = piece.get_position()
                        new_pos = [val, space]
                        # runs through every piece type
                        if piece.get_piece() == "General":
                            if self.move_blue_palace_piece(current_pos, new_pos) is True:
                                if self.position_search(self._blue_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("blue") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Chariot":
                            if self.move_chariot(current_pos, new_pos) is True:
                                if self.position_search(self._blue_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("blue") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Elephant":
                            if self.move_elephant(current_pos, new_pos) is True:
                                if self.position_search(self._blue_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("blue") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Horse":
                            if self.move_horse(current_pos, new_pos) is True:
                                if self.position_search(self._blue_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("blue") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Guard":
                            if self.move_blue_palace_piece(current_pos, new_pos) is True:
                                if self.position_search(self._blue_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("blue") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Cannon":
                            if self.move_cannon(current_pos, new_pos) is True:
                                if self.position_search(self._blue_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("blue") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Soldier":
                            if self.move_blue_soldier(current_pos, new_pos) is True:
                                if self.position_search(self._blue_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("blue") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False

        if self.is_in_check("red") is True:
            for piece in self._red_pieces:
                for val in range(10):
                    for space in range(9):
                        current_pos = piece.get_position()
                        new_pos = [val, space]
                        if piece.get_piece() == "General":
                            if self.move_red_palace_piece(current_pos, new_pos) is True:
                                if self.position_search(self._red_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("red") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Chariot":
                            if self.move_chariot(current_pos, new_pos) is True:
                                if self.position_search(self._red_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("red") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Elephant":
                            if self.move_elephant(current_pos, new_pos) is True:
                                if self.position_search(self._red_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("red") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Horse":
                            if self.move_horse(current_pos, new_pos) is True:
                                if self.position_search(self._red_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("red") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Guard":
                            if self.move_red_palace_piece(current_pos, new_pos) is True:
                                if self.position_search(self._red_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("red") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Cannon":
                            if self.move_cannon(current_pos, new_pos) is True:
                                if self.position_search(self._red_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("red") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False
                        if piece.get_piece() == "Soldier":
                            if self.move_red_soldier(current_pos, new_pos) is True:
                                if self.position_search(self._red_pieces, new_pos) is False:
                                    yes_no = 0
                                    piece.set_position(new_pos)
                                    if self.is_in_check("red") is False:
                                        yes_no += 1
                                    piece.set_position(current_pos)
                                    if yes_no == 1:
                                        return False

        return True

    def get_game_state(self):
        """This method returns the current state of the game. If red has won it returns RED WON, if blue has won it
        returns BLUE_WON, and if the game is still going it returns UNFINISHED. Initialized to unfinished"""

        if self.is_checkmate() is True:
            if self._player_turn % 2 == 0:
                return self._red_won
            if self._player_turn % 2 != 0:
                return self._blue_won
        else:
            return self._unfinished

    def is_in_check(self, color):
        """This method takes a player color, red or blue as an argument. It then returns True if that player's general
        is currently in check. It returns False otherwise. The method checks the current possibility of an opposing
         piece moving to the current position of the general. It does this by running the generals current position
         through the methods for each piece's valid move logic."""

        if color.lower() == "red":
            general = self.find_general(self._red_pieces)
            # runs through every remaining piece in the opposing list to see if they have move to hit general
            for val in self._blue_pieces:
                piece_type = val.get_piece()
                piece_pos = val.get_position()
                if piece_type == "General":
                    if self.move_blue_palace_piece(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Chariot":
                    if self.move_chariot(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Elephant":
                    if self.move_elephant(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Horse":
                    if self.move_horse(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Guard":
                    if self.move_blue_palace_piece(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Cannon":
                    if self.move_cannon(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Soldier":
                    if self.move_blue_soldier(piece_pos, general.get_position()) is True:
                        return True

        if color.lower() == "blue":
            general = self.find_general(self._blue_pieces)
            # runs through every remaining piece in the opposing list to see if they have move to hit general
            for val in self._red_pieces:
                piece_type = val.get_piece()
                piece_pos = val.get_position()
                if piece_type == "General":
                    if self.move_red_palace_piece(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Chariot":
                    if self.move_chariot(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Elephant":
                    if self.move_elephant(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Horse":
                    if self.move_horse(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Guard":
                    if self.move_red_palace_piece(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Cannon":
                    if self.move_cannon(piece_pos, general.get_position()) is True:
                        return True
                if piece_type == "Soldier":
                    if self.move_red_soldier(piece_pos, general.get_position()) is True:
                        return True
        return False

    def move_red_soldier(self, soldier_space, move_space):
        """This method is used to see if a move by a RedSoldier is a valid move. It takes the soldiers current place,
        and the position it should be moved to as arguments. If the move is valid the method will return True. If the
        move is not valid it will return False. The method first checks to see piece is within the palace and if a
        diagonal move is possible. It then checks every other possible move."""

        # moves if in the palace
        if self.in_palace(soldier_space) is True:
            if self.in_palace(move_space) is True:
                if soldier_space == [7, 3] and move_space == [8, 4]:
                    return True
                if soldier_space == [7, 5] and move_space == [8, 4]:
                    return True
                if soldier_space == [8, 4] and move_space == [9, 3]:
                    return True
                if soldier_space == [8, 4] and move_space == [9, 5]:
                    return True
        # moves outside the palace
        if move_space[0] - soldier_space[0] < 0:
            return False
        if move_space[0] - soldier_space[0] > 1:
            return False
        if abs(move_space[1] - soldier_space[1]) > 1:
            return False
        if move_space[0] - soldier_space[0] != 0 and move_space[1] - soldier_space[1] != 0:
            return False
        return True

    def move_blue_soldier(self, soldier_space, move_space):
        """This method is used to see if a move by a BlueSoldier is a valid move. It takes the soldiers current place,
        and the position it should be moved to as arguments. If the move is valid the method will return True. If the
        move is not valid it will return False. The method first checks to see piece is within the palace and if a
        diagonal move is possible. It then checks every other possible move."""

        # moves in the palace
        if self.in_palace(soldier_space) is True:
            if self.in_palace(move_space) is True:
                if soldier_space == [2, 3] and move_space == [1, 4]:
                    return True
                if soldier_space == [2, 5] and move_space == [1, 4]:
                    return True
                if soldier_space == [1, 4] and move_space == [0, 3]:
                    return True
                if soldier_space == [1, 4] and move_space == [0, 5]:
                    return True
        # moves outside the palace
        if soldier_space[0] - move_space[0] < 0:
            return False
        if soldier_space[0] - move_space[0] > 1:
            return False
        if abs(move_space[1] - soldier_space[1]) > 1:
            return False
        if move_space[0] - soldier_space[0] != 0 and move_space[1] - soldier_space[1] != 0:
            return False
        return True

    def move_red_palace_piece(self, palace_space, move_space):
        """This method is used to see if a move by a Red Guard or Red General is a valid move. It takes the guard or
        general's current place, and the position it should be moved to as arguments. If the move is valid the method
        will return True. If the move is not valid it will return False. The method first checks to see piece is within
        the palace and then makes sure any movement is valid."""

        if self.in_palace(move_space) is False:
            return False
        if palace_space == [2, 3] and move_space == [1, 4]:
            return True
        if palace_space == [2, 5] and move_space == [1, 4]:
            return True
        if palace_space == [0, 3] and move_space == [1, 4]:
            return True
        if palace_space == [0, 5] and move_space == [1, 4]:
            return True
        if palace_space == [1, 4] and move_space == [0, 3]:
            return True
        if palace_space == [1, 4] and move_space == [0, 5]:
            return True
        if palace_space == [1, 4] and move_space == [2, 3]:
            return True
        if palace_space == [1, 4] and move_space == [2, 5]:
            return True
        if move_space[0] - palace_space[0] != 0 and move_space[1] - palace_space[1] != 0:
            return False
        if abs(move_space[1] - palace_space[1]) > 1:
            return False
        if abs(move_space[0] - palace_space[0]) > 1:
            return False
        return True

    def move_blue_palace_piece(self, palace_space, move_space):
        """This method is used to see if a move by a Blue Guard or Blue General is a valid move. It takes the guard or
        general's current place, and the position it should be moved to as arguments. If the move is valid the method
        will return True. If the move is not valid it will return False. The method first checks to see piece is within
        the palace and then makes sure any movement is valid."""

        if self.in_palace(move_space) is False:
            return False
        if palace_space == [7, 3] and move_space == [8, 4]:
            return True
        if palace_space == [7, 5] and move_space == [8, 4]:
            return True
        if palace_space == [9, 3] and move_space == [8, 4]:
            return True
        if palace_space == [9, 5] and move_space == [8, 4]:
            return True
        if palace_space == [8, 4] and move_space == [9, 3]:
            return True
        if palace_space == [8, 4] and move_space == [9, 5]:
            return True
        if palace_space == [8, 4] and move_space == [7, 3]:
            return True
        if palace_space == [8, 4] and move_space == [7, 5]:
            return True
        if move_space[0] - palace_space[0] != 0 and move_space[1] - palace_space[1] != 0:
            return False
        if abs(move_space[1] - palace_space[1]) > 1:
            return False
        if abs(move_space[0] - palace_space[0]) > 1:
            return False
        return True

    def move_chariot(self, chariot_space, move_space):
        """This method is used to see if a move by a chariot is a valid move. It takes the chariot's current place, and
        the position it should be moved to as arguments. If the move is valid the method will return True. If the move
        is not valid it will return False."""

        # moves inside the palace
        if self.in_palace(chariot_space) is True:
            if self.in_palace(move_space) is True:
                if self.occupy_space([1, 4]) is False:
                    if chariot_space == [2, 3] and move_space == [0, 5]:
                        return True
                    if chariot_space == [0, 5] and move_space == [2, 3]:
                        return True
                    if chariot_space == [2, 5] and move_space == [0, 3]:
                        return True
                    if chariot_space == [0, 3] and move_space == [2, 5]:
                        return True
                if self.occupy_space([8, 4]) is False:
                    if chariot_space == [7, 3] and move_space == [9, 5]:
                        return True
                    if chariot_space == [9, 5] and move_space == [7, 3]:
                        return True
                    if chariot_space == [7, 5] and move_space == [9, 3]:
                        return True
                    if chariot_space == [9, 3] and move_space == [7, 5]:
                        return True
                if chariot_space == [2, 3] and move_space == [1, 4]:
                    return True
                if chariot_space == [2, 5] and move_space == [1, 4]:
                    return True
                if chariot_space == [0, 3] and move_space == [1, 4]:
                    return True
                if chariot_space == [0, 5] and move_space == [1, 4]:
                    return True
                if chariot_space == [1, 4] and move_space == [0, 3]:
                    return True
                if chariot_space == [1, 4] and move_space == [0, 5]:
                    return True
                if chariot_space == [1, 4] and move_space == [2, 3]:
                    return True
                if chariot_space == [1, 4] and move_space == [2, 5]:
                    return True
                if chariot_space == [7, 3] and move_space == [8, 4]:
                    return True
                if chariot_space == [7, 5] and move_space == [8, 4]:
                    return True
                if chariot_space == [9, 3] and move_space == [8, 4]:
                    return True
                if chariot_space == [9, 5] and move_space == [8, 4]:
                    return True
                if chariot_space == [8, 4] and move_space == [9, 3]:
                    return True
                if chariot_space == [8, 4] and move_space == [9, 5]:
                    return True
                if chariot_space == [8, 4] and move_space == [7, 3]:
                    return True
                if chariot_space == [8, 4] and move_space == [7, 5]:
                    return True

        # moves outside the palace
        if (move_space[0] - chariot_space[0]) != 0 and (move_space[1] - chariot_space[1]) != 0:
            return False
        # moves vertically
        if move_space[0] - chariot_space[0] != 0:
            if abs(move_space[0] - chariot_space[0]) != 1:
                if move_space[0] > chariot_space[0]:
                    for space in range(chariot_space[0] + 1, move_space[0]):
                        if self.occupy_space([space, move_space[1]]) is True:
                            return False
                if move_space[0] < chariot_space[0]:
                    for space in range(move_space[0] + 1, chariot_space[0]):
                        if self.occupy_space([space, move_space[1]]) is True:
                            return False
        # moves horizontally
        if move_space[1] - chariot_space[1] != 0:
            if abs(move_space[1] - chariot_space[1]) != 1:
                if move_space[1] > chariot_space[1]:
                    for space in range(chariot_space[1] + 1, move_space[1]):
                        if self.occupy_space([move_space[0], space]) is True:
                            return False
                if move_space[1] < chariot_space[1]:
                    for space in range(move_space[1] + 1, chariot_space[1]):
                        if self.occupy_space([move_space[0], space]) is True:
                            return False
        return True

    def move_cannon(self, cannon_space, move_space):
        """This method is used to see if a move by a cannon is a valid move. It takes the cannon's current place, and
        the position it should be moved to as arguments. If the move is valid the method will return True. If the move
        is not valid it will return False."""

        jump_count = 0  # keeps track if there is more than one object until destination space
        if self.cannon_check(move_space) is True:
            return False
        # moves within the palace
        if self.in_palace(cannon_space) is True:
            if self.in_palace(move_space) is True:
                if self.occupy_space([1, 4]) is True:
                    if cannon_space == [2, 3] and move_space == [0, 5]:
                        if self.cannon_check([1, 4]) is True:
                            return False
                        return True
                    if cannon_space == [0, 5] and move_space == [2, 3]:
                        if self.cannon_check([1, 4]) is True:
                            return False
                        return True
                    if cannon_space == [0, 3] and move_space == [2, 5]:
                        if self.cannon_check([1, 4]) is True:
                            return False
                        return True
                    if cannon_space == [2, 5] and move_space == [0, 3]:
                        if self.cannon_check([1, 4]) is True:
                            return False
                        return True
                if self.occupy_space([8, 4]) is True:
                    if cannon_space == [7, 3] and move_space == [9, 5]:
                        if self.cannon_check([8, 4]) is True:
                            return False
                        return True
                    if cannon_space == [9, 5] and move_space == [7, 3]:
                        if self.cannon_check([8, 4]) is True:
                            return False
                        return True
                    if cannon_space == [9, 3] and move_space == [7, 5]:
                        if self.cannon_check([8, 4]) is True:
                            return False
                        return True
                    if cannon_space == [7, 5] and move_space == [9, 3]:
                        if self.cannon_check([8, 4]) is True:
                            return False
                        return True
        # moves outside the palace
        if (move_space[0] - cannon_space[0]) != 0 and (move_space[1] - cannon_space[1]) != 0:
            return False
        # moves that go vertically
        if move_space[0] - cannon_space[0] != 0:
            if abs(move_space[0] - cannon_space[0]) == 1:
                return False
            if move_space[0] > cannon_space[0]:
                for space in range(cannon_space[0] + 1, move_space[0]):
                    if self.occupy_space([space, move_space[1]]) is True:
                        if self.cannon_check([space, move_space[1]]) is True:
                            return False
                        jump_count += 1
            if move_space[0] < cannon_space[0]:
                for space in range(move_space[0] + 1, cannon_space[0]):
                    if self.occupy_space([space, move_space[1]]) is True:
                        if self.cannon_check([space, move_space[1]]) is True:
                            return False
                        jump_count += 1
        # moves that go horizontally
        if move_space[1] - cannon_space[1] != 0:
            if abs(move_space[1] - cannon_space[1]) == 1:
                return False
            if move_space[1] > cannon_space[1]:
                for space in range(cannon_space[1] + 1, move_space[1]):
                    if self.occupy_space([move_space[0], space]) is True:
                        if self.cannon_check([move_space[0], space]) is True:
                            return False
                        jump_count += 1
            if move_space[0] < cannon_space[0]:
                for space in range(move_space[0] + 1, cannon_space[0]):
                    if self.occupy_space([move_space[0], space]) is True:
                        if self.cannon_check([move_space[0], space]) is True:
                            return False
                        jump_count += 1
        if jump_count != 1:
            return False
        return True

    def move_horse(self, horse_space, move_space):
        """This method is used to see if a move by a horse is a valid move. It takes the horse's current place, and
        the position it should be moved to as arguments. If the move is valid the method will return True. If the move
        is not valid it will return False."""

        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [2, 1]:
            if self.occupy_space([horse_space[0] - 1, horse_space[1]]) is True:
                return False
            else:
                return True
        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [2, -1]:
            if self.occupy_space([horse_space[0] - 1, horse_space[1]]) is True:
                return False
            else:
                return True
        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [1, -2]:
            if self.occupy_space([horse_space[0], horse_space[1] + 1]) is True:
                return False
            else:
                return True
        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [-1, -2]:
            if self.occupy_space([horse_space[0], horse_space[1] + 1]) is True:
                return False
            else:
                return True
        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [1, 2]:
            if self.occupy_space([horse_space[0], horse_space[1] - 1]) is True:
                return False
            else:
                return True
        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [-1, 2]:
            if self.occupy_space([horse_space[0], horse_space[1] - 1]) is True:
                return False
            else:
                return True
        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [-2, 1]:
            if self.occupy_space([horse_space[0] + 1, horse_space[1]]) is True:
                return False
            else:
                return True
        if [horse_space[0] - move_space[0], horse_space[1] - move_space[1]] == [-2, -1]:
            if self.occupy_space([horse_space[0] + 1, horse_space[1]]) is True:
                return False
            else:
                return True
        return False

    def move_elephant(self, elephant_space, move_space):
        """This method is used to see if a move by a elephant is a valid move. It takes the elephant's current place,
        and the position it should be moved to as arguments. If the move is valid the method will return True. If the
        move is not valid it will return False."""

        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [2, -3]:
            if self.occupy_space([elephant_space[0], elephant_space[1] + 1]) is True:
                return False
            if self.occupy_space([elephant_space[0] - 1, elephant_space[1] + 2]) is True:
                return False
            else:
                return True
        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [-2, -3]:
            if self.occupy_space([elephant_space[0], elephant_space[1] + 1]) is True:
                return False
            if self.occupy_space([elephant_space[0] + 1, elephant_space[1] + 2]) is True:
                return False
            else:
                return True
        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [-3, -2]:
            if self.occupy_space([elephant_space[0] + 1, elephant_space[1]]) is True:
                return False
            if self.occupy_space([elephant_space[0] + 2, elephant_space[1] + 1]) is True:
                return False
            else:
                return True
        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [-3, 2]:
            if self.occupy_space([elephant_space[0] + 1, elephant_space[1]]) is True:
                return False
            if self.occupy_space([elephant_space[0] + 2, elephant_space[1] - 1]) is True:
                return False
            else:
                return True
        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [-2, 3]:
            if self.occupy_space([elephant_space[0], elephant_space[1] - 1]) is True:
                return False
            if self.occupy_space([elephant_space[0] + 1, elephant_space[1] - 2]) is True:
                return False
            else:
                return True
        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [2, 3]:
            if self.occupy_space([elephant_space[0], elephant_space[1] - 1]) is True:
                return False
            if self.occupy_space([elephant_space[0] - 1, elephant_space[1] - 2]) is True:
                return False
            else:
                return True
        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [3, 2]:
            if self.occupy_space([elephant_space[0] - 1, elephant_space[1]]) is True:
                return False
            if self.occupy_space([elephant_space[0] - 2, elephant_space[1] - 1]) is True:
                return False
            else:
                return True
        if [elephant_space[0] - move_space[0], elephant_space[1] - move_space[1]] == [3, -2]:
            if self.occupy_space([elephant_space[0] - 1, elephant_space[1]]) is True:
                return False
            if self.occupy_space([elephant_space[0] - 2, elephant_space[1] + 1]) is True:
                return False
            else:
                return True
        return False

    def position_search(self, obj_list, value):
        """A helper method that takes a list of pieces and a position on the board and returns true if a piece in the
        list is at currently at that position and returns false if there is not"""

        for val in obj_list:
            if val.get_position() == value:
                return True
        return False

    def occupy_space(self, pos):
        """A helper method takes a position as an argument and returns True if there is a piece on the board at that
        position and returns False if there is not. It scans both the red team list and blue team list to do this"""

        for val in self._blue_pieces:
            if val.get_position() == pos:
                return True
        for val in self._red_pieces:
            if val.get_position() == pos:
                return True
        return False

    def cannon_check(self, pos):
        """ A helper method that takes a position as an argument and returns True if there is a cannon piece currently
        at that position. If there is not, then it returns False"""

        for val in self._blue_pieces:
            if val.get_position() == pos:
                if val.get_piece() == "Cannon":
                    return True
        for val in self._red_pieces:
            if val.get_position() == pos:
                if val.get_piece() == "Cannon":
                    return True
        return False

    def return_object(self, obj_list, value):
        """Takes a list of pieces and a position and returns the piece object if the passed position is held by one of
        the game pieces in the list."""

        for val in obj_list:
            if val.get_position() == value:
                return val

    def find_general(self, obj_list):
        """This method is a helper method that takes a list of either the blue pieces or the red pieces and returns the
        general piece as an object."""

        for val in obj_list:
            if val.get_piece() == "General":
                return val

    def letter_converter(self, letter):
        """This method is a helper method. The method takes a string letter and converts the letter column address to an
        integer. It takes a letter a-i and converts it to its corresponding number. It then returns that corresponding
        number. If the letter is not in range, the method gives it the value of 10 (out of range integer)"""

        if letter.lower() == "a":
            letter = 0
            return letter
        if letter.lower() == "b":
            letter = 1
            return letter
        if letter.lower() == "c":
            letter = 2
            return letter
        if letter.lower() == "d":
            letter = 3
            return letter
        if letter.lower() == "e":
            letter = 4
            return letter
        if letter.lower() == "f":
            letter = 5
            return letter
        if letter.lower() == "g":
            letter = 6
            return letter
        if letter.lower() == "h":
            letter = 7
            return letter
        if letter.lower() == "i":
            letter = 8
            return letter
        else:
            letter = 10
            return letter

    def in_palace(self, current_pos):
        """Takes a position list and returns true if that position is in one of the palace positions and returns False
        if not"""

        if current_pos == [0, 3]:
            return True
        if current_pos == [0, 4]:
            return True
        if current_pos == [0, 5]:
            return True
        if current_pos == [1, 3]:
            return True
        if current_pos == [1, 4]:
            return True
        if current_pos == [1, 5]:
            return True
        if current_pos == [2, 3]:
            return True
        if current_pos == [2, 4]:
            return True
        if current_pos == [2, 5]:
            return True
        if current_pos == [7, 3]:
            return True
        if current_pos == [7, 4]:
            return True
        if current_pos == [7, 5]:
            return True
        if current_pos == [8, 3]:
            return True
        if current_pos == [8, 4]:
            return True
        if current_pos == [8, 5]:
            return True
        if current_pos == [9, 3]:
            return True
        if current_pos == [9, 4]:
            return True
        if current_pos == [9, 5]:
            return True
        else:
            return False
