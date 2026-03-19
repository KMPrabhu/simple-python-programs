import tkinter as tk

# -------- login --------
user = "admin"
pw = "123"

# -------- file --------
file = "bill.txt"

total = 0

# -------- functions --------
def login():
    if e1.get() == user and e2.get() == pw:
        f1.pack_forget()
        f2.pack()
    else:
        lmsg.config(text="wrong")

def add_item():
    global total
    name = ename.get()
    price = eprice.get()

    if name != "" and price != "":
        p = int(price)
        total = total + p

        out.insert(tk.END, name + " - " + str(p) + "\n")
        ltotal.config(text="Total: " + str(total))

def save_bill():
    f = open(file, "a")
    f.write("New Bill\n")
    f.write(out.get("1.0", tk.END))
    f.write("Total = " + str(total) + "\n\n")
    f.close()
    lmsg2.config(text="saved")

def clear_all():
    global total
    total = 0
    out.delete("1.0", tk.END)
    ltotal.config(text="Total: 0")

# -------- window --------
win = tk.Tk()
win.title("shop")
win.geometry("300x400")

# -------- login frame --------
f1 = tk.Frame(win)
f1.pack()

tk.Label(f1, text="user").pack()
e1 = tk.Entry(f1)
e1.pack()

tk.Label(f1, text="pass").pack()
e2 = tk.Entry(f1, show="*")
e2.pack()

tk.Button(f1, text="login", command=login).pack()

lmsg = tk.Label(f1, text="")
lmsg.pack()

# -------- main frame --------
f2 = tk.Frame(win)

tk.Label(f2, text="item").pack()
ename = tk.Entry(f2)
ename.pack()

tk.Label(f2, text="price").pack()
eprice = tk.Entry(f2)
eprice.pack()

tk.Button(f2, text="add", command=add_item).pack()
tk.Button(f2, text="save bill", command=save_bill).pack()
tk.Button(f2, text="clear", command=clear_all).pack()

ltotal = tk.Label(f2, text="Total: 0")
ltotal.pack()

out = tk.Text(f2, height=10)
out.pack()

lmsg2 = tk.Label(f2, text="")
lmsg2.pack()

# -------- run --------
win.mainloop()
