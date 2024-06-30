from typing import List
import itertools

letter_freqs = {
    'A': 8.2    /100,
    'B': 1.5    /100,
    'C': 2.8    /100,
    'D': 4.3    /100,
    'E': 12.7   /100,
    'F': 2.2    /100,
    'G':2.0     /100,
    'H': 6.1    /100,
    'I': 7.0    /100,
    'J': 0.15   /100,
    'K': 0.77   /100,
    'L':4.0     /100,
    'M':2.4     /100,
    'N':6.7     /100,
    'O':7.5     /100,
    'P':1.9     /100,
    'Q':0.095   /100,
    'R':6.0     /100,
    'S':6.3     /100,
    'T':9.1     /100,
    'U':2.8     /100,
    'V':0.98    /100,
    'W':2.4     /100,
    'X':0.15    /100,
    'Y':2.0     /100,
    'Z':0.074   /100,
}

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def calculate_cost(divisions: List[int], verbose: bool = False) -> int:
    idx = 0
    cost = 0 
    prev_cost = 0

    while idx < len(divisions) -1:
        section = alpha[divisions[idx]:divisions[idx+1]]
        for pos, letter in enumerate(section):
            cost += letter_freqs[letter] * pos

        if verbose: print("{0:9}".format(section) + "\t" + "{0:4.4f}".format(cost - prev_cost))
        prev_cost = cost
        idx += 1

    return cost

def print_divs(divisions: List[int]):
    idx = 0
    while idx < len(divisions) -1:
        section = alpha[divisions[idx]:divisions[idx+1]]
        print(section)
        idx += 1

def hunt_for_lowest_cost(num_groups: int, verbose: bool = False):
    best_divs = []
    best_cost = 999999999999999
    for comb in itertools.combinations(range(1, 26 + 1), num_groups -1): # For n groups you need n-1 dividers eg 2 dividers:   ABC|DEF|GHI
        divs = list(comb)
        divs.insert(0,0)
        divs.append(len(alpha))

        this_cost = calculate_cost(divs)
        if this_cost < best_cost:
            best_cost = this_cost
            best_divs = divs

            if verbose: 
                print("new best: " + str(best_cost))
                print_divs(divs)

    print("\n==== BEST OVERALL ====\tn=" + str(num_groups))
    calculate_cost(best_divs, verbose=True)

def hunt_for_lowest_cost_6(verbose:bool = False):
    best_divs = []
    best_cost = 999999999999999
    for div1 in range(1, len(alpha) - 4):
        for div2 in range(div1+1, len(alpha) -3):
            for div3 in range(div2+1, len(alpha) -2):
                for div4 in range(div3+1, len(alpha) -1):
                    for div5 in range(div4+1, len(alpha)):
                        divs = [0, div1, div2, div3, div4, div5, len(alpha)] 
                        this_cost = calculate_cost(divs)

                        if this_cost < best_cost:
                            best_cost = this_cost
                            best_divs = divs

                            if verbose: 
                                print("new best: " + str(best_cost))
                                print_divs(divs)

    print("\n==== BEST OVERALL ====\tn=6")
    calculate_cost(best_divs, verbose=True)


hunt_for_lowest_cost(8, verbose=False)
