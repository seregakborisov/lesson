import os

name_file = input("Введите название файла: ")
path_file = os.getcwd()


with open("stop_words.txt", "r", encoding="utf-8") as sw:
    cens = sw.read().split()
    print(cens)
    
new_text = []

with open (name_file, "r", encoding="utf-8") as f:
    text = f.read().split()
    print(text)
    for z in cens:
        for x in text:
            if x == z:
                x = "***"
            new_text.append(x)
            
            
print(new_text)