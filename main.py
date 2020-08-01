import arithmetic as ar
import calc as ca
from tkinter import * 

#############################################################################################
# Functions #
#############

def buttonPress(btn):
    # Concatenates the button pressed to the calculator's entry field.
    entry.insert(string=str(btn), index=END)


def generate_key(text, x, y):
    # Loader function for creating the numpad and operation keys.
    #  Inputs: Button_Value, X-Coordinate, Y-Coordinate [for Grid layout]
    button = Button(root, text=text, command=lambda:buttonPress(text))
    button.grid(column=x, row=y, padx=5, pady=5)


def CalculateWrap():
    # Wrapper function to evaluate entry expression when the "=" button is pressed
    result = str(ca.Calculate(entry.get()))
    history.append(entry.get())
    entry.delete("0", END)
    entry.insert(string = result, index = END)

    

def goBack():
    # History function that revert's the entry to the previous pre-evaluated expression
    if len(history) > 0:
        prev = history.pop()
        future.append(entry.get())
        entry.delete("0", END)
        entry.insert(string = prev, index = END)
    else:
        print("No History found.")

def clear():
    # Destroys antartica
    entry.delete(0, END)


##################################################################################
root = Tk()
root.title("SimpCal")

history = []
future = []

entry = Entry(root, width=15, justify = RIGHT)
entry.grid(column = 0, row = 1, columnspan=4, pady = 5)
entry.focus()


generate_key("7", 0, 2)
generate_key("8", 1, 2)
generate_key("9", 2, 2)
generate_key("4", 0, 3)
generate_key("5", 1, 3)
generate_key("6", 2, 3)
generate_key("1", 0, 4)
generate_key("2", 1, 4)
generate_key("3", 2, 4)
generate_key("0", 1, 5)
generate_key("+", 3, 5)
generate_key("-", 2, 5)
generate_key("*", 3, 3)
generate_key("/", 3, 4)
generate_key(".", 0, 5)
generate_key("^", 2, 6)
generate_key("%", 1, 6)

Button(root, text="=", command=CalculateWrap, fg="dark green", relief=GROOVE).grid(column=3, row=6, padx = 5)
Button(root, text="H", command=goBack, fg = "blue").grid(column=3, row=2)
Button(root, text="C", command=clear, fg='red').grid(column=0, row=6)


root.resizable(False, False)
root.mainloop()


