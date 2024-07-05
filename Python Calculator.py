from tkinter import *  # type: ignore

root = Tk()
root.title("Simple Calculator")

myEntry = Entry(root, width=58, borderwidth=5)
myEntry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def ButtonClick(argument):
    current = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(current) + str(argument))

'''
The Calculate part has been done with the help of Operations

Operations has been indexed as follows:
1 means Addition
0 means Subtraction
2 means Multiplication
-1 means Division
'''

def ButtonAdd():
    first_number = myEntry.get()
    global f_num
    global operation
    operation = 1
    f_num = int(first_number)
    myEntry.delete(0, END)

def ButtonSubtract():
    first_number = myEntry.get()
    global f_num
    global operation
    operation = 0
    f_num = int(first_number)
    myEntry.delete(0, END)

def ButtonMultiply():
    first_number = myEntry.get()
    global f_num
    global operation
    operation = 2
    f_num = int(first_number)
    myEntry.delete(0, END)

def ButtonDivide():
    first_number = myEntry.get()
    global f_num
    global operation
    operation = -1
    f_num = int(first_number)
    myEntry.delete(0, END)

def Calculate():
    second_number = int(myEntry.get())
    if operation == 1:
        result = f_num + second_number
    elif operation == 0:
        result = f_num - second_number
    elif operation == 2:
        result = f_num * second_number
    elif operation == -1:
        result = f_num / second_number

    myEntry.delete(0, END)
    myEntry.insert(0, str(result))

def Clear():
    myEntry.delete(0, END)

# Creating the buttons
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: ButtonClick(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: ButtonClick(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: ButtonClick(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: ButtonClick(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: ButtonClick(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: ButtonClick(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: ButtonClick(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: ButtonClick(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: ButtonClick(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: ButtonClick(0))
button_plus = Button(root, text='+', padx=40, pady=20, command=ButtonAdd)
button_minus = Button(root, text='-', padx=40.5, pady=20, command=ButtonSubtract)
button_multiply = Button(root, text='*', padx=40, pady=20, command=ButtonMultiply)
button_divide = Button(root, text='/', padx=40, pady=20, command=ButtonDivide)
button_enter = Button(root, text='=', padx=40, pady=20, bg="#1975c5", fg="#000000", command=Calculate)
button_clear = Button(root, text='Clear', padx=30, pady=20, command=Clear)

# Griding the created buttons

# First Row
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_clear.grid(row=1, column=3)

# Second Row
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_plus.grid(row=2, column=3)

# Third Row
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

# Fourth Row
button0.grid(row=4, column=0)
button_enter.grid(row=4, column=3)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)

root.mainloop()
