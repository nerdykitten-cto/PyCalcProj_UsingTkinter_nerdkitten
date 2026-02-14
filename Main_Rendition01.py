import tkinter as tk

def main():
    # Create the main window
    main_window = tk.Tk()
    main_window.title("4x5 Button Grid")

    # entry_str
    entry_str = tk.StringVar(value="Hello World")

    # input view
    input_field = tk.Text(main_window, width=12, height=3)
    input_field.grid(row=0, column=0, columnspan=4)

    input_field.insert(tk.END, entry_str)
    # Create buttons one by one
    btn1 = tk.Button(main_window, text="1", width=12, height=4)
    btn1.grid(row=1, column=0)

    btn2 = tk.Button(main_window, text="2", width=12, height=4)
    btn2.grid(row=1, column=1)

    btn3 = tk.Button(main_window, text="3", width=12, height=4)
    btn3.grid(row=1, column=2)

    btn4 = tk.Button(main_window, text="4", width=12, height=4)
    btn4.grid(row=1, column=3)

    btn6 = tk.Button(main_window, text="5", width=12, height=4)
    btn6.grid(row=2, column=0)

    btn7 = tk.Button(main_window, text="6", width=12, height=4)
    btn7.grid(row=2, column=1)

    btn8 = tk.Button(main_window, text="7", width=12, height=4)
    btn8.grid(row=2, column=2)

    btn9 = tk.Button(main_window, text="8", width=12, height=4)
    btn9.grid(row=2, column=3)

    btn11 = tk.Button(main_window, text="9", width=12, height=4)
    btn11.grid(row=3, column=0)

    btn12 = tk.Button(main_window, text="10", width=12, height=4)
    btn12.grid(row=3, column=1)

    btn13 = tk.Button(main_window, text="11", width=12, height=4)
    btn13.grid(row=3, column=2)

    btn14 = tk.Button(main_window, text="12", width=12, height=4)
    btn14.grid(row=3, column=3)

    btn16 = tk.Button(main_window, text="13", width=12, height=4)
    btn16.grid(row=4, column=0)

    btn17 = tk.Button(main_window, text="14", width=12, height=4)
    btn17.grid(row=4, column=1)

    btn18 = tk.Button(main_window, text="15", width=12, height=4)
    btn18.grid(row=4, column=2)

    btn19 = tk.Button(main_window, text="16", width=12, height=4)
    btn19.grid(row=4, column=3)

    # Start the main event loop
    main_window.mainloop()

if __name__ == "__main__":
    main()