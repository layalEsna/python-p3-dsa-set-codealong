class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        if value in self.dictionary:
            return True
        return False
    def add(self, value):
        if value not in self.dictionary:
            self.dictionary[value] = True
            return self.dictionary
        
    def delete(self, value):
        if value in self.dictionary:
            del self.dictionary[value]
        return self.dictionary
    def size(self):
        return len(self.dictionary)
    def clear(self):
        self.dictionary.clear()

