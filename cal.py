import tkinter as tk
cal = ""
def add_to_cal(sym):
    global cal
    cal += str(sym)
    txt_res.delete(1.0, "end")
    txt_res.insert(1.0, cal)
def evolute_cal():
    global cal
    try:
        expression = cal.replace("x", "*").replace("÷", "/")
        res = str(eval(expression))
        cal = res  
        txt_res.delete(1.0, "end")
        txt_res.insert(1.0, res)
    except:
        clr_fid()
        txt_res.insert(1.0, "error")
    global cal
    cal = cal[:-1]  
    txt_res.delete(1.0, "end")
    txt_res.insert(1.0, cal)
def clr_fid():  
    global cal
    cal = ""
    txt_res.delete(1.0, "end")
root = tk.Tk()
root.title("Calculator")
root.geometry("254x275")  
txt_res = tk.Text(root, height=2, width=15, font=("Arial", 24))
txt_res.grid(columnspan=5)
btn7 = tk.Button(root, text="7", command=lambda: add_to_cal(7), width=5, font=("Times New Roman", 14))
btn7.grid(row=3, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to_cal(8), width=5, font=("Times New Roman", 14))
btn8.grid(row=3, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to_cal(9), width=5, font=("Times New Roman", 14))
btn9.grid(row=3, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to_cal(4), width=5, font=("Times New Roman", 14))
btn4.grid(row=2, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to_cal(5), width=5, font=("Times New Roman", 14))
btn5.grid(row=2, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to_cal(6), width=5, font=("Times New Roman", 14))
btn6.grid(row=2, column=3)
btn1 = tk.Button(root, text="1", command=lambda: add_to_cal(1), width=5, font=("Times New Roman", 14))
btn1.grid(row=1, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to_cal(2), width=5, font=("Times New Roman", 14))
btn2.grid(row=1, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to_cal(3), width=5, font=("Times New Roman", 14))
btn3.grid(row=1, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to_cal(0), width=5, font=("Times New Roman", 14))
btn0.grid(row=4, column=2)
btnplus = tk.Button(root, text="+", command=lambda: add_to_cal("+"), width=5, font=("Times New Roman", 14))
btnplus.grid(row=1, column=4)
btnminus = tk.Button(root, text="-", command=lambda: add_to_cal("-"), width=5, font=("Times New Roman", 14))
btnminus.grid(row=2, column=4)
btnmp = tk.Button(root, text="x", command=lambda: add_to_cal("x"), width=5, font=("Arial", 14))
btnmp.grid(row=3, column=4)
btnds = tk.Button(root, text="÷", command=lambda: add_to_cal("÷"), width=5, font=("Times New Roman", 14))
btnds.grid(row=4, column=4)
btnpoi = tk.Button(root, text=".", command=lambda: add_to_cal("."), width=5, font=("Times New Roman", 14))
btnpoi.grid(row=4, column=1)
btnp1 = tk.Button(root, text="(", command=lambda: add_to_cal("("), width=5, font=("Times New Roman", 14))
btnp1.grid(row=5, column=1)
btnp2 = tk.Button(root, text=")", command=lambda: add_to_cal(")"), width=5, font=("Times New Roman", 14))
btnp2.grid(row=5, column=2)
btnclr = tk.Button(root, text="C", command=clr_fid, width=5, font=("Times New Roman", 14))
btnclr.grid(row=5, column=3)
btns = tk.Button(root, text="<=", command=clr, width=5, font=("Times New Roman", 14))
btns.grid(row=5, column=4)
btneq = tk.Button(root, text="=", command=evolute_cal, width=5, font=("Times New Roman", 14))
btneq.grid(row=4, column=3)
root.mainloop()
