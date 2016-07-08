#Solve function
from math import sqrt
def solver (a, b, c):
    """ Solves the quadratic equation """
    D=b*b - 4*a*c
    if D>=0:
        x1= (-b+sqrt(D))/(2*a)
        x2= (-b-sqrt(D))/(2*a)
        text = "The discriminant is: %s  \n  X1 is: %s  \n  X2 is:  %s \n"  %(D, x1, x2)
    else:
        text = "This equation has no solution"
    return (text)
    
#connect GUI with Solve function
#insert information function
def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0", "end")
    output.insert("0.0", value)

def handler():
    """ Get the content of entries and passes result to the output area """
    try:
        #make sure that we've entered correct values
        a_val = float (a.get())
        b_val = float (b.get())
        c_val = float (c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Make sure you've entered 3 numbers")

def  clear (event):
    """ Clear entry form"""
    caller = event.widget 
    caller.delete("0", "end")
    
#GUI begin
from tkinter import*

#parent item
root = Tk()

#set window name
root.title("Quadratic Calculator")

#set the minimum window size
root.minsize(320, 200)

#we turn off the ability to change the window
root.resizable(width=False, height = False)

#we create work area
frame= Frame(root)
frame.grid()

#field to enter the first argument of the equation (a)
a= Entry(frame, width=3)
a.bind("<FocusIn>", clear)
a.grid(row=1, column=1, padx=(10,0))

#text after the first argument
a_lab= Label(frame, text="x**2 + ").grid(row=1, column=2)

#field to enter the second argument of the equation (b)
b=Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1, column = 3)

#text after the second argument of the equation
b_lab=Label(frame, text="x + ").grid(row=1, column=4)

#field to enter the third argument of the equation (c)
c=Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)

#text after the third argument of the equation
c_lab=Label(frame, text="= 0").grid(row=1, column=6)

#solve button
but=Button(frame, text="Solve", command = handler ).grid(row=1, column=7, padx=(10,0))

#location for the output solutions of the equation

output=Text(frame, bg="lightgrey" , font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

#run main window
       
root.mainloop()        
#GUI end

















