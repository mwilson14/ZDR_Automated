from tkinter import *
from algorithm_framework_realtime_auto import multi_case_algorithm_ML1_realtime

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("ZDR Arc Algorithm")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)
        
        # creating a button instance
        realtimeButton = Button(self, text="Run Realtime",command=self.launch_realtime)

        # placing the button on my window
        quitButton.place(x=0, y=320)
        
        realtimeButton.place(x=0, y=280)

        #Add a label at the top of the algorithm
        L0 = Label(self, text = "Core Algorithm Settings")
        L0.pack()
        L0.place(x=150, y=5)
        
        #Add a label for storm tracking settings
        La = Label(self, text = "Tracking Algorithm Settings (Optional)")
        La.pack()
        La.place(x=150, y=110)
        
        #Add entry for the first tracking threshold
        L3 = Label(self, text = "Z Threshold 1")
        L3.pack()
        L3.place(x=0, y=140)
        
        #Add a data entry window
        self.entrythingy3 = Entry()
        self.entrythingy3.pack()
        self.entrythingy3.place(x=150, y=140)

        # here is the application variable
        self.contents3 = StringVar()
        # set it to some value
        self.contents3.set("45")
        # tell the entry widget to watch this variable
        self.entrythingy3["textvariable"] = self.contents3
        
        #Add entry for the second tracking threshold
        L4 = Label(self, text = "Z Threshold 2")
        L4.pack()
        L4.place(x=0, y=170)
        
        #Add a data entry window
        self.entrythingy4 = Entry()
        self.entrythingy4.pack()
        self.entrythingy4.place(x=150, y=170)

        # here is the application variable
        self.contents4 = StringVar()
        # set it to some value
        self.contents4.set("50")
        # tell the entry widget to watch this variable
        self.entrythingy4["textvariable"] = self.contents4
        
        #Add entry for big storm area
        L5 = Label(self, text = "Big Storm Area (sq. km)")
        L5.pack()
        L5.place(x=0, y=200)
        
        #Add a data entry window
        self.entrythingy5 = Entry()
        self.entrythingy5.pack()
        self.entrythingy5.place(x=150, y=200)

        # here is the application variable
        self.contents5 = StringVar()
        # set it to some value
        self.contents5.set("300")
        # tell the entry widget to watch this variable
        self.entrythingy5["textvariable"] = self.contents5

          #Add entry for ZDR Calibration
        L12 = Label(self, text = "ZDR Calibration (dB) \n (Optional)")
        L12.pack()
        L12.place(x=0, y=70)
        
        #Add a data entry window
        self.entrythingy12 = Entry()
        self.entrythingy12.pack()
        self.entrythingy12.place(x=150, y=70)

        # here is the application variable
        self.contents12 = StringVar()
        # set it to some value
        self.contents12.set("0.0")
        # tell the entry widget to watch this variable
        self.entrythingy12["textvariable"] = self.contents12
        
          #Add entry for radar site
        L13 = Label(self, text = "Radar Site")
        L13.pack()
        L13.place(x=0, y=40)
        
        #Add a data entry window
        self.entrythingy13 = Entry()
        self.entrythingy13.pack()
        self.entrythingy13.place(x=150, y=40)

        # here is the application variable
        self.contents13 = StringVar()
        # set it to some value
        self.contents13.set("")
        # tell the entry widget to watch this variable
        self.entrythingy13["textvariable"] = self.contents13
        
          #Add entry for storm motion
        L14 = Label(self, text = "Storm Motion (deg)")
        L14.pack()
        L14.place(x=0, y=230)
        
        #Add a data entry window
        self.entrythingy14 = Entry()
        self.entrythingy14.pack()
        self.entrythingy14.place(x=150, y=230)

        # here is the application variable
        self.contents14 = StringVar()
        # set it to some value
        self.contents14.set("225")
        # tell the entry widget to watch this variable
        self.entrythingy14["textvariable"] = self.contents14

    def client_exit(self):
        exit()
        
    def print_stuff(self):
        data3 = float(self.contents3.get())
        print(data3, 'Z Threshold 1 (dBZ)')
        data4 = float(self.contents4.get())
        print(data4, 'Z Threshold 2 (dBZ)')
        data5 = float(self.contents5.get())
        print(data5, 'Big Storm Area (sq. km)')
        data12 = float(self.contents12.get())
        print(data12, 'ZDR Calibration')
        data13 = str(self.contents13.get())
        print(data13, 'Radar Site')
        data14 = str(self.contents14.get())
        print(data14, 'Storm Motion (deg)')

    def launch_realtime(self):
        z1 = float(self.contents3.get())
        print(z1, 'Z Threshold 1 (dBZ)')
        z2 = float(self.contents4.get())
        print(z2, 'Z Threshold 2 (dBZ)')
        bs1 = float(self.contents5.get())
        print(bs1, 'Big Storm Area (sq. km)')
        zdr_cal = float(self.contents12.get())
        print(zdr_cal, 'ZDR Calibration')
        site = (self.contents13.get())
        print(site, 'Radar Site')
        storm_motion = float(self.contents14.get())
        print(storm_motion, 'Storm Motion (deg)')

        print(" ")
        print('Running Algorithm')

        tracks_dataframe, zdroutlines = multi_case_algorithm_ML1_realtime(z1,z2,bs1,2,
                                                                zdr_cal,station=site, Bunkers_m=storm_motion, track_dis=10)

        #tracks_dataframe.to_pickle('ARCDEV_GUI_AUTO'+str(year1)+str(month1)+str(day1)+str(site)+'.pkl')

        
# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x400")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop()  