def build_word(words: list[str]) -> str:
    return "".join(word[i] for i, word in enumerate(words))
