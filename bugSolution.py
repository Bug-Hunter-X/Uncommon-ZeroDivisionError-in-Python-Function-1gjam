def function_with_uncommon_error_solution(a, b):
    if b == 0:
        return float('inf') # Handle division by zero
    elif a == 0:
        return b
    else:
        return a / b

result = function_with_uncommon_error_solution(10, 0)
print(result) # This will return inf

result = function_with_uncommon_error_solution(0, 10)
print(result) # This will return 10 correctly

result = function_with_uncommon_error_solution(10, 2)
print(result) # This will return 5 correctly