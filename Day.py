import tkinter as tk
from tkinter import ttk
from todayInfo import todayInfo

class Day(tk.Tk):
    def __init__(self,NumberDay,monthNumber):
        self.monthlist = ["spacerBecauseIneeditoritdoesntwork","January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October","Novemeber", "December"]

        super().__init__()
        self.Numberday = NumberDay
        self.monthNumber = monthNumber
        
        #Declaring variables for the text entry boxes 
        self.totalCalories = tk.StringVar()
        self.totalPushUps = tk.StringVar()
        self.totalSitUps = tk.StringVar()
        self.totalPullUps = tk.StringVar()

        self.dateInfo = todayInfo(NumberDay,monthNumber,)
        self.screenmaker(350,200)
        

        #sets the dimensions of the window
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=3)



        #Creates 2 Labels that display the data and data type, an entry box, and a button the enter the information

        #Water Amount _______________________________________
        self.waterAmount_label = ttk.Label(self, text="Water:")
        self.waterAmount_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.waterAmountNumber_label = ttk.Label(self, text=self.dateInfo.waterAmount)
        self.waterAmountNumber_label.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        self.waterAmount_entry = ttk.Entry(self,textvariable=self.waterAmount)
        self.waterAmount_entry.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)
        self.waterAmount_entry.focus()

        self.waterAmount_button = ttk.Button(self, text="Add", command=self.waterButtonPressed )
        self.waterAmount_button.grid(column=3, row=0, sticky=tk.EW, padx=5, pady=5)


        # #Calories Amount _______________________________________
        self.totalCalories_label = ttk.Label(self, text="Calories:")
        self.totalCalories_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.totalCaloriesNumber_label = ttk.Label(self, text=self.dateInfo.totalCalories)
        self.totalCaloriesNumber_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        self.totalCalories_entry = ttk.Entry(self,textvariable= self.totalCalories)
        self.totalCalories_entry.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)

        self.totalCalories_button = ttk.Button(self, text="Add", command=self.calorieButtonPressed )
        self.totalCalories_button.grid(column=3, row=1, sticky=tk.EW, padx=5, pady=5)


        # #Push Ups Amount _______________________________________
        self.totalPushUps_label = ttk.Label(self, text="Push Ups:")
        self.totalPushUps_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.totalPushUpsNumber_label = ttk.Label(self, text=self.dateInfo.pushUps)
        self.totalPushUpsNumber_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        self.totalPushUps_entry = ttk.Entry(self,textvariable=self.totalPushUps)
        self.totalPushUps_entry.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)

        self.totalPushUps_button = ttk.Button(self, text="Add", command=self.pushUpsButtonPressed )
        self.totalPushUps_button.grid(column=3, row=2, sticky=tk.EW, padx=5, pady=5)

        # #Sit Ups Amount _______________________________________
        self.totalsitUps_label = ttk.Label(self, text="Sit Ups:")
        self.totalsitUps_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        self.totalsitUpsNumber_label = ttk.Label(self, text=self.dateInfo.sitUps)
        self.totalsitUpsNumber_label.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        self.totalsitUps_entry = ttk.Entry(self,textvariable=self.totalSitUps)
        self.totalsitUps_entry.grid(column=2, row=3, sticky=tk.E, padx=5, pady=5)

        self.totalsitUps_button = ttk.Button(self, text="Add", command=self.sitUpsButtonPressed )
        self.totalsitUps_button.grid(column=3, row=3, sticky=tk.EW, padx=5, pady=5)

        # #Pull Ups Amount _______________________________________
        self.totalPullUps_label = ttk.Label(self, text="Pull Ups:")
        self.totalPullUps_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

        self.totalPullUpsNumber_label = ttk.Label(self, text=self.dateInfo.pullUps)
        self.totalPullUpsNumber_label.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)


        self.totalPullUps_entry = ttk.Entry(self,textvariable=self.totalPullUps)
        self.totalPullUps_entry.grid(column=2, row=4, sticky=tk.E, padx=5, pady=5)

        self.totalPullUps_button = ttk.Button(self, text="Add", command=self.pullUpsButtonPressed )
        self.totalPullUps_button.grid(column=3, row=4, sticky=tk.EW, padx=5, pady=5)


        
    def screenmaker(self,window_width, window_height):
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title(self.monthlist[self.monthNumber] + " " + str(self.Numberday) + " Info")
        self.resizable(0, 0)
        self.columnconfigure(0, weight=0)
        self.iconbitmap('Images\\table.ico')


   
    #Functions that are ran when the respective button is pressed 

    def waterButtonPressed(self):
        self.dateInfo.addWater(int(self.waterAmount.get()))
        self.dateInfo.writeToFile()
        self.waterAmountNumber_label.destroy()
        self.waterAmountNumber_label = ttk.Label(self, text=self.dateInfo.waterAmount)
        self.waterAmountNumber_label.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

    def calorieButtonPressed(self):
        self.dateInfo.addCalories(int(self.totalCalories.get()))
        self.dateInfo.writeToFile()
        self.totalCaloriesNumber_label.destroy()
        self.totalCaloriesNumber_label = ttk.Label(self, text=self.dateInfo.totalCalories)
        self.totalCaloriesNumber_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    
    def pushUpsButtonPressed(self):
        self.dateInfo.addPushUps(int(self.totalPushUps.get()))
        self.dateInfo.writeToFile()
        self.totalPushUpsNumber_label.destroy()
        self.totalPushUpsNumber_label = ttk.Label(self, text=self.dateInfo.pushUps)
        self.totalPushUpsNumber_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

    def sitUpsButtonPressed(self):
        self.dateInfo.addSitUps(int(self.totalSitUps.get()))
        self.dateInfo.writeToFile()
        self.totalsitUpsNumber_label.destroy()
        self.totalsitUpsNumber_label = ttk.Label(self, text=self.dateInfo.sitUps)
        self.totalsitUpsNumber_label.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

    def pullUpsButtonPressed(self):
        self.dateInfo.addPullUps(int(self.totalPullUps.get()))
        self.dateInfo.writeToFile()
        self.totalPullUpsNumber_label.destroy()
        self.totalPullUpsNumber_label = ttk.Label(self, text=self.dateInfo.pullUps)
        self.totalPullUpsNumber_label.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

