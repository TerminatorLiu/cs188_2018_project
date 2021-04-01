# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def dfs_(problem,state,action_stack,marked_state):
    marked_state.append(state)
    if problem.isGoalState(state):
        return True
    for child_state, action, cost in problem.expand(state):
        if child_state not in marked_state:
            action_stack.push(action)
            if(dfs_(problem,child_state,action_stack,marked_state)):
                return True
            else:
                action_stack.pop()
    return False

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    action_stack = util.Stack()
    marked_state = []
    dfs_(problem,problem.getStartState(),action_stack,marked_state)
    res = []
    while not action_stack.isEmpty():
        res.append(action_stack.pop())
    res.reverse()
    return res
    #print("Start:", problem.getStartState());
    
    "*** YOUR CODE HERE ***"

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    marked_state = []
    state_queue = util.Queue()
    state_queue.push([problem.getStartState(),[]])
    marked_state.append(problem.getStartState())
    while not state_queue.isEmpty():
        cur_state = state_queue.pop()
        if problem.isGoalState(cur_state[0]):
            return cur_state[1]
        else:
            for child_state, action, cost in problem.expand(cur_state[0]):
                if child_state not in marked_state:
                    marked_state.append(child_state)
                    temp = copy.deepcopy(cur_state[1])
                    temp.append(action)
                    state_queue.push([child_state,temp])
                   
    
    # util.raiseNotDefined()
def uniformCostSearch(problem):
    fringe = util.PriorityQueue()
    expended = []
    node_dic = {}
    fringe.push(problem.getStartState(),0)
    node_dic[problem.getStartState()] = [[],0]
    while not fringe.isEmpty():
        cur_state = fringe.pop()
        cur_priority = node_dic[cur_state][1]
        expended.append(cur_state)
        if problem.isGoalState(cur_state):
            return node_dic[cur_state][0]
        else:
            for child_state, action, cost in problem.expand(cur_state):
                if child_state not in expended:
                    if child_state not in node_dic:
                        fringe.push(child_state,cur_priority+cost)
                        temp = copy.deepcopy(node_dic[cur_state][0])
                        temp.append(action)
                        node_dic[child_state]=[temp,cur_priority+cost]
                    else:
                        fringe.update(child_state,cur_priority+cost)
                        if cur_priority+cost < node_dic[child_state][1]:
                            temp = copy.deepcopy(node_dic[cur_state][0])
                            temp.append(action)
                            node_dic[child_state]=[temp,cur_priority+cost]
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    fringe = util.PriorityQueue()
    expended = []
    node_dic = {}
    fringe.push(problem.getStartState(),heuristic(problem.getStartState(),problem))
    node_dic[problem.getStartState()] = [[],heuristic(problem.getStartState(),problem)]
    while not fringe.isEmpty():
        cur_state = fringe.pop()
        cur_priority = node_dic[cur_state][1]
        expended.append(cur_state)
        if problem.isGoalState(cur_state):
            return node_dic[cur_state][0]
        else:
            for child_state, action, cost in problem.expand(cur_state):
                if child_state not in expended:
                    if child_state not in node_dic:
                        fringe.push(child_state,cur_priority+cost+heuristic(cur_state,problem))
                        temp = copy.deepcopy(node_dic[cur_state][0])
                        temp.append(action)
                        node_dic[child_state]=[temp,cur_priority+cost+heuristic(cur_state,problem)]
                    else:
                        fringe.update(child_state,cur_priority+cost+heuristic(cur_state,problem))
                        if cur_priority+cost+heuristic(cur_state,problem) < node_dic[child_state][1]:
                            temp = copy.deepcopy(node_dic[cur_state][0])
                            temp.append(action)
                            node_dic[child_state]=[temp,cur_priority+cost+heuristic(cur_state,problem)]
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch
