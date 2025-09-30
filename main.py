from stats import get_num_words
from stats import get_character_count

def get_book_text(filepath):
  with open(filepath) as book:
    file_contents = book.read()
    return file_contents

def main():
  book = get_book_text('books/frankenstein.txt')
  get_num_words(book)
  character_count = get_character_count(book)
  print(character_count)

main()
