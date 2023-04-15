#
#Read Readme first if cannot run the code
#
#
#Order to read files
#main.py -> mainMeny.py -> Calender.py -> Day.py -> dayArray.py -> dataClass.py 

import tkinter as tk
from tkinter import ttk
from Calender import Calender


#First Screen User is shown, creates a drop down menu for the user to select a month
class mainMenu(tk.Tk):

    def __init__(self):
        super().__init__()
        self.monthlist = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October","Novemeber", "December"]
        self.option_var = tk.StringVar(self)


        self.screenMaker(400,350)
        self.createDropDown()

    # Function used in initiation of a window
    # Uses functions to set specific aspects of the window
    def screenMaker(self,window_width, window_height):
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title("Welcome")
        #self.resizable(0, 0)
        self.columnconfigure(0, weight=0)
        self.iconbitmap('Images\\weight.ico')


    #function the places a drop down menu with options of each month in monthlist
    def createDropDown(self):
        paddings = {'padx': 5, 'pady': 5}
        label = ttk.Label(self,  text='Select the Month:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)
        def optionSelected(a):
            self.destroy() 
            for i in range(len(self.monthlist)):
                if a == self.monthlist[i]:
                    thisMonth = Calender(i+1)
                    thisMonth.mainloop()
                    
        option_menu = ttk.OptionMenu(self,self.option_var,self.monthlist[0],*self.monthlist,command = optionSelected,)
        option_menu.grid(column=1, row=0, sticky=tk.W, )


    
