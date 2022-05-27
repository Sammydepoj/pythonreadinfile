# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from importlib.resources import contents


def read_file_content (filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        text=f.read()
    return text

def count_words(*args):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    for arg in args:
        words=text.count(arg)
        print({arg:words,})
       # return{arg:words,}

count_words('on','teaching','walked','smile')
