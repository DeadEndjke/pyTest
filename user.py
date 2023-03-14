
class User:
    id = 0
    def __init__(self, key, lang):
        self.__key = key
        self.__lang = lang
        self.__id = self.incr()
        

    @classmethod
    def incr(self):
        self.id += 1
        return self.id


    @property
    def get_id(self):
        return self.__id
    
    def set_id(self,id):
        self.__id = id

    @property
    def key(self):
        return self.__key
    
    @property
    def lang(self):
        return self.__lang
    

    


