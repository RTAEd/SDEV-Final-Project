"""
File: kitchenAssistant.py

This application prodides the ability to convert common kitchen 
measurements and provides a simple kitchen timer. 
"""
import tkinter as tk
import time
from tkinter.font import BOLD
import winsound
from PIL import ImageTk, Image
from tkinter import messagebox


class TimerWindow(tk.Toplevel):
    """A kitchen timer that will play a sound (if using windows)"""

    def __init__(self, parent):
        super().__init__(parent)

        # Define Window geometry and name
        self.geometry("300x300")
        self.resizable(False, False)
        self.title("Kitchen Timer")

        # Import images
        self.timerPix = ImageTk.PhotoImage(Image.open("timer.jpg"))

        # Initialzie variables used in the timer
        seconds = tk.StringVar()
        seconds.set("00")
        minutes = tk.StringVar()
        minutes.set("00")
        hours = tk.StringVar()
        hours.set("00")

        # Define and set widgets for kitchen timer labels and entry fields
        self.timerPixLabel = tk.Label(self, image=self.timerPix).place(x=0, y=0)
        self.title = tk.Label(self, text="Kitchen Timer").place(x=115, y=180)
        self.hoursLbl = tk.Label(self, text="Hours").place(x=20, y=210)
        self.minutesLbl = tk.Label(self, text="Minutes").place(x=120, y=210)
        self.secondsLbl = tk.Label(self, text="Seconds").place(x=220, y=210)

        self.hoursEnt = tk.Entry(self, textvariable=hours, width=10).place(x=20, y=230)
        self.minutesEnt = tk.Entry(self, textvariable=minutes, width=10).place(
            x=120, y=230
        )
        self.secondssEnt = tk.Entry(self, textvariable=seconds, width=10).place(
            x=220, y=230
        )

        def timer():
            """Timer calculates the total seconds to provide range for countdown and
            recalculate the number of minutes, seconds and hours for countdown.
            """
            totalSeconds = (
                int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
            )

            while totalSeconds > -1:
                convertedMinute = totalSeconds // 60
                convertedSecond = totalSeconds % 60
                converterHour = 0

                if convertedMinute > 60:
                    convertedHour = convertedMinute // 60
                    convertedMinute = convertedMinute % 60

                seconds.set(convertedSecond)
                minutes.set(convertedMinute)
                hours.set(converterHour)

                # Update the display to show time counting down each second
                tk.Toplevel.update(self)
                time.sleep(1)

                # Defines what to do when timer hits 0
                if totalSeconds == 0:
                    seconds.set(00)
                    minutes.set(00)
                    hours.set(00)

                    try:
                    # Play Windows alert sound. Will not work with mac
                        winsound.PlaySound("SystemAlert", winsound.SND_ALIAS)
                        winsound.PlaySound("SystemAlert", winsound.SND_ALIAS)
                        winsound.PlaySound("SystemAlert", winsound.SND_ALIAS)
                    except:
                        pass

                totalSeconds -= 1

        # button widgets to start the timer and close the window
        self.startTimerBtn = tk.Button(
            self, text="Start", command=timer, width=18
        ).place(x=10, y=265)
        self.closeButton = tk.Button(
            self, text="Close", command=self.destroy, width=18
        ).place(
            x=150, y=265
        )  # expand=true


