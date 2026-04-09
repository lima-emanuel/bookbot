from collections import Counter

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def get_num_words(book_str: str) -> int:
    count = 0
    for word in book_str.split():
        count += 1
    return count

def get_char_freq(book_str: str) -> Counter:
    return Counter(book_str.lower())