import tkinter as tk
from tkinter import ttk
import datetime
from math import floor





class Calender(tk.Tk,):

    def __init__(self,nameofthemonth):
        super().__init__()
        self.nameofthemonth = nameofthemonth
        self.columnnumber = 0
        self.rownumber = 0
        self.monthlist = ["","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October","Novemeber", "December"]
        self.weekList = ("Sunday","Monday", "Tuesday", "Wednessday","Thursday", "Friday","Saturday")

        
        self.screenmaker(self,985,500)
        self.CalenderMaker()
        menuBar = tk.Menu(self)
        self.config(menu=menuBar)

        file_menu = tk.Menu(menuBar)

        # add a menu item to the menu
        file_menu.add_command(label='Month Select',command=self.mainMenuOpen)

        # add the File menu to the menubar
        menuBar.add_cascade(label="Months",menu=file_menu)

    def mainMenuOpen(self):
        self.destroy()
        from mainMenu import mainMenu
        MainMenu = mainMenu()
        MainMenu.mainloop()


    
    def screenmaker(self,root,window_width, window_height):
        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        root.title('Calender')
        root.resizable(0, 0)
        root.columnconfigure(0, weight=0)
        monthname = "{}"
        Calender_label = ttk.Label(root,text=monthname.format(self.monthlist[self.nameofthemonth]), font=("Comic Sans", 20),)
        Calender_label.grid(column=3, row=0,sticky=tk.NS,)
        root.iconbitmap('Images\\calender.ico')


    def DayObjectMaker(self,dayNumber):
        from Day import Day
        self.destroy()
        thisDay = Day(dayNumber,self.nameofthemonth) 
        thisDay.mainloop()

    def CalenderMaker(self):
        for i in range(7):
            Day_label = ttk.Label(self, text=self.weekList[i],)
            Day_label.grid(column=i+0, row=1, )
            
        #Creates Button object named day button which is then placed     
        def dayButtonMaker(i):
            dayButton = ttk.Button(self, text="\n" + str( i ) + "\n",width=20,command = lambda: self.DayObjectMaker(i))
            dayButton.grid(column=self.columnnumber, row=self.rownumber+2, padx= 5, pady =5)

        def spacingChecker():
            #if button is at the end place button at begining of row underneath
            if (self.columnnumber == 6):
                self.columnnumber = 0
                self.rownumber += 1
            # If not place it one forward
            else:
                self.columnnumber += 1
        #Function that combines the button placer and spacing checker, takes in the number of the day
        def ButtonPlacer(ii):
            dayButtonMaker(ii)
            spacingChecker()

        todaysDate = datetime.datetime.now()

        #Used to get a number for the month used by the equation for finding the First Day of the month
        if (self.nameofthemonth == 1):
            todaysYear = int(todaysDate.strftime("%y")) - 1
            numberYear = 11
        elif ((self.nameofthemonth == 2)):
            todaysYear = int(todaysDate.strftime("%y")) - 1
            numberYear = 12
        else:
            todaysYear = int(todaysDate.strftime("%y"))
            numberYear = self.nameofthemonth - 2

        #Determines what day the first of the month is
        FirstDay = (floor(2.6 * (numberYear) - 0.2) - 34 + todaysYear + floor(todaysYear/4) ) % 7

        #Places Empty Labels as Placeholder
        for i in range(FirstDay):
            spacerLabel = ttk.Label(self)
            spacerLabel.grid(column = self.columnnumber, row = self.rownumber + 2)
            self.columnnumber += 1
        
        #Places 28 days on the calendar
        for i in range(28):
            ButtonPlacer(i+1)

        #Places the remain days on the calendar based on if there are 30 or 31 days in the month
        if (self.nameofthemonth == 2):
            pass
        elif (self.nameofthemonth == 1):
            ButtonPlacer(29)
            ButtonPlacer(30)
            ButtonPlacer(31)
        elif (self.nameofthemonth%2 == 1):
            if (self.nameofthemonth < 8):
                ButtonPlacer(29)
                ButtonPlacer(30)
                ButtonPlacer(31)
            else:
                ButtonPlacer(29)
                ButtonPlacer(30)
        elif (self.nameofthemonth %2 == 0):
            if self.nameofthemonth < 7:
                ButtonPlacer(29)
                ButtonPlacer(30)
            else:
                ButtonPlacer(29)
                ButtonPlacer(30)
                ButtonPlacer(31)




