#!/usr/bin/env python3

import re
import os
import sys

class Graph:

    def __init__(self):
        self.nodes = {}

    def add_edge(self, node1, node2):
        if node1 in self.nodes:
            self.nodes[node1].append(node2)
        else:
            self.nodes[node1] = [node2]

    def find_all_reachable_nodes(self, node, visited=set()):
        if not node in self.nodes:
            return visited
        for next in self.nodes[node]:
            if not next in visited: 
                visited.add(next)
                visited.union(self.find_all_reachable_nodes(next, visited))
        return visited
        

    # For debugging
    def __repr__(self):
        str = "{nodes}" 
        return str.format(nodes=self.nodes)

    
def build_graph(input):
    graph = Graph()
    for line in input:
        words = line.split()
        outer_bag = words[0] + words [1]
        words = words[4:]
        while len(words) > 0:
            number = words[0]
            if number != "no":
                inner_bag = words[1] + words[2]
                print("Adding edge (%s, %s)" % (inner_bag, outer_bag))
                graph.add_edge(inner_bag, outer_bag)
                words = words[4:]
            else:
                words = []
    print(graph)
    return graph


def compute07(input):
    graph = build_graph(input)
    result = len(graph.find_all_reachable_nodes("shinygold"))
    return result

def compute07b(input):
    result = 0
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