class App(tk.Tk):
    """Main application window for Kitchen assistant app"""

    def __init__(self):
        super().__init__()

        # Defines the window geometery, color, and title
        self.geometry("400x600")
        self.configure(bg='#FFFFFF')
        self.resizable(False, False)


        self.title("Kitchen Assistant")

        # Import Images
        self.measurePix = ImageTk.PhotoImage(Image.open("measurement.jpg"))
        
        # Place labels and other widgets for the main application window
        self.titleLbl = tk.Label(self, text="Welcome to the Kitchen Assistant", font=('Calibre', 14, 'bold'), bg="White", padx=10, pady=10)
        self.measurePixLbl = tk.Label(self, image=self.measurePix)
        self.convertTitleLbl = tk.Label(self, text="Choose your conversion.", font=('Calibre', 10, 'bold'), bg="White", fg="#494949", padx=5, pady=5)


        # Initialize variables
        choice1 = tk.StringVar()
        choice1.set("Teaspoon")

        choice2 = tk.StringVar()
        choice2.set("Teaspoon")

        userEntry = tk.StringVar()
        userEntry.set("0")

        returnText = tk.StringVar()
        returnText.set("")

        # Creates a list of types of measures for the dropdown boxes
        convertOptions = ["Teaspoon", "Tablespoon", "Cup", "Pint", "Quart", "Gallon"]

        # Places widgets to accept user input for measurement conversions
        self.convertLbl1 = tk.Label(self, text="From:", bg="White")
        self.dropdown1 = tk.OptionMenu(self, choice1, *convertOptions)
        self.dropdown1.config(width=15)
        self.fromEntry = tk.Entry(self, textvariable=userEntry, width=10)
        self.convertLbl2 = tk.Label(self, text="To:", bg="White")
        self.dropdown2 = tk.OptionMenu(self, choice2, *convertOptions)
        self.dropdown2.config(width=15)
        self.finalConvert = tk.Label(self, textvariable=returnText, width=10, relief=tk.SUNKEN)


        def measure_conversions(start_value, start_unit, end_unit):
            """This function calculates and converts the various measurements"""
            # global convetValue
            wc = {
                "Teaspoon": 1,
                "Tablespoon": 0.333,
                "Cup": 0.0205372,
                "Pint": 0.0104167,
                "Quart": 0.00520833,
                "Gallon": 0.00130208,
            }
            # start_value = float(start_value)
            convetValue = round(start_value * (wc[end_unit] / wc[start_unit]), 4)
            # return convetValue
            return convetValue

        def updateConversionLbl():
            """This Function updates the label with the result of the measure_conversion calculation"""
            
            try:       
                # Prepare tkinter object for type conversion for measure_conversoin function.
                numEntryGet = userEntry.get()
                numEntry = float(numEntryGet)
                choice1Str = choice1.get()
                choice2Str = choice2.get()

            
                finalAnswer = measure_conversions(numEntry, choice1Str, choice2Str)

                someString = str(finalAnswer)
                returnText.set(someString)
            except ValueError:
                # Displays an error box if input is incorrect. 
                messagebox.showerror('Input Error', 'Input must ba a number. Please try again!')

        # Places the button to convert process the conversion from the user's selections.
        self.doConvert = tk.Button(self, text="Convert", command=updateConversionLbl, bg='#d7d7d7', font=BOLD)

        # Places buttons to go to the timer window and to quit the main window
        self.timerBtn = tk.Button(self, text="Timer", command=self.open_timer, width=12)        
        self.quitBtn = tk.Button(self, text="Quit", command=self.destroy, width=12)


        # Position widgets
        self.titleLbl.grid(row=0, column=0, columnspan=10)
        self.measurePixLbl.grid(row=1, columnspan=10, rowspan=8)
        self.convertTitleLbl.grid(row=9, column=0, columnspan=10)

        self.convertLbl1.grid(row=10, column=3)
        self.convertLbl2.grid(row=10, column=6)

        self.dropdown1.grid(row=11, column=3)
        self.dropdown2.grid(row=11, column=6)

        self.fromEntry.grid(row=12, column=3)
        self.finalConvert.grid(row=12, column=6)

        self.doConvert.grid(row=11, column=5, rowspan=3)

        self.timerBtn.grid(row=14, column=3, columnspan=3, padx=20, pady=20)
        self.quitBtn.grid(row=14, column=5, columnspan=3, padx=20, pady=20)

    def open_timer(self):
        """Opens the timer window"""
        window = TimerWindow(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
