from string import ascii_lowercase, ascii_uppercase

from abc import ABCMeta, abstractmethod


class Prefixer(metaclass=ABCMeta):
    @abstractmethod
    def add(self, option, idx):
        pass

class UpperCasePrefixer(Prefixer):
    def add(self, option, idx):
        return f"{ascii_uppercase[idx]}. {option.strip()}"
    
class LowerCasePrefixer(Prefixer):
    def add(self, option, idx):
        return f"{ascii_lowercase[idx]}. {option.strip()}"
    
class NumberPrefixer(Prefixer):
    def add(self, option, idx):
        return f"{idx}. {option.strip()}"    