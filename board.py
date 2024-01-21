#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Adrian
# email: amtang@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                i = 3*r + c
                self.tiles[r][c] = digitstr[i]
                if digitstr[i] == '0':
                    self.blank_c = c
                    self.blank_r = r
            

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of a Board object
        """
        board = ''
        for r in range(3):
            for c in range(3):
                i = 3*r + c
                if self.tiles[r][c] != '0':
                    board += self.tiles[r][c]
                else: 
                    board += '_'
                if c == 2:
                    board += '\n'
                elif str(i) not in '258':
                    board += ' '
        return board
        
    def move_blank(self, direction):
        """ modify the contents of the called Board object accordingly
        """
        if direction == 'up':
            new_r,new_c = self.blank_r -1,self.blank_c
        elif direction == 'down':
            new_r,new_c = self.blank_r +1,self.blank_c
        elif direction == 'left':
            new_r,new_c = self.blank_r,self.blank_c - 1
        elif direction == 'right':
            new_r,new_c = self.blank_r,self.blank_c + 1
        else:
            return False
        if new_r < 0 or new_r > 2 or new_c < 0 or new_c > 2:
            return False
        old = self.tiles[new_r][new_c]
        self.tiles[new_r][new_c] = '0'
        #swap _
        self.tiles[self.blank_r][self.blank_c] = old
        #swap number
        self.blank_r,self.blank_c = new_r,new_c
        return True
        #establish new blank coord
        
    def digit_string(self):
        """ returns a string of digits that corresponds to the current 
            contents of the called Board object’s tiles attribute
        """
        dgstr = ''
        for r in range(3):
            for c in range(3):
                dgstr += self.tiles[r][c]
        return dgstr
        
    def copy(self):
        """ deep copy of the called object
        """
        new_board = Board(self.digit_string())
        return new_board
    
    def num_misplaced(self):
        """ returns the number of tiles in the called Board object
            that are not where they should be in the goal state
        """
        misplaced = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    if self.tiles[r][c] != '0':
                        misplaced += 1
        return misplaced
                  
    def __eq__(self, other):
        """ can be called when the == operator is 
            used to compare two Board objects
        """
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != other.tiles[r][c]:
                    return False
        return True
    
    
        
        
        
        
        
        
        
        
        
        
        