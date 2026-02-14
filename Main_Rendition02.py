import tkinter as tk
import tkinter.font as tkFont

# -- THE FUNCTIONS --
# These guys hold the operations here, they make the program work here.

def theCalculateMachine(the_equation):
    result = 0
    theEquation_stringified = the_equation.get()
    if "=" in theEquation_stringified:
        result = eval(theEquation_stringified)
    if result != 0:
        return result
    else:
        return theEquation_stringified

def storeTheInputs(inp, store_inp):
    # DEBUG: print(f"Hello The value is {inp}")
    # adding it into the string_var
    current_text = store_inp.get()
    new_text = current_text + str(inp)
    store_inp.set(new_text)

# -- THE OBJECTS MAKER (CLASSES) --
# These guys make the objects that the main calculator program runs
# (they are mainly buttons and are an excuse to use classes)

class CalcNumButton():
    def __init__(self, master, text, value, store_val, row, col):
        self.button = tk.Button(
            master, 
            text=text,
            activebackground="#ca883b",
            activeforeground="#b26b2e",
            bg='#f6c253',
            fg='#6e4122',
            font=('Michroma', 10, 'bold'),
            command=lambda: storeTheInputs(value, store_val),
            width=5,
            height=2
        )
        self.button.grid(row=row, column=col, padx=5, pady=5)

class CalcOperateButton():
    def __init__(self, master, text, value, store_val, row, col):
        self.button = tk.Button(
            master, 
            text=text,
            activebackground="#ca883b",
            activeforeground="#b26b2e",
            bg='#f6c253',
            fg='#6e4122',
            font=('Courier', 18, 'bold'),
            command=lambda: theCalculateMachine(value, store_val),
            width=5,
            height=2
        )
        self.button.grid(row=row, column=col, padx=5, pady=5)

class CalcOptionButton():
    def __init__(self, master, text, value, store_val, row, col):
        self.button = tk.Button(
            master, 
            text=text,
            activebackground="#ca883b",
            activeforeground="#b26b2e",
            bg='#f6c253',
            fg='#6e4122',
            font=('Courier', 18, 'bold'),
            command=lambda: storeTheInputs(value, store_val),
            width=5,
            height=2
        )
        self.button.grid(row=row, column=col, padx=5, pady=5)

# -- THE MAIN FUNCTION --
# This takes all the setup that has been made and builds a calculator


def main():
    # Create the main window
    main_window = tk.Tk(screenName="Tkinter Calculator")
    main_window.configure(bg="#e1983c")
    main_window.title("Tkinter Calculator")
    main_window.geometry("380x490")

    # -- THE ENTRY BOX STRING --
    # This stores the numbers and the operators together into a nice Tkinter String variable for visual use
    entry_tk_str = tk.StringVar()
    entry_tk_str.set("")

    # -- BUTTONs --
    # Top-row buttons
    top_row_buttons_list = ["(", ")", "<-"]

    # numbers button (from 1 to 9)
    calc_num_buttons_list = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]

    # Columns of operators
    operators_column = ["-", "+", "÷", "×", "C"]

    # bottom-row buttons
    bottom_row_buttons_list = ["•", "0", "="]

    # -- THE UI SIDE --
    # This is where the UI resides
    
    # Entry box
    # This is just the label box for where the "entry_str" puts the 
    # input together and the final result of the equation
    display_label = tk.Label(main_window, textvariable=entry_tk_str, bg="#f6c253", fg="#6e4122", font=("Courier", 20, "bold"), anchor="e")
    display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

    # Button Frame
    button_frame = tk.Frame(main_window, bg="#e1983c")
    button_frame.grid(row=1, column=0, padx=10, pady=5)

    # Generate Top-row buttons
    for tr in top_row_buttons_list:
        CalcOptionButton(button_frame, tr, tr, entry_tk_str, 0, top_row_buttons_list.index(tr))

    # Generate Operator Column Buttons
    for c in operators_column:
        CalcOptionButton(button_frame, c, c, entry_tk_str, operators_column.index(c), 4)

    # Generate Number Buttons
    for r in calc_num_buttons_list:
        for btn in r:
            CalcNumButton(button_frame, btn, btn, entry_tk_str, calc_num_buttons_list.index(r)+1, r.index(btn))
    
    # Generate bottom row buttons
    CalcOptionButton(button_frame, bottom_row_buttons_list[0], bottom_row_buttons_list[0], entry_tk_str, 4, 0)
    CalcNumButton(button_frame, bottom_row_buttons_list[1], bottom_row_buttons_list[1], entry_tk_str, 4, 1)
    CalcOperateButton(button_frame, bottom_row_buttons_list[2], bottom_row_buttons_list[2], entry_tk_str, 4, 2)
    # Start the main event loop
    main_window.mainloop()


if __name__ == "__main__":
    main()

"""
Things to do:
Get the calculator working!!!
Text box limit is 22 characters, find a way for the text to scroll through previous text once the character length is more than 22
"""