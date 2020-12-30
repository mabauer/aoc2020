Advent of Code 2020
===================

In 2020 I took part in [Advent of Code](https://adventofcode.com/), an an Advent calendar of small programming puzzles.

I solved the 2020 puzzles in Python 3. The storyline consists 25 episodes of traveling to a remote tropical island to spend Christmas vacation in peace. But that journey isn't fun without obstacles:

* Day 01: *Report Repair*: Find two (part 1) or three (part2) entries in a list of numbers that sum up to 2020.

* Day 02: *Password Philosophy*: Verify passwords according to various rules. Involves some simple parsing and some *regular expressions*.

* Day 03: *Toboggan Trajectory*: Using toboggans (sleds) to descent some slopes. Count trees on the slope for different trajectory strategies. Uses the *modulo* operator to implement an infinitly wide slope.

* Day 04: *Passport Processing*: Verify passports at the airport. Involves more advanced parsing and more regular expressions.

* Day 05: *Binary Boarding*: Find your seat in a plane (using some awkward binary space partitioning seating scheme). There is an easy solution by converting the scheme to binary numbers. I did not see that so I implemented a partitioning algorithm. :-(

* Day 06: *Custom Customs*: Evaluate answers of groups of people at custom controls. Uses *dictionaries* and logic ("*anyone* vs *everyone*). Lesson learned: Always make shure that you read in all the data, even if the last line is not finished with a *newline*.

* Day 07: *Handy Haversacks*: Figure out different ways to combine travel bags where bags of a certain color may contain a number other bags (of different specific colors). I solved it by using *direct acyclic graphs* to represent the "containment" relationships. I took me a while to implement this (and the corresponding algorithms operating on the graph, like finding reachable nodes), so there might be easier and shorter solutions.

* Day 08: *Handheld Halting*: Implement a very simple *CPU simulator* of a gaming console to discover an infinite loop in the boot code of a gaming console (and patch it successfully with trial and error).

* Day 09: *Encoding Error*: Connect to a plane's onboard entertaining system. In order to be able to interface with it, find the weakness in a list of numbers, i.e. a number that cannot be reproduced by the sum of some pair of numbers (part1) or a contiguous block of numbers (part2) in a *rolling window* of numbers previously read. 

* Day 10: *Adapter Array*: Build chains of power adapters for an electronic device. Part 1: Count joltage jumps of one or three in such chains. Part 2: Count the number of possible combinations of such chains, given that the maximun joltage jumps should be below or equal three. Involves [*dynamic programming*](https://towardsdatascience.com/beginners-guide-to-dynamic-programming-8eff07195667) with *memoization*.  

* Day 11: *Seating System*: Model how people occupy seats in the waiting area of the ferry as a modificaton of [Conways's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Note: The update rules for the cells (or seats) take place *simultaneously*. This requires precalculating the update conditions (e.g. the number of neighbouring cells/seats) and then perform the updates or something similar. 

* Day 12: *Rain Risk*: Navigate a ferry using navigation commands similar to 
[Logo's](https://en.wikipedia.org/wiki/Logo_(programming_language)) turtle graphics and calculate the endpoint of the journey.
My solution involves some trigonometry and *Polar coordinates*.

* Day 13: *Shuttle Search*: Reason about departure times of circulating busses. Each bus takes the time for its circle indicated by its number. In part 2, we are looking for some timestamp where the busses leave with some predefined offsets after one another. My implementation relies on building up the solution in an *iterative way*, e.g. by finding the solution for two busses and modify it such that the condition for the third bus is also met -- and so on.

* Day 14: *Docking Data*: Simulate some boot code again -- for the ferry's docking procedure. Involves calculating with numbers in binary encoding and bitmasks.

* Day 15: *Rambunctious Recitation*: Simulate a memory game, where a number must be spoken each round -- this number however depends on numbers spoken in previous rounds. Involves the clever use of dictionaries.

* Day 16: *Ticket Translation*: Determine fields on unreadable train tickets by correctly matching example tickets and rules. Involves a [*matching algorithm*](https://programmingwiki.de/Matching-Probleme). It took me quite some time to implement this efficiently.

* Day 17: *Conway Cubes*: Make Conways's Game of Life (from day 11) work with cubes in 3D or hypercubes in 4D. Some extra thought is needed because this time, the dimensions of the "game area" are not fixed.

* Day 18: *Operation Order*: Make the homework for some kid next to you on the ferry. Involves evaluating simple *expressions* with different *operator precedence* rules. For yy solution I've implemented a simple *recursive descent parser*(https://en.wikipedia.org/wiki/Recursive_descent_parser) (that evaluates the expressions it parsers in the same run). Lesson learned: Getting the grammars right is always difficult for me.

* Day 19: *Monster Messages*: Verify messages that are built up by some kind of "producing" grammar. My recursive, naive approach worked for part 1, for part 2 (involving recursion) I had to switch over to an approach using *regular expressions*. I got a hint form a collegue -- I am not shure if I'd come up with that idea on my own :-(

* Day 20: *Jurrasic Jigsaw*: Assemble a huge image from smaller pieces (tiles) and find a sea monster in the resulting image. For me, this was probably the hardest of the puzzles of 2020. It involves figuring out that there is a *unique solution* for *puzzling* the images together by rotating and flippiung them. My solution starts by finding the corners, using one of the corner pieces as the top left corner (rotating and flipping the corner piece until it fits) and then assembling the image row by row (again by finding each next piece via trial and error and rotating/turning it until it fits).

* Day 21: *Allergene Assessment*: Figure out allergenes in (unreadable) igredient lists of foods. Like in day 16, the solution requires some matching algorithm.

* Day 22: *Crab Combat*: Simulate a card game with and without recursion.

* Day 23: *Crab Cups*: Simulate another game -- this time the games involves cups in a circle where three cups are removed from the circle and inserted at some specific position in the circle (determined by a set of rules). A naive simulation can be easily implemented using regualr lists/arrays -- in part 2 however the circle involves one million cups. It turns out that this simulation requires a more clever implementation to avoid expensive add/remove operations -- *O(n)* -- to the array. My solution uses a *dictionary* that for each cups holds the next cup in the circle, but *linked lists* should also work, speeding up adds/removes to *O(1)*.

* Day 24: *Lobby Layout*: Again, Conway's Game of Life. This time using hexagonal tiles in the hotel lobby with a hexagonal coordinate system. Lesson learned: Working with hexagonal systems is tricky. There are a number of [ways](https://www.redblobgames.com/grids/hexagons/) of dealing with hexagons correctly, once I had that figured out, the puzzle was relatively straight forward. (I used so called axial or *skewed* coordinates, because the work well when adding or multiplying coordinates as required for part 1). 

* Day 25: *Combo Breaker*. Cracking a very simply [public key algorithm](https://skerritt.blog/diffie-hellman-merkle/). Pretty straight forward once I discovered that the brute-force-attack heavily profits from reusing the result from the previous iteration.

I did all 25 x 2 puzzles. I had fun while solving them and I did learn *a lot*. Some of the puzzles took quite some time to solve, either because of easy to avoid implementation errors or because I did not always see the "easy" to implement solution. Obviously I could use some more programming practice... :-)






