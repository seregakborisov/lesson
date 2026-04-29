import platform
import os
import shutil

print(f"Версия операционной: {platform.platform()}, {platform.system()}")

print("-" * 20)

print(f"Путь к файлу: {os.getcwd()}") 

print("-" * 20)

direc = os.getcwd()
n = 0
file_stats = {}

for file_name in os.listdir(direc):
    file_path = os.path.join(direc, file_name)
    
    if os.path.isfile(file_path):        
        ext_of_file = file_name.split(".")        
        ext = ext_of_file[-1]
        
        folder_name = ext
        folder_path = os.path.join(direc, folder_name)
        
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        
        new_file_path = os.path.join(folder_path, file_name)
        
        shutil.move(file_path, new_file_path)
        
        print(f"Перемещение .{ext} выполнено")
         
        
        """size_file = os.path.getsize(new_file_path)
        size_file += size_file
        n += 1
        
        print(f"Перемещено {n} файлов, общий объем {size_file} байт")
        print("*" * 20, "\n")"""
        
        size_new = os.path.getsize(new_file_path)
        
        if ext not in file_stats:
            file_stats[ext] = {"count":0, "size":0, "files":[]}
            
        file_stats[ext]["count"] += 1
        file_stats[ext]["size"] += size_new
        file_stats[ext]["files"].append(file_name)
            

print("-" * 20)
for ext, stats in file_stats.items():
    print(f"В папке '{ext}' перемещено {stats['count']} файлов, суммарный размер - {stats['size']} байт")
    print("*" * 20)

