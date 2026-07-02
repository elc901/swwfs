import os
import shutil
from pathlib import Path

class Folder:

    def __init__(self):
        pass
    
    @classmethod
    def create(cls, path, name=None):  # создание папки
        path = Path(path)
        if name:
            full_path = path / name
        else:
            full_path = path
        
        folder = cls()  
        folder.path = full_path
        folder.name = name if name else full_path.name
        full_path.mkdir(parents=True, exist_ok=True)
        return folder
    
    @classmethod
    def remove(cls, path):  # удаление папки
        path = Path(path)
        if path.exists():
            shutil.rmtree(path)
        return cls()
    
    @classmethod
    def clear(cls, path):  # очистка внутренностей папки
        p = Path(path)
        if not p.exists(): 
            print(f"{path} not found")
            return cls()
        if not p.is_dir():
            print(f"{path} isnt folder")
            return cls()
        for item in p.iterdir():
            if item.is_file() or item.is_symlink():  
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)  
        return cls()
    
    @classmethod
    def copy_from_to(cls, path, path_for_copy):  # копирование содержимого папки
        p = Path(path)
        pfc = Path(path_for_copy)
        if p.exists() and p.is_dir():
            shutil.copytree(p, pfc, dirs_exist_ok=True)  
        return cls()