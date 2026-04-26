import os

name_file = input("Введите название файла: ")
path_file = os.getcwd()


with open("stop_words.txt", "r", encoding="utf-8") as sw:
    cens = sw.read().split()
    print(cens)
    
new_text = {}

with open (name_file, "r", encoding="utf-8") as f:
    text = f.read().split()
    new_text = text
    print(new_text)
    for x in new_text:
        for z in cens:
            if x == z:
                z = "***"
                new_text.append(z)
            else:
                new_text.append(z)
print(new_text)