import os

class todayInfo():
    def __init__(self,dayNumber,monthNumber,):

        self.waterAmount = 0
        self.totalCalories = 0
        self.pushUps = 0 #int
        self.sitUps = 0  #int
        self.pullUps = 0 #int
        self.info = [["waterAmount",self.waterAmount],["totalCalories",self.totalCalories],["pushUps",self.pushUps],["sitUps",self.sitUps],["pullUps",self.pullUps]]

        self.monthlist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct","Nov", "Dec"]
        self.dayNumber = dayNumber 
        self.monthNumber = monthNumber

        self.getInfo()

    def getInfo(self):
        while (True):
            try:
                todayFile = open(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber - 1] + "\\" + str(self.dayNumber ) ,"r")

                rawString = todayFile.readline()

                cleanedString = ""
                
                for i in range(len(rawString) -1): #makes a new string that is trimmed
                    cleanedString  += rawString[i+1]

                list = cleanedString.split(",")

                for i in range(len(list)): #gets rid of excess characters
                    list[i] = list[i].strip()
                    list[i] = list[i].strip("[")
                    list[i] = list[i].strip("]")
                    list[i] = list[i].strip("\'")

                for i in range(int(len(list)/2)): #puts values of taken in into object      
                    if list[i*2] == self.info[i][0]:
                        self.info[i][1] = (list[(i*2)+1] ) # info at (i,1) equals int value of taken in value at index of 2 * ****does not cast as int because food list

                self.waterAmount = int(self.info[0][1])
                self.totalCalories = int(self.info[1][1])
                self.pushUps = int(self.info[2][1])
                self.sitUps = int(self.info[3][1])
                self.pullUps = int(self.info[4][1])

                break
            except Exception as e:

                try:
                    os.mkdir(os.getcwd()+ "\\Months\\" + self.monthlist[self.monthNumber - 1])
                    todayFile = open(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber - 1] + "\\" + str(self.dayNumber) ,"w")
                    todayFile.write(str(self.info))
                    todayFile.close()
                    break

                except:
                    todayFile = open(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber - 1] + "\\" + str(self.dayNumber ) ,"w")
                    todayFile.write(str(self.info))
                    todayFile.close()
                    break


    #functions to change the value for each type in the class                    
    def addWater(self,newWater):
        self.waterAmount += newWater
        self.info = [["waterAmount",self.waterAmount],["totalCalories",self.totalCalories],["pushUps",self.pushUps],["sitUps",self.sitUps],["pullUps",self.pullUps]]

    def addCalories(self,amount):
        self.totalCalories += amount
        self.info = [["waterAmount",self.waterAmount],["totalCalories",self.totalCalories],["pushUps",self.pushUps],["sitUps",self.sitUps],["pullUps",self.pullUps]]


    def addPushUps(self,amount):
        self.pushUps+= amount
        self.info = [["waterAmount",self.waterAmount],["totalCalories",self.totalCalories],["pushUps",self.pushUps],["sitUps",self.sitUps],["pullUps",self.pullUps]]

    def addSitUps(self,amount):
        self.sitUps += amount
        self.info = [["waterAmount",self.waterAmount],["totalCalories",self.totalCalories],["pushUps",self.pushUps],["sitUps",self.sitUps],["pullUps",self.pullUps]]

    def addPullUps(self,amount):
        self.pullUps += amount
        self.info = [["waterAmount",self.waterAmount],["totalCalories",self.totalCalories],["pushUps",self.pushUps],["sitUps",self.sitUps],["pullUps",self.pullUps]]


    #Function to write the information to a file based on what day it is
    def writeToFile(self):
        todayFile = open(os.getcwd() + "\\Months\\" + self.monthlist[self.monthNumber- 1] + "\\" + str(self.dayNumber) ,"w")
        todayFile.write(str(self.info))    
        
