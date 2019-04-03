from tkinter import *
#import pyttsx
import shutil
import os
##import win32com.client
#import win32com.client.gencache
import sqlite3
import tkinter.messagebox
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
idsp = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        
        self.heading = Label(self.left, text="ABC Hospital Appointments", font=('arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.place(x=0, y=0)
        
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=100)

       
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.age.place(x=0, y=140)

        
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.gender.place(x=0, y=180)

        
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.location.place(x=0, y=220)

        
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.time.place(x=0, y=260)

        
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.phone.place(x=0, y=300)

        
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)
    
        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)

        self.update = Button(self.left, text="Update Appointments", width=20, height=2, bg='steelblue', command=self.gotoupdate)
        self.update.place(x=120, y=340)

#        self.display = Button(self.left, text="Display Appointment", width=20, height=2, bg='steelblue', command=self.gotodisplay)
#        self.display.place(x=480, y=340)

    
       
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            idsp.append(self.id)
        
        
        self.new = sorted(idsp)
        self.final_id = self.new[len(idsp)-1]
        
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))
    
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )
            

            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))
    def gotoupdate(self):
         root2=Toplevel(self.master)
         upd=Update(root2)

    def gotodisplay(self):
         root3=Toplevel(self.master)
         disp=Display(root3)



class Update:
    def __init__(self, master):
        self.master = master
       
        self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        
        self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

        
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)
    
    def search_db(self):
        self.input = self.namenet.get()
        
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        
        self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=0, y=220)

        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=260)

        self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
        self.utime.place(x=0, y=300)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=340)

       
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        
number = []
patients = []

sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)
        

class Display:
    def __init__(self, master):
        self.master = master

        self.x = 0
        
        # heading
        self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
        self.heading.place(x=350, y=0)

        # button to change patients
        self.change = Button(master, text="Next Patient", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=500, y=600)

        # empty text labels to later config
        self.n = Label(master, text="", font=('arial 200 bold'))
        self.n.place(x=500, y=100)

        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=300, y=400)
    # function to speak the text and update the text
    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx.init()
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1        

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
