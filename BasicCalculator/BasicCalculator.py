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
def press(num):
    global expression
 
    expression = expression + str(num)
 
    equation.set(expression)

#calculate total
def calculate():

    try:
        global expression

        expression = re.split(r"(\+|\*|-|/|\^)", expression)
        print(float(expression[0]))

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
    window.geometry("680x680")

    equation = StringVar()
    expression_field = Entry(window, textvariable=equation, font='100')
    expression_field.grid(columnspan=4, ipadx=70, ipady=70)

    button1 = Button(window, text=' 1 ', fg='black', bg='dark gray',font='10', command=lambda: press(1), height=5, width=20)
    button1.grid(row=2, column=0)
 
    button2 = Button(window, text=' 2 ', fg='black', bg='dark gray',font='10',command=lambda: press(2), height=5, width=20)
    button2.grid(row=2, column=1)
 
    button3 = Button(window, text=' 3 ', fg='black', bg='dark gray',font='10',command=lambda: press(3), height=5, width=20)
    button3.grid(row=2, column=2)
 
    button4 = Button(window, text=' 4 ', fg='black', bg='dark gray',font='10', command=lambda: press(4), height=5, width=20)
    button4.grid(row=3, column=0)
 
    button5 = Button(window, text=' 5 ', fg='black', bg='dark gray',font='10', command=lambda: press(5), height=5, width=20)
    button5.grid(row=3, column=1)
 
    button6 = Button(window, text=' 6 ', fg='black', bg='dark gray',font='10',command=lambda: press(6), height=5, width=20)
    button6.grid(row=3, column=2)
 
    button7 = Button(window, text=' 7 ', fg='black', bg='dark gray',font='10', command=lambda: press(7), height=5, width=20)
    button7.grid(row=4, column=0)
 
    button8 = Button(window, text=' 8 ', fg='black', bg='dark gray',font='10', command=lambda: press(8), height=5, width=20)
    button8.grid(row=4, column=1)
 
    button9 = Button(window, text=' 9 ', fg='black', bg='dark gray',font='10',command=lambda: press(9), height=5, width=20)
    button9.grid(row=4, column=2)
 
    button0 = Button(window, text=' 0 ', fg='black', bg='dark gray',font='10',command=lambda: press(0), height=5, width=20)
    button0.grid(row=5, column=0)
 
    plus = Button(window, text=' + ', fg='black', bg='dark gray',font='10',command=lambda: press("+"), height=5, width=20)
    plus.grid(row=2, column=3)
 
    minus = Button(window, text=' - ', fg='black', bg='dark gray',font='10',command=lambda: press("-"), height=5, width=20)
    minus.grid(row=3, column=3)
 
    multiply = Button(window, text=' * ', fg='black', bg='dark gray',font='10',command=lambda: press("*"), height=5, width=20)
    multiply.grid(row=4, column=3)
 
    divide = Button(window, text=' / ', fg='black', bg='dark gray',font='10',command=lambda: press("/"), height=5, width=20)
    divide.grid(row=5, column=3)
 
    equal = Button(window, text=' = ', fg='black', bg='dark gray',font='10',command=calculate, height=5, width=20)
    equal.grid(row=5, column=2)

    power = Button(window, text=' ^ ', fg='black', bg='dark gray',font='10',command=lambda: press("^"), height=5, width=20)
    power.grid(row=6, column=1)
 
    clearb = Button(window, text='Clear', fg='black', bg='dark gray',font='10', command=clear, height=5, width=20)
    clearb.grid(row=5, column='1')
 
    Decimal= Button(window, text='.', fg='black', bg='dark gray',font='10', command=lambda: press('.'), height=5, width=20)
    Decimal.grid(row=6, column=0)

    window.mainloop()
