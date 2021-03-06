###project start####

from tkinter import *

class BillingSft:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("ABC COMPANY")

        bg_color = '#856ff8'
        colorbtn = "#6e8ab2"

        title = Label(self.root, text="ABC COMPANY", bd=15, relief=GROOVE, bg=bg_color, fg="indigo",font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        #####customer detail####
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),fg="#a0615f", bg=bg_color)
        F1.place(x=0, y=85, relwidth=1)

        cnane_lbbl = Label(F1, text="Customer Name", bg=bg_color, fg="lavender",font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=16, textvar=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1,pady=5, padx=10)

        cphone_lbbl = Label(F1, text="Customer Phone No", bg=bg_color, fg="lavender",font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, width=16, textvar=self.c_phn, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbbl = Label(F1, text="Bill Number ", bg=bg_color, fg="lavender",font=("times new roman", 15, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=16, textvar=self.bill_no, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=8, bg=colorbtn, fg="indigo", font="arial 12 bold").grid(row=0,column=6,padx=10, pady=10)


root=Tk()
obj = BillingSft(root)
root.mainloop()
