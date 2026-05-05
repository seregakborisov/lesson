import os

name_file = input("Введите название файла: ")
path_file = os.getcwd()


with open("stop_words.txt", "r", encoding="utf-8") as sw:
    cens = sw.read().split()
    print(cens)
    
new_text = []


with open (name_file, "r", encoding="utf-8") as f:
    text = f.read().split()
  
    for word in text:
        l = len(word)
        if word not in cens:
            new_text.append(word)
        else:
            new_text.append(word[0] + "*" * (l-2) + word[-1])
            
            
            
print(" ".join(new_text))
            