import sys
from pathlib import Path

from stats import get_word_count, get_character_count, get_sorted_character_count

def get_book_text(book_path):
    try:
        return book_path.read_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"Book file not found at: {book_path}")
    except IOError as e:
        raise IOError(f"Error reading book file: {e}")

def print_report(book_path, word_count, character_count):
    print(f"=========== BOOKBOT ============\n"
          f"Analyzing book found at {book_path}...\n"
          f"----------- Word Count ----------\n"
          f"Found {word_count} total words\n"
          f"--------- Character Count -------")
    for char in character_count:
        if not char['char'].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = Path(sys.argv[1])
    if not book_path.exists():
        print(f"Book file not found at: {book_path}")
        sys.exit(1)

    try:
        book_text = get_book_text(book_path)
        word_count = get_word_count(book_text)
        character_count = get_character_count(book_text)
        sorted_character_count = get_sorted_character_count(character_count)
        print_report(book_path, word_count, sorted_character_count)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
