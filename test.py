def calculator(self):
        self.main_frame = Frame(self.window,width=270,height=270)
        self.text_Input=StringVar()
        self.operator =""
        self.txtdisplay = Entry(self.main_frame,font=('ariel' ,20,'bold'), textvariable=self.text_Input ,width=17, bd=5 ,insertwidth=4 ,bg="white",justify='right')
        self.txtdisplay.place(relx=0,rely=0)
        self.btn7=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="7",bg="powder blue", command=lambda: self.btnclick(7))
        self.btn7.place(relx=0,rely=0.17)
        self.btn8=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="8",bg="powder blue", command=lambda: self.btnclick(8) )
        self.btn8.place(relx=0.23,rely=0.17)
        self.btn9=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="9",bg="powder blue", command=lambda: self.btnclick(9) )
        self.btn9.place(relx=0.46,rely=0.17)
        self.Addition=Button(self.main_frame,bd=4,width=6, fg="black", font=('ariel', 14 ,'bold'),text="+",bg="powder blue", command=lambda: self.btnclick("+") )
        self.Addition.place(relx=0.69,rely=0.17)
        self.btn4=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="4",bg="powder blue", command=lambda: self.btnclick(4) )
        self.btn4.place(relx=0,rely=0.33)
        self.btn5=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="5",bg="powder blue", command=lambda: self.btnclick(5))
        self.btn5.place(relx=0.23,rely=0.33)
        self.btn6=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="6",bg="powder blue", command=lambda: self.btnclick(6) )
        self.btn6.place(relx=0.46,rely=0.33)
        self.Substraction=Button(self.main_frame,bd=4,width=6, fg="black", font=('ariel', 14 ,'bold'),text="-",bg="powder blue", command=lambda: self.btnclick("-") )
        self.Substraction.place(relx=0.69,rely=0.33)
        self.btn1=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="1",bg="powder blue", command=lambda: self.btnclick(1) )
        self.btn1.place(relx=0,rely=0.49)
        self.btn2=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="2",bg="powder blue", command=lambda: self.btnclick(2) )
        self.btn2.place(relx=0.23,rely=0.49)
        self.btn3=Button(self.main_frame,bd=4,width=4,fg="black", font=('ariel', 14 ,'bold'),text="3",bg="powder blue", command=lambda: self.btnclick(3) )
        self.btn3.place(relx=0.46,rely=0.49)
        self.multiply=Button(self.main_frame,bd=4,width=6, fg="black", font=('ariel', 14 ,'bold'),text="*",bg="powder blue", command=lambda: self.btnclick("*")) 
        self.multiply.place(relx=0.69,rely=0.49)
        self.btn0=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="0",bg="powder blue", command=lambda: self.btnclick(0) )
        self.btn0.place(relx=0,rely=0.65)
        self.btnc=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text="c",bg="powder blue", command=self.clrdisplay)
        self.btnc.place(relx=0.23,rely=0.65)
        self.Decimal=Button(self.main_frame,bd=4,width=4, fg="black", font=('ariel', 14 ,'bold'),text=".",bg="powder blue", command=lambda: self.btnclick(".") )
        self.Decimal.place(relx=0.46,rely=0.65)
        self.Division=Button(self.main_frame,bd=4,width=6, fg="black", font=('ariel', 14 ,'bold'),text="/",bg="powder blue", command=lambda: self.btnclick("/") )
        self.Division.place(relx=0.69,rely=0.65)
        self.btnequal=Button(self.main_frame,bd=4,width = 21, fg="black", font=('ariel', 14 ,'bold'),text="=",bg="powder blue",command=self.eqals)
        self.btnequal.place(relx=0.01,rely=0.82)
        self.main_frame.place(relx=0.52,rely=0.15)
        