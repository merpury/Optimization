
import bisect
import math
from random import random

# Constant
infinity = 1.0e400

############
# Classes (from SearchAUX2023)
############

class FIFOQueue():
    """A First-In-First-Out Queue."""
    def __init__(self):
        self.A = []; self.start = 0
        
    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)     

    def pop(self):    
        e = self.A[self.start]
        self.start += 1
        return e

    def is_empty(self):
        return self.__len__() == 0


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent is not None: 
            self.depth = parent.depth + 1
                    
    def path(self):
        x, result = self, [self]
        while x.parent is not None:
            result.append(x.parent)
            x = x.parent
        return result

    def expand(self, problem):
        return [Node(child, self, act,
            problem.path_cost(self.path_cost, self.state, act, child))
                for (act, child) in problem.successor(self.state)]

############
# Problem Classes (from SearchAUX2023)
############

class RoutingProblem:
    "The problem of searching a graph from one node to another."
    def __init__(self, local_map, initial, goal):
        self.map = local_map
        self.initial = initial
        self.goal = goal

    def successor(self, s):
        """
        Take s: current state/current town
        Return a list of (action, result/linked town) pairs.
        """
        return [(snext, snext) for snext in self.map['transit'][s].keys()]

    def path_cost(self, cost_to_s, s, action, snext):
        transit_cost = infinity
        if s in self.map["transit"]:
            if snext in self.map["transit"][s]:
                transit_cost = self.map["transit"][s][snext]
        return cost_to_s + transit_cost

    def goal_test(self, state):
        return state == self.goal

    def h(self, state):
        cx, cy = self.map["location"][state]
        gx, gy = self.map["location"][self.goal]
        # Squared Euclidean distance
        return math.sqrt( (cx - gx)**2 + (cy - gy)**2 )

############
# Search Functions (from SearchAUX2023)
############

def breadth_first_search(problem, show=False):
    fringe = FIFOQueue()
    fringe.append(Node(problem.initial))
    search_cost = 0

    reached = {}
    while not fringe.is_empty():
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node, search_cost
        if node.state not in reached:
            reached[node.state] = node
            fringe.extend(node.expand(problem))
            search_cost += 1
    return None, search_cost

towns ={'Arad': (91, 492), 'Bucharest': (400, 327), 'Craiova': (253, 288), \
    'Drobeta': (165, 299), 'Eforie': (562, 293), 'Fagaras': (305, 449), \
    'Giurgiu': (375, 270), 'Hirsova': (534, 350), 'Iasi': (473, 506), \
    'Lugoj': (165, 379), 'Mehadia': (168, 339), 'Neamt': (406, 537), \
    'Oradea': (131, 571), 'Pitesti': (320, 368), 'Rimnicu Vilcea': (233, 410), \
    'Sibiu': (207, 457), 'Timisoara': (94, 410), 'Urziceni': (456, 350), \
    'Vaslui': (509, 444), 'Zerind': (108, 531)}

roads = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
        'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
        'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Drobeta': {'Mehadia': 75, 'Craiova': 120},
        'Eforie': {'Hirsova': 86},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Giurgiu': {'Bucharest': 90},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
        'Neamt': {'Iasi': 87},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
        'Sibiu': {'Rimnicu Vilcea': 80, 'Arad': 140, 'Oradea': 151, 'Fagaras': 99},
        'Timisoara': {'Lugoj': 111, 'Arad': 118},
        'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98},
        'Vaslui': {'Iasi': 92, 'Urziceni': 142},
        'Zerind': {'Oradea': 71, 'Arad': 75} }

romania_map = {"location": towns, "transit": roads}

def P1_route(start, goal):
    prob = RoutingProblem(romania_map, initial=start, goal=goal)
    rst, scost = breadth_first_search(prob)
    
    if rst is None:
        return "No route found"
    
    soln = rst.path()
    route = ""
    for s in soln:
        route = s.state + ' - ' + route
    route = route[:-3].strip()
    return route

if __name__ == '__main__':

    start = input("Current town: ")
    goal = input("Destination: ")
    print(P1_route(start, goal))
    