#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Adrian
# email: amtang@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
def process_file(filename, algorithm, param):
    num_puzzles = 0
    total_moves = 0
    total_states = 0
    
    for line in open(filename):
        puzzle = line.strip()
        board = Board(puzzle)
        state = State(board, None, 'init')
        
        if algorithm == 'random':
            searcher = Searcher(param)
        elif algorithm == 'BFS':
            searcher = BFSearcher(param)
        elif algorithm == 'DFS':
            searcher = DFSearcher(param)
        elif algorithm == 'Greedy':
            searcher = GreedySearcher(param)
        elif algorithm == 'A*':
            searcher = AStarSearcher(param)
        else:  
            print('unknown algorithm:', algorithm)
        solution = str(searcher.find_solution(state))
        if solution is not None:
            num_moves = solution.split("-")[-1]
            num_tested = searcher.num_tested
            print(puzzle+":",num_moves,"moves,",num_tested,"states tested")
            num_puzzles += 1
            total_moves += int(num_moves)
            total_states += int(num_tested)
            
    if num_puzzles > 0:
        avg_moves = total_moves / num_puzzles
        avg_states = total_states / num_puzzles
        print()
        print("solved",num_puzzles,"puzzles")
        print("averages:",avg_moves,"moves,",avg_states,"states tested")
    else:
        print("solved",num_puzzles,"puzzles")
            
        






