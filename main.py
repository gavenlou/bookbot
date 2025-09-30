import sys
from stats import get_num_words
from stats import get_character_count
from stats import create_sorted_list

def get_book_text(filepath):
  print(f"Analyzing book found at {filepath}")
  with open(filepath) as book:
    file_contents = book.read()
    return file_contents

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  print("============ BOOKBOT ============")
  book = get_book_text(sys.argv[1])
  get_num_words(book)
  character_count = get_character_count(book)
  sorted_list = create_sorted_list(character_count)
  for dict in sorted_list:
    if dict["char"].isalpha():
      print(f"{dict["char"]}: {dict["num"]}")
  print("============= END ===============")

main()
