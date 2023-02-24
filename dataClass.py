
from tkinter import ttk

class dataClass():
    def __init__(self, nameIn,valueIn):
        self.name = nameIn
        self.value = valueIn

    def stringgGetter(self):
        return(str(self.name) + "," + str(self.value) )

    def changeValue(self,a):
        self.value = a

#add ttk variable to this class so one is made 