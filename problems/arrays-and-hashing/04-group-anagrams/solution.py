def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Groups strings that are anagrams of each other using sorting.

    Each string is sorted alphabetically and used as a hash key.
    Strings with identical sorted representations belong to the same group.

    Time Complexity: O(n * m log m)
    Space Complexity: O(n * m)

    where:
        n = number of strings
        m = maximum length of a string

    :param strs: List of lowercase strings.
    :return: List of grouped anagrams.
    """
    lookup: dict[str, list[str]] = {}

    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str in lookup:
            lookup[sorted_str].append(s)
        else:
            lookup[sorted_str] = [s]

    return list(lookup.values())


def group_anagrams_optimal(strs: list[str]) -> list[list[str]]:
    """
    Groups strings that are anagrams using a frequency-count key.

    Instead of sorting each string, a fixed-size character frequency
    array (size 26) is used as a hash key. This removes the log factor
    from sorting and achieves linear time per string.

    Time Complexity: O(n * m)
    Space Complexity: O(n * m)

    where:
        n = number of strings
        m = maximum length of a string

    :param strs: List of lowercase strings.
    :return: List of grouped anagrams.
    """
    lookup: dict[tuple[int, ...], list[str]] = {}

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        key = tuple(count)

        if key in lookup:
            lookup[key].append(s)
        else:
            lookup[key] = [s]

    return list(lookup.values())


print(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
