from tkinter import *

window = Tk()

def close_window():
     window.quit()

def main():


    window.geometry("800x600")
    window.title("Calculator")


    
    
    Button(window, text= "Close the Window", font=("Calibri",14,"bold"), command=close_window).pack(pady=20)
    Button(window, text= "Main operation", font=("Calibri",14,"bold"), command=main_function).pack(pady=20)

    window.mainloop()