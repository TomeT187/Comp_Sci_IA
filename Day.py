import tkinter as tk
from tkinter import ttk
from dayArray import dayArray
from tkinter import StringVar

class Day(tk.Tk):
    def __init__(self,NumberDayIn,monthNumberIn):
        super().__init__()
        self.monthlist = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October","Novemeber", "December"]
        self.objectArray = []
        self.Numberday = NumberDayIn
        self.monthNumber = monthNumberIn
        self.screenmaker(500,500)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=3)
        self.todayArray = dayArray(NumberDayIn,monthNumberIn)

        backButton = ttk.Button(self, text="Back to Calendar",command=lambda: self.openCalendar())
        backButton.grid(column=0,row=0,padx=5, pady=5,sticky=tk.W )#
        
        addButton = ttk.Button(self, text="Add Type",command=lambda: print("hi"))
        addButton.grid(column=3,row=0,sticky=tk.E,padx=5, pady=5)

        headerTypeLabel = ttk.Label(self,text="Type",)    
        headerTypeLabel.grid(column=0,row=1,sticky=tk.W,padx=5, pady=5)    

        headerAmountLabel = ttk.Label(self,text="Amount",)
        headerAmountLabel.grid(column=1,row=1,padx=5, pady=5,sticky=tk.W,)

        headerEntryLabel = ttk.Label(self,text="Set Amount")
        headerEntryLabel.grid(column=2,row=1,padx=5, pady=5,sticky=tk.E)

        

        for i in range(len(self.todayArray.dataClassList)):
            self.objectPlacer(self.todayArray,i)
            

        
        
            
    def objectPlacer(self,dataClassIN,rowNum):
        
        
        #for i in todayArray.dataClassList:

        label = ttk.Label(self, text=dataClassIN.dataClassList[rowNum].name)
        amountLabel = ttk.Label(self, text=dataClassIN.dataClassList[rowNum].value)
        dataStringVar = StringVar()
        amountEntry = ttk.Entry(self,textvariable=dataStringVar)
        addButton = ttk.Button(self, text="Add", command= lambda: self.buttonPressed(dataClassIN,amountEntry,rowNum) )
        #addButton = ttk.Button(self, text="Add", command= lambda: dataClassIN.changeValue(amountEntry.get()))
        
        
        label.grid(column=0,row=rowNum + 2,padx=5, pady=5,sticky=tk.W,)
        amountLabel.grid(column=1,row=rowNum + 2,padx=5, pady=5,sticky=tk.W,)
        amountEntry.grid(column=2,row=rowNum + 2,padx=5, pady=5,sticky=tk.E)
        addButton.grid(column=3,row=rowNum + 2,padx=5, pady=5,sticky=tk.E)

        self.objectArray.append([label,amountLabel,amountEntry,addButton])

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
        self.resizable(0, 0)
        self.columnconfigure(0, weight=0)
        self.iconbitmap('Images\\table.ico')

# test = Day(12,12)
# test.mainloop()

