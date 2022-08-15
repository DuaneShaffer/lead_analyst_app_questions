def are_anagrams(x, y):
    """Given two strings, return if they are anagrams of each other"""
    return sorted(x.replace(' ', '')) == sorted(y.replace(' ', ''))