import re
from tkinter import *

#creating window object
window = Tk()

expression = ""

#basic function, uses a switch statment based on the passed in operator
#to do the basic calculation, returns this value back
def basic_cal(numb1, numb2, operator):
     x = numb1
     y = numb2
     if operator == "+":
         return x+y
     elif operator == "-":
         return x-y
     elif operator == "*":
         return x*y
     elif operator == "/":
         return x/y
     elif operator == "^":
         return pow(x,y)
     else:
         return "Error"

#button press function
def press(num, _event=None):
    global expression
 
    expression = expression + str(num)
 
    equation.set(expression)

#calculate total
def calculate():

    try:
        global expression

        expression = re.split(r"(\+|\*|-|/|\^)", expression)

        total = str(basic_cal(float(expression[0]), float(expression[2]), expression[1]))
 
        equation.set(total)
 
        expression = ""
 
    except:
        equation.set(" error ")
        expression = ""
    
#clear display
def clear():
    global expression
    expression = ""
    equation.set("")

#driver code
if __name__ == "__main__":
    window.configure(background="gray")
    window.title("Calculator")
    window.geometry("240x480")


    equation = StringVar()
    expression_field = Entry(window, textvariable=equation, font='100', state=DISABLED)
    expression_field.grid(columnspan=4, ipadx=70, ipady=70)

    #reactive window
    window.grid_rowconfigure(0, weight=2)
    window.grid_rowconfigure(1, weight=3)
    window.grid_rowconfigure(2, weight=3)
    window.grid_rowconfigure(3, weight=3)
    window.grid_rowconfigure(4, weight=3)
    window.grid_rowconfigure(5, weight=3)
    window.grid_rowconfigure(6, weight=3)
    window.grid_columnconfigure(0, weight=3)
    window.grid_columnconfigure(1, weight=3)
    window.grid_columnconfigure(2, weight=3)
    window.grid_columnconfigure(3, weight=3)

    #keyboard key binds
    window.bind('1', lambda event:press(1))
    window.bind('2', lambda event:press(2))
    window.bind('3', lambda event:press(3))
    window.bind('4', lambda event:press(4))
    window.bind('5', lambda event:press(5))
    window.bind('6', lambda event:press(6))
    window.bind('7', lambda event:press(7))
    window.bind('8', lambda event:press(8))
    window.bind('9', lambda event:press(9))
    window.bind('0', lambda event:press(0))
    window.bind('*', lambda event:press("*"))
    window.bind('/', lambda event:press("/"))
    window.bind('-', lambda event:press("-"))
    window.bind('+', lambda event:press("+"))
    window.bind('^', lambda event:press("^"))
    window.bind('.', lambda event:press("."))

    button1 = Button(window, text=' 1 ', fg='black', bg='dark gray',font='10', command=lambda: press(1), height=5, width=10)
    button1.grid(row=2, column=0) 
 
    button2 = Button(window, text=' 2 ', fg='black', bg='dark gray',font='10',command=lambda: press(2), height=5, width=10)
    button2.grid(row=2, column=1)

    button3 = Button(window, text=' 3 ', fg='black', bg='dark gray',font='10',command=lambda: press(3), height=5, width=10)
    button3.grid(row=2, column=2)
 
    button4 = Button(window, text=' 4 ', fg='black', bg='dark gray',font='10', command=lambda: press(4), height=5, width=10)
    button4.grid(row=3, column=0)
 
    button5 = Button(window, text=' 5 ', fg='black', bg='dark gray',font='10', command=lambda: press(5), height=5, width=10)
    button5.grid(row=3, column=1)
 
    button6 = Button(window, text=' 6 ', fg='black', bg='dark gray',font='10',command=lambda: press(6), height=5, width=10)
    button6.grid(row=3, column=2)
 
    button7 = Button(window, text=' 7 ', fg='black', bg='dark gray',font='10', command=lambda: press(7), height=5, width=10)
    button7.grid(row=4, column=0)
 
    button8 = Button(window, text=' 8 ', fg='black', bg='dark gray',font='10', command=lambda: press(8), height=5, width=10)
    button8.grid(row=4, column=1)
 
    button9 = Button(window, text=' 9 ', fg='black', bg='dark gray',font='10',command=lambda: press(9), height=5, width=10)
    button9.grid(row=4, column=2)
 
    button0 = Button(window, text=' 0 ', fg='black', bg='dark gray',font='10',command=lambda: press(0), height=5, width=10)
    button0.grid(row=5, column=0)
 
    plus = Button(window, text=' + ', fg='black', bg='dark gray',font='10',command=lambda: press("+"), height=5, width=10)
    plus.grid(row=2, column=3)
 
    minus = Button(window, text=' - ', fg='black', bg='dark gray',font='10',command=lambda: press("-"), height=5, width=10)
    minus.grid(row=3, column=3)
 
    multiply = Button(window, text=' * ', fg='black', bg='dark gray',font='10',command=lambda: press("*"), height=5, width=10)
    multiply.grid(row=4, column=3)
 
    divide = Button(window, text=' / ', fg='black', bg='dark gray',font='10',command=lambda: press("/"), height=5, width=10)
    divide.grid(row=5, column=3)
 
    equal = Button(window, text=' = ', fg='black', bg='dark gray',font='10',command=calculate, height=5, width=10)
    equal.grid(row=5, column=2)

    power = Button(window, text=' ^ ', fg='black', bg='dark gray',font='10',command=lambda: press("^"), height=5, width=10)
    power.grid(row=6, column=1)
 
    clearb = Button(window, text='Clear', fg='black', bg='dark gray',font='10', command=clear, height=5, width=10)
    clearb.grid(row=5, column='1')
 
    Decimal= Button(window, text='.', fg='black', bg='dark gray',font='10', command=lambda: press('.'), height=5, width=10)
    Decimal.grid(row=6, column=0)

    window.mainloop()
