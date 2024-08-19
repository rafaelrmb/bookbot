def main ():
  path = "books/frankenstein.txt"
  book_text = get_book_as_string(path)
  num_of_words = count_total_of_words(book_text)
  chars_dict = count_total_chars(book_text)
  print(f"{num_of_words} words in the book!")
  generate_report(chars_dict, path)

def get_book_as_string(path_to_book):
  with open(path_to_book) as book_file:
    return book_file.read()

def count_total_of_words(text):
  non_whitespace_words = text.split()
  return len(non_whitespace_words)

def count_total_chars(text):
  chars_dict = {}
  lowercase_text = text.lower()

  for char in lowercase_text:
      if char.isalpha():
        if char in chars_dict.keys():
          chars_dict[char] += 1
        else: 
          chars_dict[char] = 1
  return chars_dict

def generate_report(dictionary, path):
  sorted_dictionary = sort_dictionary_by_value(dictionary)

  print(f"--- Begin report of {path} ---")

  for item in sorted_dictionary:
    print(f"The char {item[0]} was found {item[1]} times")

  print("--- End report ---")

def sort_dictionary_by_value(dictionary):
  dictionary_tuple = dictionary.items()
  sorted_items_by_value = sorted(dictionary_tuple, key=lambda item: item[1], reverse=True)
  
  return sorted_items_by_value

main()
