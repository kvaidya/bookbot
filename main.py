
def get_words_count(text):
    return len(text.split())

def get_letter_instances(text):
    letters = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha():
            if letter in letters:
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1
    return letters

def sort_letters(dict):
    return dict["count"]

def get_sorted_letter_counts(text):
    letter_instances = get_letter_instances(text)
    letter_list = []
    for key in letter_instances:
        letter_list.append({"letter": key, "count": letter_instances[key]})
    letter_list.sort(reverse=True, key=sort_letters)
    return letter_list


def get_file_contents(file_path):
    with open(file_path) as f:
        return f.read()

def print_book_report(file_path):
    print(f"--- Begin report of {file_path} ---")
    file_content = get_file_contents(file_path)
    print(f"{get_words_count(file_content)} words found in the document\n")
    for letter_record in get_sorted_letter_counts(file_content):
        print(f"The '{letter_record["letter"]}' character was found {letter_record["count"]} times")
    print("--- End report ---")
    
def main():
    print_book_report("books/frankenstein.txt")

main()
