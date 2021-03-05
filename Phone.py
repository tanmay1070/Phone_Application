from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from tkinter import ttk
from playsound import playsound
from tkinter import messagebox
import cv2
cap = cv2.VideoCapture(0)

window = tk.Tk()
window.title("My Project")

desktop = ImageTk.PhotoImage(Image.open("phone.jpg"))
l1= Label(window,image=desktop)
l1.pack()

l2 = Label(text="welcome",font="Times 62")
l2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def gallery():

    global img
    global img1
    global img2
    global Scrollbar
    top=Toplevel()
    top.title("Gallery")
    img = ImageTk.PhotoImage(Image.open("cr7.jpg"))
    img1 = ImageTk.PhotoImage(Image.open("messi5.jpg"))
    img2=ImageTk.PhotoImage(Image.open("nature.jpg"))
    l3 = Label(top,image=img)
    l3.pack()
    l4 = Label(top,image=img1)
    l4.pack()
    l5 = Label(top, image=img2)
    l5.pack()

    b1=Button(top,text="close window",command=top.destroy)
    b1.pack()

photo = PhotoImage(file = "g.png")    # for adding icon to button
g = photo.subsample(20,20)
b2=Button(window,image = g,command=gallery)
b2.place(relx = 0.63, rely = 0.86, anchor = CENTER)

def calender():
    global img3
    top=Toplevel()
    top.title("calender")
    img3 = ImageTk.PhotoImage(Image.open("2020-calendar.png"))
    l6=Label(top,image=img3)
    l6.pack()
    b3 = Button(top, text="close window", command=top.destroy)
    b3.pack()

photo = PhotoImage(file = "cal.jpg")
cal = photo.subsample(20,20)
b4 = Button(window, image = cal,command=calender)
b4.place(relx = 0.37, rely = 0.86, anchor = CENTER)

photo = PhotoImage(file = "middle.png")
middle = photo.subsample(15,14)
b5 = Button(window, image = middle,command=window.destroy )
b5.place(relx = 0.5, rely = 0.86, anchor = CENTER)


def music():

    playsound('We Don t Talk Anymore - Charlie Puth (Ft. Selena Gomez).mp3')
photo = PhotoImage(file = "Apple-Music-logo.png")
mus = photo.subsample(7,7)
b6=Button(window,image = mus,command=music)
b6.place(relx = 0.6, rely = 0.6, anchor = CENTER )

def camera():
    counter = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            cv2.imshow("Camera", frame)

        key_value = cv2.waitKey(1)

        if key_value & 0xFF == ord('c') :
            image = "Successfully clicked {}.jpg".format(counter)
            cv2.imwrite(image, frame)
            print(image)
            counter += 1

        elif key_value & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
photo = PhotoImage(file = "camera.png")
cam = photo.subsample(3,3)
b7=Button(window,image = cam,command=camera)
b7.place(relx = 0.5, rely = 0.1, anchor = N)

def phonebase():
    global Scrollbar
    top=Toplevel()
    def connect():
        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS app (FirstName TEXT, Surname TEXT, Phone INT, Email TEXT)")
        conn.commit()
        conn.close()

    # All Variables Declaration
    # -------
    firstname = tk.StringVar()
    surname = tk.StringVar()
    phoneno = tk.IntVar()
    emailid = tk.StringVar()
    # --------
    fn = Label(top, text="First name")
    fn.pack()
    entry1 = Entry(top, textvariable=firstname)
    entry1.pack()

    sn = Label(top, text="Surname")
    sn.pack()
    entry2 = Entry(top, textvariable=surname)
    entry2.pack()

    ph = Label(top, text="Phone NO")
    ph.pack()
    entry3 = Entry(top, textvariable=phoneno)
    entry3.pack()

    em = Label(top, text="Email id")
    em.pack()
    entry4 = Entry(top, textvariable=emailid)
    entry4.pack()

    def save():
        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        c.execute('INSERT INTO app (FirstName,Surname,Phone, Email) VALUES (?,?,?,?)',
                  (entry1.get(), entry2.get(), entry3.get(), entry4.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Successfully Saved")
    b8 = Button(top, text="Save", command=save)
    b8.pack()

    def view():

        conn = sqlite3.connect("project.db")
        c = conn.cursor()
        c.execute("SELECT * FROM app")
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        conn.commit()
        conn.close()
    tree = ttk.Treeview(top, column=("column1", "column2", "column3", "column4"), show='headings')
    Scrollbar = Scrollbar(top, command=tree.yview)
    Scrollbar.pack(side='right', fill=Y)
    tree.config(yscrollcommand=Scrollbar.set)
    tree.heading("#1", text="FIRST NAME")
    tree.heading("#2", text="SURNAME")
    tree.heading("#3", text="PHONE")
    tree.heading("#4", text="EMAIL")
    tree.pack()

    b9 = Button(top, text="view", command=view)
    b9.pack()

    def delete():
        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        item_deleted = tree.selection()
        tree.delete(item_deleted)
        messagebox.askquestion("confirm", "Are you sure you want to delete?")
    b10 = Button(top, text="delete", command=delete)
    b10.pack()
photo = PhotoImage(file = "book.png")
contact = photo.subsample(7,7)    #Just to Adjust the size of Button
b11=Button(window,image=contact,command=phonebase)
b11.place(relx = 0.6, rely = 0.1, anchor = N)

window.geometry('789x900')
window.mainloop()

