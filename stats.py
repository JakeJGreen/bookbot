import string
import operator

def get_num_words(text):
    tokens = text.split()
    num_words = len(tokens)
    #print(f"{num_words} words found in the document")
    print(f"Found {num_words} total words")
'''
def get_num_char(string):
    string = string.lower()
    letters = list(map(chr, range(97, 123)))
    char_count = {}
    for l in letters:
        count = string.count(l)
        char_count.update({l:count})
    #print(char_count)
    return char_count
'''
def get_num_char(string):
    string = string.lower()
    chars = list(string)
    char_count = {}
    for c in chars:
        if c.isalpha():
            count = string.count(c)
            char_count.update({c:count})
        else:
            pass
    #print(char_count)
    return char_count


def sort_dict(dictionary):
    #print(f"dictionary for sorting:{dictionary}")
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict
    #print(f"sorted dictionary: {sorted_dict}")
    #print(sorted_dict.items())
    #for k,v in sort_dict.items():
        #print(f"{k}:{v}")
