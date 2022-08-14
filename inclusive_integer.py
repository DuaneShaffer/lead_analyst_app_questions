def is_inclusive_integer(range, input_integer):
    lower_bound, upper_bound = range
    if upper_bound < lower_bound:
        raise ValueError("Upper bound must be >= lower bound")
    return lower_bound <= input_integer <= upper_bound