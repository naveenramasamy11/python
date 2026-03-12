#!/usr/bin/env python3
"""Remove duplicates from a list while preserving order."""


def unique(items: list) -> list:
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


print(unique([1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8]))
