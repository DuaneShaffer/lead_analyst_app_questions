def is_inclusive_integer(range, input_integer):
    """ Given a lower and upper bound as range, return if input integer is between them inclusive."""
    lower_bound, upper_bound = range
    if upper_bound < lower_bound:
        raise ValueError("Upper bound must be >= lower bound")
    return lower_bound <= input_integer <= upper_bound