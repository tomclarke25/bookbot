from collections import Counter

def get_word_count(book_text: str) -> int:
    if not book_text:
        return 0
    words = book_text.strip().split()
    return len(words)

def get_character_count(book_text: str) -> dict:
    return dict(Counter(book_text.lower()))

def get_sorted_character_count(character_count) -> list:
    char_list = [{"char": char, "num": count} for char, count in character_count.items()]
    return sorted(char_list, key=lambda char: char["num"], reverse=True)

