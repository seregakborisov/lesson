import os

with open("text.txt", "r") as t:
    text_file = t.readlines()
    for text in text_file:
        words = text.split()
         
        counts = {}
         
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1 
        max_word = ""
        max_count = 0
        
        for word in counts:
            if counts[word] > max_count:
                max_word = word
                max_count = counts[word]
                with open("result.txt", "a") as result:
                    result.write(f"{max_word} {max_count}\n")
