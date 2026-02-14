import tkinter as tk

# -- THE FUNCTIONS --
# These guys hold the operations here, they make the program work here.
def theCalculateMachine(action, final_eqtn=tk.StringVar):
    equation_txt = final_eqtn.get()
    if action == "=":
        try:
            final_result = eval(equation_txt)
            # DEBUG: print(final_result)
            final_eqtn.set(final_result)
        except ZeroDivisionError:
            final_eqtn.set("Error cannot divide by zero")

    elif action == "C":
        final_eqtn.set("")
        
    elif action == "\u232B":
        if len(equation_txt) >= 1:
            li_eqtn_txt = [i for i in equation_txt]
            li_eqtn_txt[-1] = ""
            final_eqtn.set("".join(li_eqtn_txt))


def storeTheInputs(num_oprtr_entr, eqtn_entry_TkStr):
    # DEBUG: print(f"Hello The value is {inp}")
    # adding it into the string_var
    current_eqtn = eqtn_entry_TkStr.get()
    upd_eqtn = current_eqtn + str(num_oprtr_entr)
    eqtn_entry_TkStr.set(upd_eqtn)

# -- THE OBJECTS MAKER (CLASSES) --
# These guys make the objects that the main calculator program runs
# (they are mainly buttons and are an excuse to use classes)

class NumberCalcButton():
    def __init__(self, master, text, num_val, eqtn_entry, row, col):
        self.button = tk.Button(
            master, 
            text=text,
            activebackground="#de4a0f",
            activeforeground="#ffe69a",
            bg='#9e3c1b',
            fg='#f09646',
            font=('Michroma', 11),
            command=lambda: storeTheInputs(num_val, eqtn_entry),
            width=5,
            height=2
        )
        self.button.grid(row=row, column=col, padx=5, pady=5)

class OperatorCalcButton():
    def __init__(self, master, text, oprtr_val, eqtn_entry, row, col):
        self.button = tk.Button(
            master, 
            text=text,
            activebackground="#de4a0f",
            activeforeground="#ffe69a",
            bg="#9e3c1b",
            fg='#f09646',
            font=('Michroma', 11),
            command=lambda: storeTheInputs(oprtr_val, eqtn_entry),
            width=5,
            height=2
        )
        self.button.grid(row=row, column=col, padx=5, pady=5)

class ActionCalcButton():
    def __init__(self, master, text, action, eqtn_entry, row, col):
        self.button = tk.Button(
            master, 
            text=text,
            activebackground="#de4a0f",
            activeforeground="#ffe69a",
            bg='#9e3c1b',
            fg='#f09646',
            font=('Michroma', 11),
            command=lambda: theCalculateMachine(action, eqtn_entry),
            width=5,
            height=2
        )
        self.button.grid(row=row, column=col, padx=5, pady=5)

# -- THE MAIN FUNCTION --
# This takes all the setup that has been made and builds a calculator


def main():
    # Create the main window
    main_window = tk.Tk(screenName="Tkinter Calculator")
    main_window.configure(bg="#3a1612")
    main_window.title("Tkinter Calculator")
    main_window.geometry("368x494")

    # -- THE ENTRY BOX STRING --
    # This stores the numbers and the operators together into a nice Tkinter String variable for visual use
    equation_entry_TkStr = tk.StringVar()
    equation_entry_TkStr.set("")

    # -- BUTTONs --
    # Top-row buttons
    top_row_buttons_list = ["(", ")", "\u232B"]

    # numbers button (from 1 to 9)
    calc_num_buttons_list = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]

    # Columns of operators
    operators_column = [("-", "-"), ("+", "+"), ("/", "/"), ("\u00D7", "*")]

    # bottom-row buttons
    bottom_row_buttons_list = ["•", "0", "=", "C"]

    # -- THE UI SIDE --
    # This is where the UI resides

    # Entry box
    # This is just the label box for where the "entry_str" puts the 
    # input together and the final result of the equation
    display_label = tk.Label(main_window, textvariable=equation_entry_TkStr, borderwidth=5, relief="sunken", bg="#ffe69a", fg="#3a1612", font=("Courier", 20, "bold"), anchor="e", width=18)
    display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

    # Button Frame
    button_frame = tk.Frame(main_window, bg="#952a0b", borderwidth=5, relief="raised")
    button_frame.grid(row=1, column=0, padx=10, pady=5)

    # Generate Top-row buttons
    OperatorCalcButton(button_frame, top_row_buttons_list[0], top_row_buttons_list[0], equation_entry_TkStr, 0, top_row_buttons_list.index(top_row_buttons_list[0]))
    OperatorCalcButton(button_frame, top_row_buttons_list[1], top_row_buttons_list[1], equation_entry_TkStr, 0, top_row_buttons_list.index(top_row_buttons_list[1]))
    ActionCalcButton(button_frame, top_row_buttons_list[2], top_row_buttons_list[2], equation_entry_TkStr, 0, top_row_buttons_list.index(top_row_buttons_list[2]))

    # Generate Number Buttons
    for r in calc_num_buttons_list:
        for btn in r:
            NumberCalcButton(button_frame, btn, btn, equation_entry_TkStr, calc_num_buttons_list.index(r)+1, r.index(btn))

    # Generate Operators Buttons
    for c in operators_column:
        OperatorCalcButton(button_frame, c[0], c[1], equation_entry_TkStr, operators_column.index(c), 3)

    # Generate Bottom-Row Buttons
    ## Numbers -> (decimal point, 0)
    NumberCalcButton(button_frame, bottom_row_buttons_list[0], ".", equation_entry_TkStr, 4, bottom_row_buttons_list.index(bottom_row_buttons_list[0]))
    NumberCalcButton(button_frame, bottom_row_buttons_list[1], bottom_row_buttons_list[1], equation_entry_TkStr, 4, bottom_row_buttons_list.index(bottom_row_buttons_list[1]))
    ## Actions -> (equal sign, clear button)
    ActionCalcButton(button_frame, bottom_row_buttons_list[2], bottom_row_buttons_list[2], equation_entry_TkStr, 4, bottom_row_buttons_list.index(bottom_row_buttons_list[2]))
    ActionCalcButton(button_frame, bottom_row_buttons_list[3], bottom_row_buttons_list[3], equation_entry_TkStr, 4, bottom_row_buttons_list.index(bottom_row_buttons_list[3]))

    # Start the main event loop
    main_window.mainloop()


if __name__ == "__main__":
    main()