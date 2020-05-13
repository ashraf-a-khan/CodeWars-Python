"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

"""



#str = "Hello this is Anthony a Gonzalves"
words = str.split(" ")
word = words[0]
for i in words:
    if len(word) < len(i):
        word = word
    else:
        word = i
return (len(word))