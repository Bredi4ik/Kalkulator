

#μ=Fb/Fr
#Fb=μ*Fr
#Fr=Fb/μ

import tkinter as tk

logs = tk.Tk()

logs.title("Berzes kalkulators")

logs.configure(bg="#49C33C")


def addotvet1():

    berzesspeks1 = berzesspeksievads1.get()

    speks1 = speksievads1.get()


    berzeskoeficents1=(int(berzesspeks1)/int(speks1))
    

    if berzesspeks1 and speks1:

        berzeskoeficentsievads1.insert(tk.END, f" {berzeskoeficents1}")


def addotvet2():

    berzeskoeficents2 = berzeskoeficentsievads2.get()

    speks2 = speksievads2.get()

    
    berzesspeks2=(int(berzeskoeficents2)*int(speks2))


    
    if berzeskoeficents2 and speks2:

        berzesspeksievads2.insert(tk.END, f" {berzesspeks2}")
        
        
        

def addotvet3():

    berzesspeks3 = berzesspeksievads3.get()

    berzeskoeficents3=berzeskoeficentsievads3.get()


    speks3=(int(berzesspeks3)/int(berzeskoeficents3))
    

    if berzesspeks3 and berzeskoeficents3:

        speksievads3.insert(tk.END, f" {speks3}")




def delete1():


    berzeskoeficentsievads1.delete(0, tk.END)

    berzesspeksievads1.delete(0, tk.END)
    
    speksievads1.delete(0, tk.END)


def delete2():


    berzeskoeficentsievads2.delete(0, tk.END)

    berzesspeksievads2.delete(0, tk.END)
    
    speksievads2.delete(0, tk.END)
    

def delete3():


    berzeskoeficentsievads3.delete(0, tk.END)

    berzesspeksievads3.delete(0, tk.END)
    
    speksievads3.delete(0, tk.END)












berzeskoeficentsmet1 = tk.Label(logs, text="μ:", bg="#8AD926")


berzeskoeficentsievads1 = tk.Entry(logs)

berzeskoeficentsievads1.configure(bg="#E9FEEB")



berzeskoeficentsmet2 = tk.Label(logs, text="μ:", bg="#8AD926")


berzeskoeficentsievads2 = tk.Entry(logs)

berzeskoeficentsievads2.configure(bg="#E9FEEB")



berzeskoeficentsmet3 = tk.Label(logs, text="μ:", bg="#8AD926")


berzeskoeficentsievads3 = tk.Entry(logs)

berzeskoeficentsievads3.configure(bg="#E9FEEB")



berzesspeksmet1 = tk.Label(logs, text="Fb:", bg="#8AD926")


berzesspeksievads1 = tk.Entry(logs)

berzesspeksievads1.configure(bg="#E9FEEB")


berzesspeksmet2 = tk.Label(logs, text="Fb:", bg="#8AD926")


berzesspeksievads2 = tk.Entry(logs)

berzesspeksievads2.configure(bg="#E9FEEB")


berzesspeksmet3 = tk.Label(logs, text="Fb:", bg="#8AD926")


berzesspeksievads3 = tk.Entry(logs)

berzesspeksievads3.configure(bg="#E9FEEB")


speksmet1 = tk.Label(logs, text="F:", bg="#8AD926")


speksievads1 = tk.Entry(logs)

speksievads1.configure(bg="#E9FEEB")


speksmet2 = tk.Label(logs, text="F:", bg="#8AD926")


speksievads2 = tk.Entry(logs)

speksievads2.configure(bg="#E9FEEB")



speksmet3 = tk.Label(logs, text="F:", bg="#8AD926")


speksievads3 = tk.Entry(logs)

speksievads3.configure(bg="#E9FEEB")






adpogu1 = tk.Button(logs, text="Atbilde",command=addotvet1, bg="#8AD926")
adpogu2 = tk.Button(logs, text="Atbilde",command=addotvet2, bg="#8AD926")
adpogu3 = tk.Button(logs, text="Atbilde",command=addotvet3, bg="#8AD926")

adpogudel1 = tk.Button(logs, text="Izdzest",command=delete1, bg="#FF4500")
adpogudel2 = tk.Button(logs, text="Izdzest",command=delete2, bg="#FF4500")
adpogudel3 = tk.Button(logs, text="Izdzest",command=delete3, bg="#FF4500")












zime1= tk.Label(logs, text="=", bg="#49C33C")
zime2= tk.Label(logs, text="/", bg="#49C33C")
zime3= tk.Label(logs, text="=", bg="#49C33C")
zime4= tk.Label(logs, text="*", bg="#49C33C")
zime5= tk.Label(logs, text="=", bg="#49C33C")
zime6= tk.Label(logs, text="/", bg="#49C33C")









berzeskoeficentsmet1.grid(row=1, column=8, pady=5, padx=10)
berzeskoeficentsmet2.grid(row=2, column=2, pady=5, padx=10)
berzeskoeficentsmet3.grid(row=3, column=5, pady=5, padx=10)



berzeskoeficentsievads1.grid(row=1, column=9, pady=5, padx=10)
berzeskoeficentsievads2.grid(row=2, column=3, pady=5, padx=10)
berzeskoeficentsievads3.grid(row=3, column=6, pady=5, padx=10)

berzesspeksmet1.grid(row=1, column=2, pady=5, padx=10)
berzesspeksmet2.grid(row=2, column=8, pady=5, padx=10)
berzesspeksmet3.grid(row=3, column=2, pady=5, padx=10)

berzesspeksievads1.grid(row=1, column=3, pady=5, padx=10)
berzesspeksievads2.grid(row=2, column=9, pady=5, padx=10)
berzesspeksievads3.grid(row=3, column=3, pady=5, padx=10)


speksmet1.grid(row=1, column=5, pady=5, padx=10)
speksmet2.grid(row=2, column=5, pady=5, padx=10)
speksmet3.grid(row=3, column=8, pady=5, padx=10)

speksievads1.grid(row=1, column=6, pady=5, padx=10)
speksievads2.grid(row=2, column=6, pady=5, padx=10)
speksievads3.grid(row=3, column=9, pady=5, padx=10)


zime1.grid(row=1, column=7, pady=5, padx=10)
zime2.grid(row=1, column=4, pady=5, padx=10)
zime3.grid(row=2, column=7, pady=5, padx=10)
zime4.grid(row=2, column=4, pady=5, padx=10)
zime5.grid(row=3, column=7, pady=5, padx=10)
zime6.grid(row=3, column=4, pady=5, padx=10)


adpogu1.grid(row=1, column=10, pady=5, padx=10)
adpogu2.grid(row=2, column=10, pady=5, padx=10)
adpogu3.grid(row=3, column=10, pady=5, padx=10)

adpogudel1.grid(row=1, column=11, pady=5, padx=10)
adpogudel2.grid(row=2, column=11, pady=5, padx=10)
adpogudel3.grid(row=3, column=11, pady=5, padx=10)

logs.mainloop()

