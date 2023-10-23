from random import random
from functools import reduce
from queue import *
from collections import namedtuple
import numpy as np

PROBLEM_SIZE = 8
NUM_SETS = 8
State = namedtuple('State', ['taken', 'not_taken'])

def goal_check(state):
    return np.all(reduce(np.logical_or, [SETS[i] for i in state.taken], np.array([False for _ in range(PROBLEM_SIZE)])))

def main():

    SETS = tuple(np.array([ random()<.3 for _ in range(PROBLEM_SIZE) ]) for _ in range(NUM_SETS))
    
    assert goal_check(State(set(range(NUM_SETS)), set())), "Problem not solvable"


    frontier = LifoQueue()
    frontier.put(State(set(), set(range(NUM_SETS))))

    counter = 0
    current_state = frontier.get()
    while not goal_check(current_state):
        counter += 1
        for action in current_state[1]:
            new_state = State(current_state.taken ^ {action}, current_state.not_taken ^ {action})
            frontier.put(new_state)
        current_state = frontier.get()

    print(f"Solved in {counter:,} steps")

    print(f"current_state: {current_state}")
    print(f"current state goal check: {goal_check(current_state)}")
    

def test():
    #boolean_array = np.ndarray(10, dtype=bool)
    #print(boolean_array)

    PROBLEM_SIZE = 8
    NUM_SETS = 8

    SETS = tuple( np.array([ random()<.2 for _ in range(PROBLEM_SIZE) ]) for _ in range(NUM_SETS) )

    state = {'taken':{1,3,5}, 'not_taken':{0,2,4,6,7}}
    #print()
    #for i in state[0]:
    #    print(SETS[i])

    def goal_check(state): # tentando entender o que tá acontecendo com o italiano que nao cala a boca atras de mim
        check = np.all( reduce(
            np.logical_or, 
            [SETS[i] for i in state['taken']],
            np.array([False for _ in range(NUM_SETS)])
            ) 
        )
        return check
    #assert goal_check({ 'taken':set(range(NUM_SETS)), 'not_taken':set() }), 'Problem not solvable'

    frontier = PriorityQueue()
    frontier.put({'taken':set(), 'not_taken':set(range(NUM_SETS))})
    
    current_state = frontier.get()
    #if goal_check(current_state):
    #    print('!!!')
    
    counter = 0
    while not goal_check(current_state):
        counter += 1
        for action in current_state['not_taken']:
            new_state = {
                'taken':current_state['taken']^{action}, 
                'not_taken':current_state['not_taken']^{action}
                }
            frontier.put(new_state)
        current_state = frontier.get()
    print(f"Solved in {counter:,} steps")

if __name__ == '__main__':
    main()