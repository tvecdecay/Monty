import subprocess

class program:
    def __init__(self, narr = []):
        self.name = narr[0]
        self.path = narr[1]
        if narr[2]:
            try:
                subprocess.run(narr[1])
            except:
                raise Exception("Program Error: Given path is not valid.")
    
    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__path

    @name.setter
    def name(self, sname):
        self.__name = sname

    @path.setter
    def path(self, spath):
        self.__path = spath

    def start(self):
        try:
            subprocess.run(self.__path)
        except:
            raise Exception("Program Error: Given path is not valid.")