import sys
from stats import get_word_count, get_char_count, sort_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_list = sort_dict(char_count)
    report = f"""
    ============ BOOKBOT ============
    Analyzing book found at {file_path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------
    """

    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        report += f"{char}: {count}\n"

    report += "============= END ==============="
    # print(f"{num_words} words found in the document")
    # print(char_count)
    print(report)

if len(sys.argv) > 1:
    main()
else:
    sys.exit(1)
