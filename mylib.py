class requirement:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def reqFun(self):
        print(self.name)
        print(self.type)

class safRequirement(requirement):
    def __init__(self, name, type):
        requirement.__init__(self, name, type)
        self.type = "SafetyRequirement"
        self.ASIL = "QM"
    
def myFun(name,reqtype,ASIL):
    req1 = safRequirement(name,reqtype)
    if type(name) == type(""):
        req1.reqFun()
        req1.ASIL = "D"
        print(req1.ASIL)
    else:
        print("not valid req name")
