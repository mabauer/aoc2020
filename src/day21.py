#!/usr/bin/env python3

import re

from typing import Dict, List, Set, Tuple

from utils import read_inputfile



def part1(input):
    ingredient_to_food : Dict[str, Set[int]] = {}
    allergen_to_food : Dict[str, Set[int]] = {}
    ingredient_to_allergen : Dict[str, Set[str]] = {}    
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
    allergen_free_ingredients = [ ingredient for ingredient in ingredient_to_allergen 
        if ingredient_to_allergen[ingredient] == set() ]
    print(allergen_free_ingredients)
    result = 0
    for ingredient in allergen_free_ingredients:
        result += len(ingredient_to_food[ingredient])
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = read_inputfile("input21.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

