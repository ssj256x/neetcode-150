def encode_simple(strs: list[str]) -> str:
    """
    Encodes the string in the patter below

    strs = ["red", "black", "purple", "white"]
    encoded = "3#red5#black6#purple5#white"
    where each number #n before a string represents the length to look ahead to.

    :param strs: list of strings
    :return: encoded string
    """

    encoded = []
    for s in strs:
        encoded.append(f"{len(s)}#{s}")

    return ''.join(encoded)


def decode_simple(s: str) -> list[str]:
    """
    Decodes a string from below format into a `list[str]`

    encoded = "3#red5#black6#purple5#white"
    decoded_list = ["red", "black", "purple", "white"]

    :param s: the string to decode
    :return: list of decoded strings
    """

    decoded = []
    i = 0

    while i < len(s):
        j = i

        while s[j] != '#':
            j += 1

        length = int(s[i:j])
        start = j + 1
        end = start + length
        decoded.append(s[start:end])

        i = end

    return decoded

def encode_state_machine(strs: list[str]) -> str:
    """
    Encodes the string in the patter below

    strs = ["red", "black", "purple", "white"]
    encoded = "<3>red<5>black<6>purple<5>white"
    where each number <#> before a string represents the length to look ahead to.

    :param strs: list of strings
    :return: encoded string
    """

    encoded = []
    for s in strs:
        encoded.append(f'<{len(s)}>{s}')

    return ''.join(encoded)


def decode_state_machine(s: str) -> list[str]:
    """
    Decodes a string from below format into a `list[str]`

    encoded = "<3>red<5>black<6>purple<5>white"
    decoded_list = ["red", "black", "purple", "white"]

    :param s: the string to decode
    :return: list of decoded strings
    """

    decoded = []
    expect = '<'
    size = ''

    i = 0
    while i < len(s):
        c = s[i]

        if expect == '<':
            assert c == '<'
            expect = 'num'
            i += 1

        elif expect == 'num':
            while c.isdigit() and i < len(s):
                i += 1
                size += c
                c = s[i]
            expect = '>'

        elif expect == '>':
            extract = s[i + 1: i + int(size) + 1]
            expect = '<'
            decoded.append(extract)
            i += int(size) + 1
            size = ''

    return decoded


str_list = ["red", "black", "purple", "white"]
e = encode_simple(str_list)
print(f'Encoded: {e}')

d = decode_simple(e)
print(f'Decoded: {d}')
