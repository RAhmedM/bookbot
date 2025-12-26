import sys

from stats import convert_to_list, get_char_num, get_num_words, get_text, list_sort


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    filePath = sys.argv[1]

    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    text = get_text(filePath)
    num_word = get_num_words(text)
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")
    char_num = get_char_num(text)

    clist = convert_to_list(char_num)
    list_sort(clist)


main()
