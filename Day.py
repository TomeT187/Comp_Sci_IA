#
#Read Readme first if cannot run the code
#
#
#Order to read files
#main.py -> mainMeny.py -> Calender.py -> Day.py -> dayArray.py -> dataClass.py 

import tkinter as tk
from tkinter import ttk
from dayArray import dayArray
from tkinter import StringVar
from Presets import presets


#Displays data from each day
#Allows the User to enter new data types, edit old data types, and delete old data types
class Day(tk.Tk):
    def __init__(self,NumberDayIn,monthNumberIn):
        super().__init__()
        self.monthlist = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October","Novemeber", "December"]
        self.objectArray = []
        self.presetObjectArray = []
        self.Numberday = NumberDayIn
        self.monthNumber = monthNumberIn
        self.screenmaker(1000,700)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=3)
        self.todayArray = dayArray(NumberDayIn,monthNumberIn)
        self.presets = presets()


       

        backButton = ttk.Button(self, text="Back to Calendar",command=lambda: self.openCalendar())
        backButton.grid(column=0,row=0,padx=5, pady=5,sticky=tk.W )#
        
        

        newTypeLabel = ttk.Label(self, text="New Type")
        newTypeLabel.grid(column=5,row=0,sticky=tk.W,padx=20, pady=5)

        addButton = ttk.Button(self, text="Add Type",command=lambda: self.AddType())
        addButton.grid(column=5,row=1,sticky=tk.W,padx=20, pady=5)

        newTypeEntryLabel = ttk.Label(self,text="Enter Name" )
        newTypeEntryLabel.grid(column=5,row=2,sticky=tk.W,padx=20, pady=5)

        self.newTypeInVar = StringVar()
        newTypeEntry = ttk.Entry(self,textvariable=self.newTypeInVar)
        newTypeEntry.grid(column=5,row=3,sticky=tk.W,padx=20, pady=5)

        newAmountLabel = ttk.Label(self,text="Enter Amount")
        newAmountLabel.grid(column=5,row=4,sticky=tk.W,padx=20, pady=5)

        self.newAmountVar = StringVar()
        newAmountEntry = ttk.Entry(self,textvariable=self.newAmountVar)
        newAmountEntry.grid(column=5,row=5,sticky=tk.W,padx=20, pady=5)




        addPresetLabel = ttk.Label(self,text="Add Preset")
        addPresetLabel.grid(column=6,row=0,padx=20, pady=5,sticky=tk.W)

        addPresetButton = ttk.Button(self,command=lambda: self.newPresetButtonPressed() ,text="Create Preset")
        addPresetButton.grid(column=6,row=1,padx=20, pady=5,sticky=tk.W)

        newPresetEntryLabel = ttk.Label(self,text="Enter New Type")
        newPresetEntryLabel.grid(column=6,row=2,sticky=tk.W,padx=20, pady=5)

        self.newPresetVar = StringVar()
        newPresetEntry = ttk.Entry(self,textvariable=self.newPresetVar)
        newPresetEntry.grid(column=6,row=3,padx=20, pady=5,sticky=tk.W)

        for self.j in range(len(self.presets.presetArray)):
            self.addPresets(self.j)
        
    


        headerTypeLabel = ttk.Label(self,text="Type",)    
        headerTypeLabel.grid(column=0,row=1,sticky=tk.W,padx=5, pady=5)    

        headerAmountLabel = ttk.Label(self,text="Amount",)
        headerAmountLabel.grid(column=1,row=1,padx=5, pady=5,sticky=tk.W,)

        enterBoxLabel = ttk.Label(self,text="Enter New Amount")
        enterBoxLabel.grid(column=2,row=1,padx=5, pady=5,sticky=tk.E)

        headerEntryLabel = ttk.Label(self,text="Set Amount")
        headerEntryLabel.grid(column=3,row=1,padx=5, pady=5,sticky=tk.E)

        removeLabel = ttk.Label(self,text="Remove Data")
        removeLabel.grid(column=4,row=1,padx=5, pady=5,sticky=tk.E)

        

        for self.i in range(len(self.todayArray.dataClassList)):
            self.objectPlacer(self.todayArray,self.i)
            

        
    def AddType(self):
        self.todayArray.addDataType(self.newTypeInVar.get(),self.newAmountVar.get())
        self.todayArray.writeInfo()
        self.destroyObjects()
        for i in range(len(self.todayArray.dataClassList)):
            self.objectPlacer(self.todayArray,i)


    def addPresets(self,rowNum):
        newPresetButton = ttk.Button(self,command= lambda: self.addPresetButtonPressed(self.presets.presetArray[rowNum]), text= self.presets.presetArray[self.j])
        newPresetButton.grid(column=6,row= 4 + rowNum ,padx=20, pady=5,sticky=tk.W)
        self.presetObjectArray.append(newPresetButton)


    def addPresetButtonPressed(self,nameIn):
        print(nameIn)
        self.todayArray.addDataType(nameIn,"")
        self.todayArray.writeInfo()
        self.destroyObjects()
        for i in range(len(self.todayArray.dataClassList)):
            self.objectPlacer(self.todayArray,i)


    def newPresetButtonPressed(self):
        self.presets.addPreset(self.newPresetVar.get())
        for i in self.presetObjectArray:
            i.destroy()
        for self.j in range(len(self.presets.presetArray)):
            self.addPresets(self.j)

            
    def objectPlacer(self,dataClassIN,rowNum):
        
        
        #for i in todayArray.dataClassList:

        label = ttk.Label(self, text=dataClassIN.dataClassList[rowNum].name,font="Helvetica 12 bold")
        amountLabel = ttk.Label(self, text=dataClassIN.dataClassList[rowNum].value,font="Helvetica 12 bold")
        dataStringVar = StringVar()
        amountEntry = ttk.Entry(self,textvariable=dataStringVar)
        addButton = ttk.Button(self, text="Set", command= lambda: self.buttonPressed(dataClassIN,amountEntry,rowNum) )
        deleteButton = ttk.Button(self,text="X", command= lambda: self.deleteButtonPressed(dataClassIN,rowNum))
        #addButton = ttk.Button(self, text="Add", command= lambda: dataClassIN.changeValue(amountEntry.get()))
        
        
        label.grid(column=0,row=rowNum + 2,padx=5, pady=5,sticky=tk.W,)
        amountLabel.grid(column=1,row=rowNum + 2,padx=5, pady=5,sticky=tk.W,)
        amountEntry.grid(column=2,row=rowNum + 2,padx=5, pady=5,sticky=tk.E)
        addButton.grid(column=3,row=rowNum + 2,padx=5, pady=5,sticky=tk.E)
        deleteButton.grid(column=4,row=rowNum + 2, padx=5, pady=5,sticky=tk.E)

        self.objectArray.append([label,amountLabel,amountEntry,addButton,deleteButton])

    def destroyObjects(self):
        for i in self.objectArray:
            for j in i:
                j.destroy()

    def buttonPressed(self,dataClassIN,entryVarIN,i):
        dataClassIN.dataClassList[i].changeValue(entryVarIN.get())
        dataClassIN.writeInfo()
        self.destroyObjects()
        for i in range(len(self.todayArray.dataClassList)):
            self.objectPlacer(self.todayArray,i)


############################


    def deleteButtonPressed(self,dataClassIN,i):
        dataClassIN.removeType(dataClassIN.dataClassList[i])
        #print(dataClassIN.dataClassList[i])
        dataClassIN.writeInfo()
        self.destroyObjects()
        for i in range(len(self.todayArray.dataClassList)):
            self.objectPlacer(self.todayArray,i)

############################
        
    def openCalendar(self):
        from Calender import Calender
        self.destroy()
        newCalendar = Calender(self.monthNumber)
        newCalendar.mainloop()

    def screenmaker(self,window_width, window_height):
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title(self.monthlist[self.monthNumber -1 ] + " " + str(self.Numberday) + " Info")
        self.resizable(1, 1)
        self.columnconfigure(0, weight=0)
        self.iconbitmap('Images\\table.ico')

# test = Day(12,12)
# test.mainloop()

