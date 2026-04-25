import platform
import os
import shutil

print(f"Версия операционной: {platform.platform()}, {platform.system()}")

print("-" * 20)

print(f"Путь к файлу: {os.getcwd()}") 

print("-" * 20)

direc = os.getcwd()

for file_name in os.listdir(direc):
    file_path = os.path.join(direc, file_name)
    
    if os.path.isfile(file_path):        
        ext_of_file = file_name.split(".")        
        ext = ext_of_file[-1]
        
        folder_name = ext
        folder_path = os.path.join(direc, folder_name)
        
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        
        new_file_patch = os.path.join(folder_path, file_name)
        
        shutil.move(file_path, new_file_patch)
        
        print(f"Перемещение .{ext} выполнено")

print("-" * 20)