from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

from tkinter import filedialog
import sqlite3
root = Tk()
root.title('Library Management System')
root.iconbitmap("D:\LBS\libico.ico")
root.geometry("900x650+300+150")
root.resizable(0, 0)

#Databases
# Create a databases or connect to one
conn = sqlite3.connect('libraryin.db')

# Create cursor
c = conn.cursor()
conn.commit()

# Create table
# c.execute(""" CREATE TABLE books(
#       userid integer,
#       title text,
#       author text, 
#       edition integer,
#       price integer
# ) """)



#Creating an update function
def update():
    # Create a databases or connect to one
    conn = sqlite3.connect('libraryin.db')
    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute(""" UPDATE books SET
         userid = :id,
         title= :tit,
         author = :auth,
         edition = :edi,
         price = :pri
         WHERE userid = :userid """,
         {'id': userid_editor.get(),
          'tit': title_editor.get(),
          'auth': author_editor.get(),
          'edi': edition_editor.get(),
          'pri': price_editor.get(),
          'userid': record_id
               }
    )
    conn.commit()
    conn.close()

    #Destroying all the data and closing window
    editor.destroy()


# Create submit button for databases
def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('libraryin.db')
    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO books VALUES (:userid, :title, :author, :edition, :price)",{
        'userid':u_id.get(),
        'title':btitle.get(),
        'author':bauthor.get(),
        'edition':bedition.get(),
        'price':bprice.get()
        #'zipcode':zipcode.get()
    })

    # showinfo messagebox
    messagebox.showinfo("Books", "Inserted Successfully")
    conn.commit()
    conn.close()
    # clear the text boxes
    u_id.delete(0,END)
    btitle.delete(0,END)
    bauthor.delete(0,END)
    bedition.delete(0, END)
    bprice.delete(0, END)

testf=LabelFrame(root,text="LIBRARY MANAGMENT SYSTEM",bg='light yellow',width=455,height=50,bd=9,
                 relief='groove',font=('arial',20,'bold'))
testf.place(x=230,y=30)


#frame for textbox
tframe=Frame(root,bg='#a7ecd9',width=900,height=390)
tframe.place(x=0,y=110)

#shows all book record function
def b_all_records():
    # Create a databases or connect to one
    conn = sqlite3.connect('libraryin.db')

    # Create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, userid FROM books")
    records = c.fetchall()

   # print(records)
    # Loop through the results
    print_record=''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record +="ID:- " +str(record[0]) + '\t'+" Title:- "+ str(record[1]) + '\t' +"Author:- "+ str(record[2]) + '\t'\
                        +"Edition:- "+ str(record[3]) + '\t'+"Price Rs:- " + str(record[4])+ "\t"  "\n"

    label=LabelFrame(tframe,text="ALL BOOKS DETAILS",width=30,bd=4,relief='groove',font=('arial',10,'bold'))
    label.place(x=550, y=0, height=20,width=155)
    query_label = Label(tframe, text=print_record)
    query_label.place(x=380,y=20,height=100)

    conn.commit()
    conn.close()


# Creating a function to delete a record
def delete():
    # create database
    conn = sqlite3.connect('libraryin.db')
    #create cursor
    c = conn.cursor()
    #delete a record
    c.execute("DELETE from books WHERE userid = " + delete_box.get())
    print('Deleted Successfully')
    # query of the database
    c.execute("SELECT *, userid FROM books")
    records = c.fetchall()
    # print(records)
    # Loop through the results
    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + '\t' + str(record[1]) + '\t' + str(record[2]) + '\t'+ "\n"
    query_label = Label(tframe, text=print_record)
    query_label.place(x=500,y=135,height=40)
    conn.commit()
    conn.close()



