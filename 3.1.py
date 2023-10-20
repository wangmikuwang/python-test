def max_value(*args):
    if len(args) == 0:
        return None
    max_arg = args[0]
    for arg in args[1:]:
        if arg > max_arg:
            max_arg = arg
    return max_arg
print(max_value(1,5.9,88,157,224))