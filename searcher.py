#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Adrian
# email: amtang@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ constructor
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        """ adds new states to self.states
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """ returns True if the called Searcher should add state 
            to its list of untested states, and False otherwise.
        """
        if self.depth_limit != -1:
            if state.num_moves > self.depth_limit:
                return False
        if state.creates_cycle():
            return False
        return True
        
    def add_states(self, new_states):
        """ processes the elements of new_states one at a time
        """
        for i in new_states:
            if self.should_add(i) == True:
                self.add_state(i)
        
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        self.add_state(init_state)
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None # failure


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ perform breadth-first search (BFS) instead of random search
        inherits from Searcher class
    """
    def next_state(self):
        if len(self.states) > 0:
            min_depth = min(State.num_moves for State in self.states)
            for s in self.states:
                if s.num_moves == min_depth:
                    self.states.remove(s)
                    # self.num_tested += 1
                    return s
        return None
    
class DFSearcher(Searcher):
    """ perform depth-first search (DFS) instead of random search
        inherits from Searcher class
    """
    def next_state(self):
        if len(self.states) > 0:
            max_depth = max(State.num_moves for State in self.states)
            reverse = self.states[::-1]
            for s in reverse:
                if s.num_moves == max_depth:
                    self.states.remove(s)
                    self.num_tested += 1
                    return s
        return None


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    """ computes and returns an estimate of how many additional
        moves are needed to get from state to the goal state
    """
    return state.board.num_misplaced()

def h2(state):
    """ Heuristic function that finds distance between tile and goal
        through using the pythagoren theorem
    """
    distance = 0
    board = state.board.tiles
    for r in range(3):
        for c in range(3):
            tile = board[r][c]
            if tile != '0':
                for i in range(3):
                    for j in range(3):
                        if GOAL_TILES[i][j] == tile:
                            distance += ((r-i) ** 2 + (c-j) ** 2) ** 0.5
    return distance
    



### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """constructor"""
        super().__init__(-1)
        self.heuristic = heuristic
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def add_state(self, state):
        """ the method should add a sublist that is a [priority, state] pair,
            where priority is the priority of state that is determined by 
            calling the priority method
        """
        priority = self.priority(state)
        Searcher.add_state(self, [priority, state])
        
    def next_state(self):
        """ This version of next_state should choose one of the states 
            with the highest priority.
        """
        if len(self.states) > 0:
            max_prio = max(state[0] for state in self.states)
            for state in self.states:
                if state[0] == max_prio:
                    self.states.remove(state)
                    self.num_tested += 1
                    return state[1]
        return None
    



### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    def __init__(self, heuristic):
        """constructor"""
        super().__init__(heuristic)
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
    









