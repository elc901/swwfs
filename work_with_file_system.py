import os
import shutil
from pathlib import Path
class Folder:

    def __init__(self):
        pass

    def create(self, name, path):
            self.path = Path(path)
            self.name = name if name is not None else self.path.name
            self.path.mkdir(parents=True, exist_ok=True)
            return self
    def remove(self, path): 
        path = Path(path)
        shutil.rmtree(path)
        return self
