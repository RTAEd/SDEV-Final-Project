# Tutorisl at https://realpython.com/python-gui-tkinter/

import tkinter as tk
import time

# Set window config
window = tk.Tk()
window.title("Kitchen Timer")
window.rowconfigure([0,1,2,3,4, 5], minsize=15)
window.columnconfigure([0, 1, 2, 3, 4], minsize=25)

# Set Values
seconds = tk.StringVar()
seconds.set("00")
minutes = tk.StringVar()
minutes.set("00")
hours = tk.StringVar()
hours.set("00")


# Create Widgets

# Labels
hoursLbl = tk.Label(text="Hours")
minutesLbl = tk.Label(text="Minutes")
secondsLbl = tk.Label(text="Seconds")

# Entry
hoursEnt = tk.Entry(textvariable=hours)
minutesEnt = tk.Entry(textvariable=minutes)
secondssEnt = tk.Entry(textvariable=seconds)

# Arrange widgets in grid
hoursLbl.grid(row=1, column=0, sticky=tk.NSEW, pady=2)
minutesLbl.grid(row=1, column=2, sticky=tk.NSEW,pady=2)
secondsLbl.grid(row=1, column=4, sticky=tk.NSEW,pady=2)

hoursEnt.grid(row=2, column=0, sticky=tk.NSEW,pady=2, padx=10)
minutesEnt.grid(row=2, column=2, sticky=tk.NSEW,pady=2)
secondssEnt.grid(row=2, column=4, sticky=tk.NSEW,pady=2, padx=10)

# Timer Code
def timer():
   totalSeconds = int(hours.get())*3600 + int(minutes.get())*60 + int(seconds.get())

   while totalSeconds > - 1:
      convertedMinute = totalSeconds // 60
      convertedSecond = totalSeconds % 60
      converterHour = 0

      if convertedMinute > 60:
         convertedHour = convertedMinute // 60
         convertedMinute = convertedMinute % 60

      seconds.set(convertedSecond)
      minutes.set(convertedMinute)
      hours.set(converterHour)

      #Update the time
      window.update()
      time.sleep(1)

      if(totalSeconds == 0):
         seconds.set(00)
         minutes.set(00)
         hours.set(00)
      totalSeconds -= 1
      #TODO: add code to display that the timer is up. 
      # I can't figue out how to play a sound using standard library

def quitTimer():
    window.destroy()
    window.quit()   

# buttons
startBtn = tk.Button(text="Start", width=25, command=timer)
quitBtn = tk.Button(text="Quit", width=25, command=quitTimer)
# Button locations
startBtn.grid(row=4, column=0, columnspan=2,   pady=2, padx=15)
quitBtn.grid(row=4, column=3, columnspan=2,  pady=2, padx=15)

window.mainloop()
