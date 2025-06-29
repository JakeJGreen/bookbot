import os
from stats import get_num_words,get_num_char,sort_dict
def main(): 
    path = "books/frankenstein.txt"
    content = get_book_text(path)
    #print("============ BOOKBOT ============")
    #print(f"Analyzing book found at {path}...")
    #print("----------- Word Count ----------")
    get_num_words(content)
    #print("----------- Character Count ----------")
    #get_num_char(content)
    num_of_chars = get_num_char(content)
    #print(num_of_chars)
    report = sort_dict(num_of_chars)
    for k,v in report.items():
        print(f"{k}: {v}")
    #print (content)
    
def get_book_text(file):
    if os.path.exists(file):
        with open(file) as book:
            return book.read()
    else:
        print (file)
        print("The specified path does NOT exist.")

    
main()