# Numbers From A Hat

A number-pulling simulator with a configurable chart to show frequencies of various outcomes.

### Examples

Display full argument list and help: `python simulate.py --help`

With no arguments, the default behavior is equivalent to rolling a standard D6 die. The output gives you a summary of the simulation, then lists a few aggregate stats, then displays a frequency chart for the results simulated. The summary and aggregate stats can be omitted by passing the `--no-headers` argument.
```
$ python simulate.py
----- 10000 iterations dependently drawing 1 time(s) from 1 groups of 1-6 -----
Most common: 4
Avg: 3.5014
1 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (16.64%)
2 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (16.52%)
3 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (16.38%)
4 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (17.32%)
5 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (16.80%)
6 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (16.34%)
```

You can also tweak the parameters of the hat and the number of draws per simulation. So in this run, we are simulating 2 copies of the numbers 2, 3, 4, and 5 being drawn from twice. The hat will start with [2,2,3,3,4,4,5,5], then we might draw a 4 so it becomes [2,2,3,3,4,5,5], then we might draw a 2. Our result in that case would be 6, as 4 + 2 == 6. In this case we are doing one million iterations of the simulation.
```
$ python simulate.py --iterations 1000000 --range 4 --minimum 2 --groups 2 --draws 2
----- 1000000 iterations dependently drawing 2 time(s) from 2 groups of 2-5 -----
Most common: 7
Avg: 6.999319
 4 ]]]]]]]]]]]]] (3.61%)
 5 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (14.22%)
 6 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (17.92%)
 7 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (28.55%)
 8 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (17.85%)
 9 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (14.26%)
10 ]]]]]]]]]]]]] (3.58%)
```

If the range/min/groups mechanics are not sufficient, you can simply input a custom list of numbers for the hat like so:
```
$ python simulate.py --iterations 1000000 --custom "1,4,5,6,7,9,9,9,9"
----- 1000000 iterations dependently drawing 1 time(s) from [1, 4, 5, 6, 7, 9, 9, 9, 9] -----
Most common: 9
Avg: 6.554125
1 ]]]]]]]]]]]]]]]]]]]]]]]]] (11.13%)
2  (0.00%)
3  (0.00%)
4 ]]]]]]]]]]]]]]]]]]]]]]]]] (11.13%)
5 ]]]]]]]]]]]]]]]]]]]]]]]]] (11.09%)
6 ]]]]]]]]]]]]]]]]]]]]]]]]] (11.09%)
7 ]]]]]]]]]]]]]]]]]]]]]]]]] (11.14%)
8  (0.00%)
9 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (44.42%)
```

You can also change how the chart looks in several ways. This is the same "D6 roll" as the first example, reskinned
```
$ python simulate.py --chart-size 20 --chart-character "=" --label-right --show-exact-occurrences --no-percentages
----- 10000 iterations dependently drawing 1 time(s) from 1 groups of 1-6 -----
Most common: 6
Avg: 3.4964
==================== 1 (1698 times)
==================== 2 (1673 times)
=================== 3 (1670 times)
=================== 4 (1600 times)
=================== 5 (1644 times)
==================== 6 (1715 times)
```

By default draws are treated *dependently*, meaning once a number has been chosen, one copy of that number is removed from the hat, so that number is less likely to be chosen on the next draw. However, you can simply use the argument `--independent` to revert this behavior and simulate as if all the numbers are put back into the hat for each draw.
```
$ python simulate.py --iterations 1000000 --range 4 --minimum 2 --groups 2 --draws 2 --independent
----- 1000000 iterations independently drawing 2 time(s) from 2 groups of 2-5 -----
Most common: 7
Avg: 7.001334
 4 ]]]]]]]]]]]]]]]]]]]]]]]]] (6.22%)
 5 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (12.47%)
 6 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (18.80%)
 7 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (25.01%)
 8 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (18.74%)
 9 ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] (12.51%)
10 ]]]]]]]]]]]]]]]]]]]]]]]]] (6.26%)
```