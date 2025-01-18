# Uncommon ZeroDivisionError in Python

This repository demonstrates a subtle bug involving a `ZeroDivisionError` in Python. The function `function_with_uncommon_error` attempts to handle cases where either the first or second parameter is 0; however, it only correctly handles when the first parameter is 0. When the second parameter is 0, a `ZeroDivisionError` is raised.

The bug and its solution are provided in separate Python files (`bug.py` and `bugSolution.py`, respectively). The solution file showcases a more robust approach that avoids the `ZeroDivisionError` by explicitly checking for zero values before attempting division.