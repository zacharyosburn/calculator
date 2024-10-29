import tkinter as tk

calculation = ""

def calculation_field(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calculation)

def eval_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
    except:
        clear()
        result.insert(1.0, "ERR")

def clear():
    global calculation
    calculation = ""
    result.delete(1.0, "end")


root = tk.Tk()
root.geometry("500x625")
result = tk.Text(root, height=2, width=20, font=("Cascadia Code", 32))
result.grid (columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: calculation_field(1), width=7, height=3, font=("Cascadia Code", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: calculation_field(2), width=7, height=3, font=("Cascadia Code", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: calculation_field(3), width=7, height=3, font=("Cascadia Code", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: calculation_field(4), width=7, height=3, font=("Cascadia Code", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: calculation_field(5), width=7, height=3, font=("Cascadia Code", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: calculation_field(6), width=7, height=3, font=("Cascadia Code", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: calculation_field(7), width=7, height=3, font=("Cascadia Code", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: calculation_field(8), width=7, height=3, font=("Cascadia Code", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: calculation_field(9), width=7, height=3, font=("Cascadia Code", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: calculation_field(0), width=7, height=3, font=("Cascadia Code", 14))
btn_0.grid(row=5, column=1)

btn_l_paran = tk.Button(root, text="(", command=lambda: calculation_field("("), width=7, height=3, font=("Cascadia Code", 14))
btn_l_paran.grid(row=5, column=2)

btn_r_paran = tk.Button(root, text=")", command=lambda: calculation_field(")"), width=7, height=3, font=("Cascadia Code", 14))
btn_r_paran.grid(row=5, column=3)

btn_mult = tk.Button(root, text="*", command=lambda: calculation_field("*"), width=7, height=3, font=("Cascadia Code", 14))
btn_mult.grid(row=2, column=4)

btn_div = tk.Button(root, text="/", command=lambda: calculation_field("/"), width=7, height=3, font=("Cascadia Code", 14))
btn_div.grid(row=3, column=4)

btn_plus = tk.Button(root, text="+", command=lambda: calculation_field("+"), width=7, height=3, font=("Cascadia Code", 14))
btn_plus .grid(row=4, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: calculation_field("-"), width=7, height=3, font=("Cascadia Code", 14))
btn_minus.grid(row=5, column=4)

btn_clear = tk.Button(root, text="C", command=clear, width=28, height=3, font=("Cascadia Code", 14))
btn_clear.grid(row=6, column=1, columnspan=3)

btn_equal = tk.Button(root, text="=", command=eval_calculation, width=7, height=3, font=("Cascadia Code", 14))
btn_equal.grid(row=6, column=4)

root.mainloop()