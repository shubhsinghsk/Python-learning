def count_occurrences(iterable):
    occurrence_dict = {}
    for item in iterable:
        if item not in occurrence_dict:
            occurrence_dict[item] = 1
        else:
            occurrence_dict[item] += 1
    return occurrence_dict