#
#Read Readme first if cannot run the code
#
#
#Order to read files
#main.py -> mainMeny.py -> Calender.py -> Day.py -> dayArray.py -> dataClass.py 


# Data type class
# contains name and value
# has a function to change the function 
# has a function to return the name and value in a format to be written to a file
class dataClass():
    def __init__(self, nameIn,valueIn):
        self.name = nameIn
        self.value = valueIn

    def stringgGetter(self):
        return(str(self.name) + "," + str(self.value) )

    def changeValue(self,newValue):
        self.value = newValue

