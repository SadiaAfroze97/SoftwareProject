###project start####
from tkinter import *
import math,random,os

class BillingSft:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("ABC COMPANY")

        bg_color = '#856ff8'
        colorbtn = "#6e8ab2"

        title = Label(self.root, text="ABC COMPANY", bd=15, relief=GROOVE, bg=bg_color, fg="indigo",font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        ###########Variables####################

        ######Cosmetic_variable#######

        self.soap = IntVar()

        self.face_cream = IntVar()

        self.face_wash = IntVar()

        self.spray = IntVar()

        self.gel = IntVar()

        self.lotion = IntVar()



        #end######



        ####Cloths_Variable########

        self.rice = IntVar()

        self.food_oil = IntVar()

        self.tea = IntVar()

        self.daal = IntVar()

        self.wheat = IntVar()

        self.suger = IntVar()



        ###End

        #######Jwellery_Variable######

        self.maza = IntVar()

        self.cock = IntVar()

        self.sprite = IntVar()

        self.thumbsup = IntVar()

        self.limca = IntVar()

        self.frooti= IntVar()

        ##End

        ######Total Price&Tax Variable###

        self.cosmetic_price = StringVar()
        self.cold_price = StringVar()
        self.grocery_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.cold_tax = StringVar()
        self.grocery_tax = StringVar()

        ###END

        ####Customer Variable######

        self.c_name = StringVar()
        self.c_phn = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        ###ENd

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

        #####Cloth_Frame######
        F3=LabelFrame(self.root,text="Cloths",bd=10,relief=GROOVE, font= ("times new roman", 15, "bold"), fg="#a0615f", bg=bg_color)
        F3.place(x=340, y=175, width=325,height=380)

        rice_lbl= Label(F3, text="Gulhar",font=("times new roman", 16, "bold"),bg=bg_color, fg="lavender").grid(row=0, column=0,padx=10, pady=10, sticky="w")
        rice_txt=Entry(F3, width=10, textvariable=self.rice,font=("times new roman", 16, "bold"), bd=5, relief= SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Food_lbl = Label(F3, text="Vivek", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Food_txt = Entry(F3, width=10, textvariable=self.food_oil,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Daal_lbl = Label(F3, text="Twakkal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Daal_txt = Entry(F3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        wheat_lbl = Label(F3, text="Ksrishma", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        suger_lbl = Label(F3, text="Malhar", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        suger_txt = Entry(F3, width=10, textvariable=self.suger,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        tea_lbl = Label(F3, text="Digital", font=("times new roman", 16, "bold"), bg=bg_color,fg="lavender").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tea_txt = Entry(F3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #####End

        ######Cosmetics_Frame#######
        F2=LabelFrame(self.root,text="Cosmatics",bd=10,relief=GROOVE, font= ("times new roman", 15, "bold"), fg="#a0615f", bg=bg_color)
        F2.place(x=5, y=175, width=325,height=380)

        bath_lbl= Label(F2, text="Bath Soap",font=("times new roman", 16, "bold"),bg=bg_color, fg="lavender").grid(row=0, column=0,padx=10, pady=10, sticky="w")
        bath_txt=Entry(F2, width=10,textvariable=self.soap, font=("times new roman", 16, "bold"), bd=5, relief= SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid( row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10,textvariable=self.spray, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.gel,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10,textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        ######End

        #####Jwellery_Frame$$$$$$
        F4=LabelFrame(self.root,text="Jwellery",bd=10,relief=GROOVE, font= ("times new roman", 15, "bold"), fg="#a0615f", bg=bg_color)
        F4.place(x=670, y=175, width=325,height=380)

        maza_lbl= Label(F4, text="Ear ring",font=("times new roman", 16, "bold"),bg=bg_color, fg="lavender").grid(row=0, column=0,padx=10, pady=10, sticky="w")
        maza_txt=Entry(F4, width=10,textvariable=self.maza, font=("times new roman", 16, "bold"), bd=5, relief= SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        cock_lbl = Label(F4, text="Necklace", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        cock_txt = Entry(F4, width=10,textvariable=self.cock, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        frooti_lbl = Label(F4, text="Pendant", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        frooti_txt = Entry(F4, width=10,textvariable=self.frooti, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        th_lbl = Label(F4, text="Bangles", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid( row=3, column=0, padx=10, pady=10, sticky="w")
        th_txt = Entry(F4, width=10,textvariable=self.thumbsup, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        limca_lbl = Label(F4, text="Bracelet", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        limca_txt = Entry(F4, width=10,textvariable=self.limca, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        sprite_lbl = Label(F4, text="Chain", font=("times new roman", 16, "bold"), bg=bg_color, fg="lavender").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sprite_txt = Entry(F4, width=10,textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)
        ######End

        ####Bill_Section#####


        ###END

        ####Button_Section###
        ####End



 #####Functions
    def total(self):
        pass
    def new_bill(self):
        pass
    def make_bill(self):
        pass

root=Tk()
obj = BillingSft(root)
root.mainloop()





























