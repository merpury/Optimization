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

############
# Main Functions
############

def read_map(map_fname):
    """
    Read map data from file.
    
    Args:
        map_fname: Name of map file
    
    Returns:
        Dictionary with location and transit information
    """
    towns = {}
    roads = {}
    
    with open(map_fname, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            
            city_part, rest = line.strip().split(";", 1)
            city, coords = city_part.split(":")
            city = city.strip()
            x, y = coords.split(",")
            towns[city] = (int(x), int(y))
            roads[city] = {}
            
            connections = rest.strip().split(",")
            for conn in connections:
                if ":" in conn:
                    dest, dist = conn.split(":")
                    roads[city][dest.strip()] = int(dist.strip())
    
    return {"location": towns, "transit": roads}

def P2_route(map_fname, start, goal):
    """
    Find route using breadth-first search algorithm.
    
    Args:
        map_fname: Name of map file
        start: Starting city name
        goal: Goal city name
    
    Returns:
        String representing the route path
    """
    romania_map = read_map(map_fname)
    prob = RoutingProblem(romania_map, initial=start, goal=goal)
    rst, scost = breadth_first_search(prob)
    
    if rst is None:
        return "No route found"
    
    soln = rst.path()
    route = ""
    for s in soln:
        route = s.state + " - " + route
    route = route[:-3].strip()
    return route