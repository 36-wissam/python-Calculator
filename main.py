import tkinter as tk



def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)



root = tk.Tk()
root.configure(bg="#3B2E5E")
root.title("Calculator")
ICON=tk.PhotoImage(file="images/logo_icon.png")
root.iconphoto(False,ICON)




entry = tk.Entry(root, width=20, font=("Arial", 20), bd=5, relief=tk.GROOVE, bg="#FF4A64", fg="#FFBC15")
entry.grid(row=0, column=0, columnspan=4, padx=30, pady=30)



buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]


row_val = 1
col_val = 0


for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), command=lambda b=button: on_click(b),bg="#FF4A64",fg="#FFBC15").grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()