"""
Print out the longest even word in the given sentence

"""

sentence = "Hello my name is Mohammad Ashraf Khan"
words = sentence.split(" ")
# print(words)
maxim = ""
for i in words:
    if len(i)%2 == 0:
        if len(i) >= len(maxim):
            maxim = i

print(maxim)
