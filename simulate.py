"""
This script simulates drawing numbers out of a hat and summing them, and provides a frequency chart via text output

The specific scenario envisioned is a certain number of groups of numbers 1-n.
You draw a number, then that number is then no longer available so the next draw
excludes it. The idea would be that the available numbers to start with might be 1, 1, 2, 2, 3, 3. So two groups of 1 to 3.
"""

__author__ = "Andy Chamberlain"


import random
import argparse


DEFAULT_RANGE = 6
DEFAULT_MINIMUM = 1
DEFAULT_NUM_GROUPS = 1
DEFAULT_NUM_DRAWS = 1
DEFAULT_NUM_ITERATIONS = 10000
DEFAULT_CHART_SIZE = 100
DEFAULT_CHART_CHARACTER = "]"


def parse_custom_hat(custom : str) -> list[int]:
    """ parses and returns a custom hat of numbers
        assumes inputs are integers separated by commas and/or whitespace """
    return [int(s.strip()) for s in custom.split(",")]


def generate_hat(range_size : int, minimum : int, num_groups : int, custom : str) -> list[int]:
    """ generates and returns a list of numbers to be drawn "from a hat" """
    choices = []
    if custom is None:
        for _ in range(num_groups):
            choices += [x + minimum for x in range(range_size)]
        
        return choices
    else:
        return parse_custom_hat(custom)


def draw(base_choices : list[int], num_draws : int, independent = False) -> int:
    """ draws the specified number of times, uniformly randomly from the given choices and removes each choice after it is chosen
        returns the sum of all draws """
    choices = base_choices[:]
    
    draws = []

    for _ in range(num_draws):
        choice = random.choice(choices)
        if not independent:
            choices.remove(choice)
        draws.append(choice)

    return sum(draws)


def extreme_draw(base_choices : list[int], num_draws : int, do_max = False, independent = False):
    """ Gets mininmum possible draw by default. Set do_max to True to get max instead """
    choices = base_choices[:]

    draws = []

    for _ in range(num_draws):
        if do_max:
            choice = max(choices)
        else:
            choice = min(choices)
        if not independent:
            choices.remove(choice)
        draws.append(choice)
    
    return sum(draws)


def main(args):
    base_choices = generate_hat(args.range, args.minimum, args.groups, args.custom)

    min_possible_result = extreme_draw(base_choices, args.draws, do_max=False, independent=args.independent)
    max_possible_result = extreme_draw(base_choices, args.draws, do_max=True, independent=args.independent)

    results = []

    for _ in range(args.iterations):
        results.append(draw(base_choices, args.draws, args.independent))
    
    num_occurrences = {(n + min_possible_result): 0 for n in range(max_possible_result - min_possible_result + 1)}

    for item in results:
        num_occurrences[item] += 1

    max_occurrences = -1
    most_frequent_result = -1

    for result in num_occurrences:
        if num_occurrences[result] > max_occurrences:
            max_occurrences = num_occurrences[result]
            most_frequent_result = result

    hat_desc = f"{args.groups} groups of {args.minimum}-{args.minimum + args.range - 1}" if args.custom is None else parse_custom_hat(args.custom)

    if not args.no_headers:
        print(f"----- {args.iterations} iterations drawing {args.draws} time(s) from {hat_desc} -----\nMost common: {most_frequent_result}\nAvg: {sum(results) / args.iterations}")

    keys_sorted = sorted(num_occurrences.keys())

    chart_lines = []

    max_chars_in_a_result = max([len(str(result)) for result in num_occurrences])

    for result in [k for k in keys_sorted if num_occurrences[k] > 0 or not args.omit_zero_occurrences]:
        line = args.chart_character*round(args.chart_size * num_occurrences[result] / (max_occurrences * len(args.chart_character)))
        if args.label_right:
            line += f" {result}"
        else:
            line = f"{result:>{max_chars_in_a_result}} " + line
        if not args.no_percentages:
            line += f" ({100 * num_occurrences[result] / args.iterations:.2f}%)"
        if args.show_exact_occurrences:
            line += f" ({num_occurrences[result]} times)"
        chart_lines.append(line)

    print("\n".join(chart_lines))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script simulates drawing numbers out of a hat and summing them, and provides a frequency chart via text output. By default it simulates the equivalent of a standard D6 die roll.")
    parser.add_argument("-i", "--iterations", type=int, default=DEFAULT_NUM_ITERATIONS, help="The number of iterations to run the simulation")
    parser.add_argument("-r", "--range", type=int, default=DEFAULT_RANGE, help="The size of the range of numbers possible on each draw.")
    parser.add_argument("-m", "--minimum", type=int, default=DEFAULT_MINIMUM, help="The minimum value of the range of numbers.")
    parser.add_argument("-d", "--draws", type=int, default=DEFAULT_NUM_DRAWS, help="The number of draws")
    parser.add_argument("-g", "--groups", type=int, default=DEFAULT_NUM_GROUPS, help="The number of groups of the range")
    parser.add_argument("-c", "--custom", type=str, default=None, help="Custom set of numbers to start in the hat. Example: \"1,1,2,3,7,8\"")
    parser.add_argument("-cs", "--chart-size", type=int, default=DEFAULT_CHART_SIZE, help="The length of the bar representing the most frequent result.")
    parser.add_argument("-cc", "--chart-character", type=str, default=DEFAULT_CHART_CHARACTER, help="The character or string used to make up the bars in the chart.")
    parser.add_argument("-o", "--omit-zero-occurrences", action="store_true", help="Whether to omit possible values from the chart which were drawn 0 times")
    parser.add_argument("-e", "--show-exact-occurrences", action="store_true", help="Display the exact number of occurrences for each result in the chart")
    parser.add_argument("-np", "--no-percentages", action="store_true", help="Hide the percentages of occurrences for each result in the chart")
    parser.add_argument("-lr", "--label-right", action="store_true", help="Label the results on the right of the chart rather than the left")
    parser.add_argument("-in", "--independent", action="store_true", help="Makes the draws independent; as if each number is put right back into the hat after drawn.")
    parser.add_argument("-nh", "--no-headers", action="store_true", help="Disable the headers; the simulation summary and aggregate stats printed above the bar chart.")
    args = parser.parse_args()
    main(args)
