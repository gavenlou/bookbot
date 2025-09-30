def get_book_text(filepath):
  with open(filepath) as book:
    file_contents = book.read()
    return file_contents

def number_of_words(text):
  print(f"Found {len(text.split())} total words")

def main():
  book = get_book_text('books/frankenstein.txt')
  number_of_words(book)

main()
