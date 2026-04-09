import sys

from src.stats import get_book_text, get_char_freq, get_num_words


def main():
    if len(sys.argv) == 2:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words.")
    print("--------- Character Count -------")
    sorted_by_value = sorted(
        get_char_freq(text).items(), key=lambda item: item[1], reverse=True
    )
    for char_freq in sorted_by_value:
        if char_freq[0].isalpha():
            print(char_freq)
    print("============= END ===============")


if __name__ == "__main__":
    main()
