#!/usr/bin/env python3

import re

from typing import Dict, List, Set

from utils import read_inputfile

ingredient_to_food : Dict[str, Set[int]] 
allergen_to_food : Dict[str, Set[int]] 
ingredient_to_allergen : Dict[str, Set[str]]   

def analyze_foods(input):
    global ingredient_to_food 
    global allergen_to_food 
    global ingredient_to_allergen
    ingredient_to_food = {}
    allergen_to_food = {}
    ingredient_to_allergen = {}
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
    for ingredient in ingredient_to_food:
        ingredient_to_allergen[ingredient] = set()
        for allergen in allergen_to_food:
            if allergen_to_food[allergen].issubset(ingredient_to_food[ingredient]):
                ingredient_to_allergen[ingredient].add(allergen)  
    # print(ingredient_to_food)
    # print(allergen_to_food)
    # print(ingredient_to_allergen)
 
def part1(input):
    global ingredient_to_allergen
    global ingredient_to_food
    analyze_foods(input) 
    allergen_free_ingredients = [ ingredient for ingredient in ingredient_to_allergen 
        if ingredient_to_allergen[ingredient] == set() ]
    print(allergen_free_ingredients)
    result = 0
    for ingredient in allergen_free_ingredients:
        result += len(ingredient_to_food[ingredient])
    return result

def solve(problem, done = None, keys_to_process = None):
    if done is None:
        done = []
    if keys_to_process is None:
        keys_to_process = [ k for k in problem.keys() ]
    solution = problem.copy()
    for key in sorted(keys_to_process, key=lambda k: len(solution[k])):
        values = [ v for v in list(problem[key]) if v not in done]
        if values == []:
            return None
        if len(values) == 1:
            done.append(values[0]) 
            solution[key] = [values[0]]
            keys_to_process.remove(key)
        else:
            for elem in values:
                done2 = done.copy()
                done2.append(elem)
                keys_to_process2 = keys_to_process.copy()
                keys_to_process2.remove(key)
                solution = solve(solution, done2, keys_to_process2)
                if solution is not None:
                    solution[key] = [elem]
                    return solution
            return None
    return solution

def part2(input):
    global ingredient_to_allergen
    result = 0
    analyze_foods(input)
    # for ingredient in sorted(ingredient_to_allergen, 
    #     key=lambda ingredient: len(ingredient_to_allergen[ingredient])):
    #     print("%s -> %s" % (ingredient, ingredient_to_allergen[ingredient]))
    ingredient_to_allergen = solve({ ingredient:allergenes for (ingredient,allergenes) in ingredient_to_allergen.items() if allergenes != set() })
    result = ",".join(sorted(ingredient_to_allergen, key=lambda ingredient: ingredient_to_allergen[ingredient][0]))
    return result

def main():    

    # Official input
    input = read_inputfile("input21.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %s" % (part2(input)))

if __name__ == "__main__": 
    main()

