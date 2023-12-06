"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    distinct = []

    for it in items:
        if isinstance(it, int):
            it = str(it)
        if it not in distinct:
            distinct.append(it)

    for dis in distinct:
        count = 0
        for it in items:
            if isinstance(it, int):
                it = str(it)
            if dis == it:
                count += 1
        frequencies[dis] = count

    # Your code goes here
    return frequencies