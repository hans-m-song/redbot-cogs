def repeatchar(char: str, length: int, delim: str = "") -> str:
    return delim.join(list(map(lambda _: char, range(length))))
