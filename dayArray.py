import os
from dataClass import dataClass
#only use to sort dataClass objects into the day by arrays
# and to read/write to files

#reads a file specific to a day
# retrieves information for data types and places creates a dataClass class which is places into a list 
#Contains functions to add, edit and delete data
class dayArray():
    def __init__(self,dayNumberIn, monthNumberIn):
        self.dayNumber = dayNumberIn
        self.monthNumber = monthNumberIn
        self.monthlist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct","Nov", "Dec"]
        self.dataClassList = []
        self.getInfo()

    def getInfo(self):
        
        #check to see if file exists and then create or open it 
        
        if (os.path.exists(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber - 1] + "\\" + str(self.dayNumber ) + ".txt")): #if file and folder exists
            todayFile = open(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber - 1] + "\\" + str(self.dayNumber ) + ".txt","r")
            self.dataClassList = []
            for i in todayFile:
                if i != "\n": 
                    x = i.split(",")
                    tempDataClass = dataClass(x[0],x[1])
                    self.dataClassList.append(tempDataClass)
            todayFile.close()

        elif(os.path.exists(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber - 1])): # if folder exists but not file
            f = open(os.getcwd()+ "\\Months\\" + self.monthlist[self.monthNumber - 1] + "\\" + str(self.dayNumber ) + ".txt", "x")
            f.close()
            self.getInfo()
            
        else: #if nothing exists
            os.mkdir(os.getcwd()+ "\\Months\\" + self.monthlist[self.monthNumber - 1])
            self.getInfo()
            

    def writeInfo(self):
        todayFile = open(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber - 1] + "\\" + str(self.dayNumber ) + ".txt","w")
        for i in self.dataClassList:
            todayFile.write(i.stringgGetter() + "\n")

    def addDataType(self,nameIn,valueIn):
        tempDataClass = dataClass(nameIn,valueIn)
        self.dataClassList.append(tempDataClass)



    def changeDataValue(self,nameIn,newValue):
        for i in self.dataClassList:
            if i.name == nameIn:
                i.value =newValue

    def removeType(self,nameIn):
        
        for i in self.dataClassList:
            #print(i)
            if i == nameIn:
                self.dataClassList.remove(i)


    #for testing
    def test(self,a):
        print(a)


            




            
            


# test = dayArray(12,12)
# test.getInfo()
# test.changeDataValue("abc", "0")
# #test.addDataType("abc", "999888999")
# test.writeInfo()


# #print(len(test.dataClassList))
# # print("nothing")
# # test.addDataType("abcd",2)
# # print("added to list")
# # test.writeInfo()
# # print("written to file")
# # test.getInfo()


