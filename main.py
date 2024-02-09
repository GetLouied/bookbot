def count_words_in_text(text: str) -> int:
    words = text.split()
    word_count = len(words)
    return word_count

def letter_count_in_text(text: str) -> dict:
    words = text.split()
    letter_dict = {}
    for word in words:
        word = word.lower()
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            elif letter in letter_dict:
                letter_dict[letter] += 1
            else:
                print('something broke')
    return letter_dict

def sort_on(dict: dict) -> int:
    return list(dict.values())[0]

def aggregate_report(letter_dict: dict) -> list:
    letter_count_list = []

    for k, v in letter_dict.items():
        temp_dict = {k: v}
        letter_count_list.append(temp_dict)

    letter_count_list.sort(reverse=True, key=sort_on)
    return letter_count_list 

def print_report(aggregate_list: list, word_count: int, book_path: str) -> None:

    print("")
    print(f"--- Begin report of {book_path} ---")
    print(f'{word_count} words found in the document')
    print("")
    for item in aggregate_list:
        # Can use isalpha() if statement on key if you want only alphabetical letters.
        for key, value in item.items():
            print(f"The '{key}' character was found {value} times")

    print("--- End report ---")
    print("")


def main():
    book_path = "books/frankenstein.txt"

    with open(f"{book_path}") as f:
        file_contents = f.read()
        word_count = count_words_in_text(file_contents)
        aggregate_report_list = aggregate_report(letter_count_in_text(file_contents))
        print_report(aggregate_report_list, word_count, book_path)

main()