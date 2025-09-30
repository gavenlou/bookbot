def get_num_words(text):
  print(f"Found {len(text.split())} total words")

def get_character_count(text):
  print("--------- Character Count -------")
  character_counts = {}
  for letter in text.lower():
    if letter in character_counts:
      character_counts[letter] += 1
    else:
      character_counts[letter] = 1
  return character_counts

def sort_dict(characters):
  return characters["num"]

def create_sorted_list(dict):
  sorted_list = [];
  for value in dict:
    sorted_list.append({"char": value, "num": dict[value]})
  sorted_list.sort(reverse=True,key=sort_dict)
  return sorted_list
