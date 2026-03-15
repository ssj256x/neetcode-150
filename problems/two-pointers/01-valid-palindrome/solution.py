def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue

        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False

    return True


string = "Was it a car or a cat I saw?"
print(is_palindrome(string))
string = "No lemon, no melon"
print(is_palindrome(string))
