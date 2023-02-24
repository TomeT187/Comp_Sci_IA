import tkinter as tk
from tkinter import ttk
from todayInfo import todayInfo
from dayArray import dayArray
from tkinter import StringVar

class Day(tk.Tk):
    def __init__(self,NumberDayIn,monthNumberIn):
        super().__init__()
        self.monthlist = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October","Novemeber", "December"]
        self.Numberday = NumberDayIn
        self.monthNumber = monthNumberIn
        self.screenmaker(500,500)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=3)
        todayArray = dayArray(NumberDayIn,monthNumberIn)
        for i in range(len(todayArray.dataClassList)):
            self.objectPlacer(todayArray,i)
            

        
        
            
    def objectPlacer(self,dataClassIN,rowNum):
        
        
        #for i in todayArray.dataClassList:

        label = ttk.Label(self, text=dataClassIN.dataClassList[rowNum].name)
        amountLabel = ttk.Label(self, text=dataClassIN.dataClassList[rowNum].value)
        dataStringVar = StringVar()
        amountEntry = ttk.Entry(self,textvariable=dataStringVar)


        addButton = ttk.Button(self, text="Add", command= lambda: self.buttonPressed(dataClassIN,amountEntry,rowNum) )
        #addButton = ttk.Button(self, text="Add", command= lambda: dataClassIN.changeValue(amountEntry.get()))
        
        label.grid(column=0,row=rowNum,padx=5, pady=5,sticky=tk.W,)
        amountLabel.grid(column=1,row=rowNum,padx=5, pady=5,sticky=tk.W,)
        amountEntry.grid(column=2,row=rowNum,padx=5, pady=5,sticky=tk.E)
        addButton.grid(column=3,row=rowNum,padx=5, pady=5,sticky=tk.E)

    def buttonPressed(self,dataClassIN,entryVarIN,i):
        dataClassIN.dataClassList[i].changeValue(entryVarIN.get())
        dataClassIN.writeInfo()

        


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

