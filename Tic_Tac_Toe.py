from tkinter import *
root= Tk()
root.title("Tic Tac Toe")
root.geometry("260x340")
turn="X"
s1=StringVar()
s1.set("")

def check_win():
    if (s1.get()==s2.get()==s3.get()!=""):
        L1=Label(root,text=s1.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if (s4.get()==s5.get()==s6.get()!=""):
        L2=Label(root,text=s4.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if (s7.get()==s8.get()==s9.get()!=""):
        L3=Label(root,text=s7.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if (s1.get()==s4.get()==s7.get()!=""):
        Label(root,text=s1.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if (s2.get()==s5.get()==s8.get()!=""):
        Label(root,text=s2.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if (s3.get()==s6.get()==s9.get()!=""):
        Label(root,text=s3.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if (s1.get()==s5.get()==s9.get()!=""):
        Label(root,text=s1.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if (s3.get()==s5.get()==s7.get()!=""):
        Label(root,text=s3.get()+"--WON",font=("Courier",15)).grid(row=3,column=1)
        return True
    if s1.get()!="" and s2.get()!="" and s3.get()!="" and s4.get()!="" and s5.get()!="" and s6.get()!="" and s7.get()!="" and s8.get()!="" and s9.get()!="":
        Label(root,text="TIE",font=("Courier",15)).grid(row=3,column=1)
        return True
    return False

def change_text(s):
    global turn
    if turn=="X":
        s.set("X")
        if check_win():
            turn="no"
        else:
            turn="O"
    elif turn=="O":
        s.set("O")
        if check_win():
            turn="no"
        else:
            turn="X"

l1=Button(root,textvariable=s1,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s1)).grid(row=0,column=0)
s2=StringVar()
s2.set("")
l2=Button(root,textvariable=s2,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s2)).grid(row=0,column=1)
s3=StringVar()
s3.set("")
l3=Button(root,textvariable=s3,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s3)).grid(row=0,column=2)
s4=StringVar()
s4.set("")
l4=Button(root,textvariable=s4,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s4)).grid(row=1,column=0)
s5=StringVar()
s5.set("")
l5=Button(root,textvariable=s5,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s5)).grid(row=1,column=1)
s6=StringVar()
s6.set("")
l6=Button(root,textvariable=s6,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s6)).grid(row=1,column=2)
s7=StringVar()
s7.set("")
l7=Button(root,textvariable=s7,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s7)).grid(row=2,column=0)
s8=StringVar()
s8.set("")
l8=Button(root,textvariable=s8,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s8)).grid(row=2,column=1)
s9=StringVar()
s9.set("")
l9=Button(root,textvariable=s9,bg="light blue",borderwidth=5,relief="ridge",height=5,width=10,command=lambda:change_text(s9)).grid(row=2,column=2)
def restart():
    global turn
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    s6.set("")
    s7.set("")
    s8.set("")
    s9.set("")
    turn="X"
    Label(root, text="",width=23).grid(row=3,column=1, columnspan=3)


b=Button(root, text="QUIT",bg="red",borderwidth=5,relief="raised",width=10,command=root.destroy).grid(row=4,column=2)
b1=Button(root, text="Restart", bg="red",borderwidth=5,relief="raised",width=10,command=restart).grid(row=4,column=0)
root.mainloop()