# Create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title('Update Books')
    editor.iconbitmap("D:\LBS\libico.ico")
    editor.geometry('400x300')
    editor.resizable(0, 0)

    # frame for edit/update
    eframe = Frame(editor, bg='#a7ecd9', width=900, height=390)
    eframe.place(x=0, y=0)

    # Create a databases or connect to one
    conn = sqlite3.connect('libraryin.db')
    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    # query of the database
    c.execute("SELECT * FROM books WHERE userid =" + record_id)
    records = c.fetchall()
    # print(records)

    #Creating global variable for all text boxes
    global userid_editor
    global title_editor
    global author_editor
    global edition_editor
    global price_editor

    # Create text boxes of update books
    userid_editor = Entry(eframe,width=30,bd=4,relief='groove',font=('arial',10,'bold'))
    userid_editor.place(x=120, y=20)
    title_editor = Entry(eframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
    title_editor.place(x=120, y=60)
    author_editor = Entry(eframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
    author_editor.place(x=120, y=100)
    edition_editor = Entry(eframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
    edition_editor.place(x=120, y=140)
    price_editor = Entry(eframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
    price_editor.place(x=120, y=180)

    # Create textbox labels of update books
    id_label = Label(eframe, text="User ID",fg='black',bg='light blue',font=('Arial',13,'bold'))
    id_label.place(x=20, y=20)
    Title_label = Label(eframe, text="Title",fg='black',bg='light blue',font=('Arial',13,'bold'))
    Title_label.place(x=20, y=60)
    Author_label = Label(eframe, text="Author",fg='black',bg='light blue',font=('Arial',13,'bold'))
    Author_label.place(x=20, y=100)
    Edition_label = Label(eframe, text="Edition",fg='black',bg='light blue',font=('Arial',13,'bold'))
    Edition_label.place(x=20, y=140)
    Price_label = Label(eframe, text="Price",fg='black',bg='light blue',font=('Arial',13,'bold'))
    Price_label.place(x=20, y=180)

    # loop through the results
    for record in records:
        userid_editor.insert(0, record[0])
        title_editor.insert(0, record[1])
        author_editor.insert(0, record[2])
        edition_editor.insert(0, record[3])
        price_editor.insert(0, record[4])


   # Create a update button
    edit_btn = Button(eframe, text=" UPDATE ", command=update,activeforeground='red'
                      ,width=20,height=2, fg='black', bg='light green', font=('Arial', 10, 'bold'))
    edit_btn.place(x=140,y=230)


# Create text boxes
u_id = Entry(tframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
u_id.place(x=130,y=20)
btitle = Entry(tframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
btitle.place(x=130,y=50)
bauthor = Entry(tframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
bauthor.place(x=130,y=80)
bedition = Entry(tframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
bedition.place(x=130,y=110)
bprice = Entry(tframe, width=30,bd=4,relief='groove',font=('arial',10,'bold'))
bprice.place(x=130,y=140)

# Create textbox labels
id_label = Label(tframe, text="ID",fg='black',bg='silver',font=('Arial',13,'bold'))
id_label.place(x=50,y=20)
title_label = Label(tframe, text="Title",fg='black',bg='silver',font=('Arial',13,'bold'))
title_label.place(x=50,y=50)
author_label = Label(tframe, text="Author",fg='black',bg='silver',font=('Arial',13,'bold'))
author_label.place(x=50,y=80)
edition_label = Label(tframe, text="Edition",fg='black',bg='silver',font=('Arial',13,'bold'))
edition_label.place(x=50,y=110)
price_label = Label(tframe, text="Price",fg='black',bg='silver',font=('Arial',13,'bold'))
price_label.place(x=50,y=140)

#frame for button
f1=Frame(root,bg='#fff',width=900,height=1920)
f1.place(x=0,y=300)

#open the image
bg=Image.open('D:\LBS\download.png')

#resize the image
resized=bg.resize((450,347),Image.ANTIALIAS)
newpic=ImageTk.PhotoImage(resized)

#bg=PhotoImage(file= 'D:\LBS\download.png')
my_label= Label(f1,image=newpic)
my_label.place(x=440,y=0)

# ENTRY BOX FOR DELETE BOX
delete_box = Entry(f1,width=40,bg="light blue" )
delete_box.place(x=150, y=125,height=35)

delete_box_label = Label(f1, text="USER ID",font=('Arial', 15, 'bold'),fg='black',bg="#fff",
                           width=7,height=0,bd=8,relief='flat',cursor='hand2')
delete_box_label.place(x=40, y=120)


# Create submit button
submit_btn = Button(f1, text="Add Books",fg='#fff',bg='#ff0076',font=('Arial',15,'bold'),width=10,
                          height=0,bd=7,relief='flat',command=submit,cursor='hand2')
submit_btn.place(x=40,y=40)

# Create query button
query_btn = Button(f1, text="Show Books",fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                            width=10,height=0, bd=7,relief='flat', command=b_all_records,cursor='hand2')
query_btn.place(x=250, y=40)

# Create a delete button
delete_btn = Button(f1, text="Delete", command=delete, fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                          width=10,height=0,bd=7,relief='flat',cursor='hand2')
delete_btn.place(x=40, y=200)

# Create a update button
edit_btn = Button(f1, text="Update", command=edit, fg='#fff', bg='#ff0076', font=('Arial', 15, 'bold'),
                           width=10,height=0,bd=7, relief='flat',cursor='hand2')
edit_btn.place(x=250, y=200)


# commit change
conn.commit()
# close connection
conn.close()

mainloop()