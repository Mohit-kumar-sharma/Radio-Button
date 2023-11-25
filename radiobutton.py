from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()

root.geometry("700x300")
root.title("Radio Button")

def order():
    print("we have recieved your order")
    tmsg.showinfo("Order recieved",f"we have recieved your order for {Var.get()},Thanks for ordering")
Var=StringVar()
Var.set("radio")

label=Label(root,text="what would you like to have sir?",font="lucida,20,Bold",justify=LEFT,padx=14)
label.pack()

radio=Radiobutton(root,text="Dosa",padx=14,variable=Var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="paratha",padx=14,variable=Var,value="paratha").pack(anchor="w")
radio=Radiobutton(root,text="idly",padx=14,variable=Var,value="Idly").pack(anchor="w")
radio=Radiobutton(root,text="samosa",padx=14,variable=Var,value="samosa").pack(anchor="w")


button=Button(root,text="Order Now",command=order,relief=SUNKEN,background="yellow",fg="black",borderwidth=10)
button.pack()

root.mainloop()