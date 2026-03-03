def is_anagram_1(s: str, t: str) -> bool:
    """
    Returns True if `s` and `t` are anagrams.

    This implementation sorts both strings and compares the sorted results.
    Two strings are anagrams if their sorted character sequences are identical.

    Time Complexity: O(n log n)
    Space Complexity: O(n)

    :param s: first string
    :param t: second string
    :return: if the two strings are anagrams
    """
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t


def is_anagram_2(s: str, t: str) -> bool:
    """
    Returns True if `s` and `t` are anagrams.

    This implementation uses frequency balancing with a fixed-size
    array of length 26 (for lowercase English letters). Characters
    from `s` increment counts, and characters from `t` decrement them.
    If all counts return to zero, the strings are anagrams.

    Assumes input contains only lowercase English letters ('a'–'z').

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param s: first string
    :param t: second string
    :return: if the two strings are anagrams
    """
    if len(s) != len(t):
        return False

    lookup: list[int] = [0] * 26
    for c in s:
        lookup[ord(c) - ord('a')] += 1

    for c in t:
        lookup[ord(c) - ord('a')] -= 1

    for i in lookup:
        if i != 0:
            return False

    return True


r = is_anagram_2("racecar", "carrace")
print(r)
