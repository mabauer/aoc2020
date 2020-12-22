#!/usr/bin/env python3

import re

from typing import Dict, List, Set, Tuple

from utils import read_inputfile

# Analyze the food declarations and return the following mappings:
#   * ingredient_to_food - tracks all food declarations where an ingredient is used
#   * ingredient_to_allergenes - lists all possible allergenes for an ingredient
def analyze_foods(input) -> Tuple[Dict[str, Set[int]], Dict[str, Set[str]]]:
    ingredient_to_food : Dict[str, Set[int]] = {}
    allergen_to_food : Dict[str, Set[int]] = {}
    ingredient_to_allergenes : Dict[str, Set[str]] = {} 
    # Parse the input
    food = 0
    for line in input:
        mo = re.search("(\(contains )(.*)\)", line)
        if mo is not None:
            food += 1
            allergens_part = mo.group(2)
            allergens = allergens_part.replace(" ", "").split(",")
            pos = mo.start(1)
            ingredients = line[:pos].strip().split(" ")
            # print("%s -> %s" % (ingredients, allergens)) 
            for ingredient in ingredients:
                if ingredient not in ingredient_to_food:
                    ingredient_to_food[ingredient] = set()
                ingredient_to_food[ingredient].add(food) 
            for allergen in allergens:
                if allergen not in allergen_to_food:
                    allergen_to_food[allergen] = set()
                allergen_to_food[allergen].add(food)
    # An ingredient can only contain an allergen if it shows up in the same (or more) food declarations as the allergen
    for ingredient in ingredient_to_food:
        ingredient_to_allergenes[ingredient] = set()
        for allergen in allergen_to_food:
            if allergen_to_food[allergen].issubset(ingredient_to_food[ingredient]):
                ingredient_to_allergenes[ingredient].add(allergen)  
    # print(ingredient_to_food)
    # print(allergen_to_food)
    # print(ingredient_to_allergen)
    return (ingredient_to_food, ingredient_to_allergenes)
 
def part1(input):
    (ingredient_to_food, ingredient_to_allergenes) = analyze_foods(input) 
    allergen_free_ingredients = [ ingredient for ingredient in ingredient_to_allergenes 
        if ingredient_to_allergenes[ingredient] == set() ]
    print(allergen_free_ingredients)
    result = 0
    for ingredient in allergen_free_ingredients:
        result += len(ingredient_to_food[ingredient])
    return result

# Find a perfect matching for between two candidate sets defined by a map
# The first candidate set makes up the keys, the second candidate set makes up the values of the map.
# Example: For {'nhx': {'fish'}, 'rrjb': {'peanuts'}, 'xmhsbd': {'wheat', 'peanuts', 'fish'}} a matching is:
#    {'nhx': 'fish', 'rrjb': 'peanuts', 'xmhsbd': 'wheat'}
def find_matching(candidates, done = None, keys_to_process = None):
    if done is None:
        done = []
    if keys_to_process is None:
        keys_to_process = [ k for k in sorted(candidates.keys(), key=lambda k: len(candidates[k])) ]
    solution = candidates.copy()
    while keys_to_process != []:
        key = keys_to_process[0]
        values = [ v for v in list(candidates[key]) if v not in done]
        if values == []:
            return None
        if len(values) == 1:
            solution[key] = values[0]
            done.append(values[0]) 
            keys_to_process.remove(key)
        else:
            for elem in values:
                done2 = done.copy()
                done2.append(elem)
                keys_to_process2 = keys_to_process.copy()
                keys_to_process2.remove(key)
                temp = find_matching(solution, done2, keys_to_process2)
                if temp is not None:
                    solution = temp
                    solution[key] = elem
                    return solution
            return None
    return solution

def part2(input):
    result = 0
    (_, ingredient_to_allergenes) = analyze_foods(input)
    # for ingredient in sorted(ingredient_to_allergen, 
    #     key=lambda ingredient: len(ingredient_to_allergen[ingredient])):
    #     print("%s -> %s" % (ingredient, ingredient_to_allergen[ingredient]))
    ingredient_to_allergenes = { ingredient:allergenes for (ingredient,allergenes) in ingredient_to_allergenes.items() if allergenes != set() }
    ingredient_to_allergen = find_matching(ingredient_to_allergenes)
    assert ingredient_to_allergen is not None
    result = ",".join(sorted(ingredient_to_allergenes, key=lambda ingredient: ingredient_to_allergen[ingredient]))
    return result

def main():    

    # Official input
    input = read_inputfile("input21.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %s" % (part2(input)))

if __name__ == "__main__": 
    main()

