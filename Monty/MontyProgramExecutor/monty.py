import objclass

class command:
    def __init__(self, cmdstr, execinstant=False):
        self.mstr = cmdstr
        if execinstant:
            self.execute()

    @property
    def mstr(self):
        return self.__mstr

    @mstr.setter
    def mstr(self, cmd):
        self.__mstr = cmd

    def execute(self):
        try:
            tokenent1 = self.__mstr.split(' ')
            decidertoken = tokenent1[0]
            opparr = []
            if decidertoken not in ["prog", "web"]:
                raise Exception
            tokenent1.pop(0)
            if decidertoken == "prog":
                for token in range(len(tokenent1)):
                    tokenent1[token] = tokenent1[token].replace('|', ' ')
                    opparr.append(tokenent1[token])
                opparr.append(True)
                objclass.program(opparr) 
            if decidertoken == "web":
                for token in range(len(tokenent1)):
                    opparr.append(tokenent1[token])
                opparr.append(True)
                objclass.website(opparr)
        except:
            raise Exception(f"Command Error: {self.__mstr} is not a valid command.")

    def givename(self):
        tokens = self.__mstr.split()
        if len(tokens) == 3:
            return tokens[1]
        return "error"