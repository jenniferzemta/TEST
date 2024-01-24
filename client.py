from tkinter import *
from tkcalendar import * 
import pymysql
from tkinter import ttk,messagebox
from subprocess import call
class FormMysql :
    def __init__(self, root) :
        self.root=root
        self.root.title("MENU DES CLIENTS")
        self.root.geometry("1350x1000+0+0")
        self.root.configure(background="#091021")
        #champs du formulaire
        frame1 = Frame(self.root, bg="black")
        frame1.place(x=0, y=0, width=1350, height=100)

        title = Label(root, text="FORMULAIRE DU CLIENT", font=('Lucida handwriting', 20), bg="#2f4f4f",fg="white").place(x=0, y=0,width=1350 ,height=100)
        
        #prenom
        txt_code= Label(root, text="CODE", font=("Lucida handwriting", 15), bg="#091021", fg="white").place(x=50, y=150,width=100)
        self.ecr_code=Entry(root, font=("times new roman", 15), bg="lightgrey")
        self.ecr_code.place(x=250, y=150, width=250)

        #nom
        txt_nom= Label(root,text="NOM", font=("Lucida handwriting", 15), bg="#091021", fg="white").place(x=50, y=200,width=100)
        self.ecr_nom=Entry(root,font=("times new roman", 15), bg="lightgrey")
        self.ecr_nom.place(x=250, y=200, width=250)

        #prenom
        txt_telephone= Label(root,text="PRENOM", font=("Lucida handwriting", 15), bg="#091021", fg="white").place(x=50, y=250,width=100)
        self.ecr_prenom=Entry(root,font=("times new roman", 15), bg="lightgrey")
        self.ecr_prenom.place(x=250, y=250, width=250)

        #adresse
        txt_ad= Label(root,text="ADRESSE", font=("Lucida handwriting", 15), bg="#091021", fg="white").place(x=50, y=300,width=100)
        self.ecr_ad=Entry(root,font=("times new roman", 15), bg="lightgrey")
        self.ecr_ad.place(x=250, y=300, width=250)

        #tel
        txt_tel= Label(root,text="TELEPHONE", font=("Lucida handwriting", 15), bg="#091021", fg="white").place(x=50, y=350,width=100)
        self.ecr_tel=Entry(root,font=("times new roman", 15), bg="lightgrey")
        #self.ecr_nationalite["values"]=("Cameroun","Senegale","France","Chine","Gabon","Egypte","Algerie","Marroc","Serbie","Mali")
        self.ecr_tel.place(x=250, y=350, width=250)
        
        txt_email= Label(root,text="EMAIL", font=("Lucida handwriting", 15), bg="#091021", fg="white").place(x=50, y=400,width=100)
        self.ecr_email=Entry(root,font=("times new roman", 15), bg="lightgrey")
        self.ecr_email.place(x=250, y=400, width=250)

      
      

        #date
        #txt_date= Label(frame1,text="Date", font=("time new roman", 15), bg="grey", fg="black").place(x=50, y=280)
        #self.ecr_date=DateEntry(frame1,font=("times new roman", 15), state="readonly", bg="lightgrey" ,date_pattern="dd/mm/yy")
        #self.ecr_date.place(x=50, y=310, width=250)
        bretour = Button(root, text="Retour", font=('lucida', 10), command= self.retour,width=8, height=3)
        bretour.place(x=100, y=15)

        btn= Button(root, text="Valider",font=("impact", 15),command=self.achat, bg="green", fg="black").place(x=250, y=500 ,width=150)
        table = ttk.Treeview(root, columns=(1,2,3,4,5,6), height= 5,  show="headings")
        table.place(x= 550, y= 100, width=700, height=450)
        table.heading(1 , text = "CODE")
        table.heading(2 , text = "NOM")
        table.heading(3 , text = "PRENOM")
        table.heading(4 , text = "TELEPHONE")
        table.heading(5 , text = "ADRESSE")
        table.heading(6 , text = "EMAIL")
    



#elements des colonnes
        table.column(1,width = 100)
        table.column(2,width = 100)
        table.column(3,width = 150)
        table.column(4,width = 100)
        table.column(5,width = 100)
        table.column(6,width = 50)
        

        con = pymysql.connect(host="localhost", user="root", password="", database="etude")
        cur = con.cursor()
        cur.execute("select * from client")
        for row in cur:
         table.insert('', END, value = row)
        con.close()


    def reini(self):
        self.ecr_code.delete(0, END)
        self.ecr_nom.delete(0, END)
        self.ecr_prenom.delete(0, END)
        self.ecr_ad.delete(0, END)
        self.ecr_email.delete(0, END)
        self.ecr_tel.delete(0, END)
    
       
    def retour( self):

     root.destroy()
     call(["python", "main.py"])
#ma fenetre  
       

    def achat(self):
        if self.ecr_code.get()=="" or self.ecr_nom.get()=="":
         messagebox.showerror("Erreur", "Remplissez tous les champs", parent=self.root)
        else:
       
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="etude")
                cur=con.cursor()
                cur.execute("select* from client where email=%s", self.ecr_email.get())
                row = cur.fetchone()

                if row!=None:
                    messagebox.showerror("Erreur", "ce mail existe deja, Essayer un autre email", parent=self.root)
                else:
                    cur.execute("insert into client(code, nom, prenom,telephone,adresse, email) values(%s,%s,%s,%s,%s,%s)",
                                (self.ecr_code.get(),
                                self.ecr_nom.get(),
                                self.ecr_prenom.get(),
                                self.ecr_tel.get(),
                                self.ecr_ad.get(),
                                self.ecr_email.get(),
                                 
                                 
                                
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ajout Effectué!!", parent=self.root)
                    self.reini()
            except Exception as es:
                messagebox.showerror("Erreur",f"Erreur de connexion : {str(es)})",parent=self.root)    







root=Tk()
obj=FormMysql(root)
root.mainloop()