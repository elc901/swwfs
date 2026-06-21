import os
import shutil
from pathlib import Path
class Folder:

    def __init__(self):
        pass

    def create(self, path, name): # создание папки
            self.path = Path(path)
            self.name = name if name is not None else self.path.name
            self.path.mkdir(parents=True, exist_ok=True)
            return self
    
    def remove(self, path): # удаление папки
        path = Path(path)
        shutil.rmtree(path)
        return self
    
    def clear(self, path): # очистка внутренностей папки
        p = Path(path)
        if not p.exist(): # если путь не найден
            print(f"{path} not found")
            return self
        if not p.is_dir():
            print(f"{path} isnt folder") # если не папка в пути
            return self
        for item in p.iterdir():
            if item.is_file() or item.symlink(): 
                item.unlink() # удаление файлов и ссылок на них
            elif item.is_dir():
                shutil.rmtree(path)  # удаление директории

    def copy(self, path, path_for_copy): # копирование папки
        p = Path(path)
        pfc = Path(path_for_copy)


