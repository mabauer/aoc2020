#!/usr/bin/env python3

import re
import os
import sys

class DirectedGraph:

    def __init__(self):
        # Example graph:
        # brightwhite +-(1)-> lightred
        #             +-(3)-> darkorange
        # {'brightwhite': {'lightred': 1, 'darkorange': 3}, {'lightred': {}}. {'darkorange': {}}}
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = {}

    def add_edge(self, node1, node2, weight=0):
        self.add_node(node1)
        self.add_node(node2)
        self.nodes[node1][node2] = weight

    def get_weight(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes[node1]:
            return self.nodes[node1][node2]
        else:
            return None

    def get_all_nodes(self):
        return [node for node in self.nodes] 

    # Not really needed, but useful for debugging purposes
    def get_all_edges(self):
        result = []
        for node in self.get_all_nodes():
            result += [(node, neighbour, self.get_weight(node, neighbour)) for neighbour in self.get_neighbours(node)]
        return result

    def get_neighbours(self, node):
        return [node for node in self.nodes[node]]

    def find_all_reachable_nodes(self, node, visited=set()):
        if not node in self.nodes:
            return visited
        for next in self.get_neighbours(node):
            if not next in visited: 
                visited.add(next)
                visited.union(self.find_all_reachable_nodes(next, visited))
        return visited

    # For debugging
    def __repr__(self):
        str = "{nodes}" 
        return str.format(nodes=self.nodes)


# Recursively count all inner bags (using the containment graph)
def count_all_bags_recursively(graph, bag):   
    if not bag in graph.get_all_nodes():
        return 0
    result = 1
    for inner_bag in graph.get_neighbours(bag):
        weight = graph.get_weight(bag, inner_bag)
        result = result + weight * count_all_bags_recursively(graph, inner_bag)
    return result

# Build directed graph: 
#   if use_contains == True, an edge from bag1 to bag2 means that bag1 contains number (=weight) bag2s
#   if use_contains == False, an edge from bag1 to bag2 indicates that number (=weight) bag2s are contained in bag1    
def build_graph_from_rules(input, use_contains=False):
    graph = DirectedGraph()
    for line in input:
        words = line.split()
        # words -> "light red bags contain..." 
        outer_bag = words[0] + words [1]
        # words[3] -> "contain"
        words = words[4:]
        while len(words) > 0:
            number = words[0]
            if number != "no":
                # words -> "1 bright white bag, 2 muted yellow bags.""
                inner_bag = words[1] + words[2]
                if use_contains:
                    # print("Adding edge (%s, %s)" % (inner_bag, outer_bag))
                    graph.add_edge(outer_bag, inner_bag, int(number))
                else:
                    # print("Adding edge (%s, %s)" % (inner_bag, outer_bag))
                    graph.add_edge(inner_bag, outer_bag, int(number))
                words = words[4:]
            else:
                # words -> "no other bags.""
                words = []
    # print(graph)
    return graph

def compute07(input):
    graph = build_graph_from_rules(input)
    result = len(graph.find_all_reachable_nodes("shinygold"))
    return result

def compute07b(input):
    graph = build_graph_from_rules(input, use_contains=True)
    result = count_all_bags_recursively(graph, "shinygold")-1
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input07.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 on the official input is %d" % (compute07(input)))
    print("The solution for part 2 on the official input is %d" % (compute07b(input)))

if __name__ == "__main__": 
    main()

