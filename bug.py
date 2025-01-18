def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result) # This will cause a ZeroDivisionError

result = function_with_uncommon_error(0, 10)
print(result) # This will return 10 correctly

result = function_with_uncommon_error(10, 2)
print(result) # This will return 5 correctly