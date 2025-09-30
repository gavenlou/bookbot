def get_num_words(text):
  print(f"Found {len(text.split())} total words")

def get_character_count(text):
  character_counts = {}
  for letter in text.lower():
    if letter in character_counts:
      character_counts[letter] += 1
    else:
      character_counts[letter] = 1
  return character_counts
