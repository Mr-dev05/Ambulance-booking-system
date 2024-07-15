import mysql.connector as d
import datetime
from tabulate import tabulate

import tkinter as tk
from tkinter import messagebox

mydb=d.connect(host='localhost',user='root',passwd='mysql')
cur=mydb.cursor()
cur.execute("create database if not exists Emergency_service_system")
cur.execute("use Emergency_service_system")

#user_account
userdata="create table if not exists user_data(user_name varchar(40),\
password varchar(40) primary key, \
phno varchar(15))"
cur.execute(userdata)
        
#Ambulance Booking Table
booking="create table if not exists Ambulance_Booking(Pname varchar(40),\
age varchar(4),\
gender varchar(50),\
phno varchar(20),\
Ambulance_code varchar(20),\
Current_location varchar(20),\
to_hospital varchar(20),\
Date varchar(50),Time varchar(50))"
cur.execute(booking)

#Ambulance
Ambulance="create table if not exists Ambulance(Ambulance_type varchar(40),\
Ambulance_code varchar(20) primary key,\
With_In_5km varchar(50),\
With_In_10km varchar(30),\
Hospital varchar(50))"
cur.execute(Ambulance)

def date():
    n=datetime.datetime.now()
    print(n.strftime("\t\t\t %d-%m-%y %M:%M:%S"))



def menu():
    while True:
        date()
        print("="*99,end="")
        print()
        print('\t\t\t','WELCOME TO OUR AMBULANCE BOOKING SYSTEM')
        print('\t\t\t',chr(773)*40)
        print("="*99,end="")
        print('\t\t\t\t\t',"DESIGNED AND DEVELOPED BY ")
        print('\t\t\t\t',chr(773)*25,end="")
        print()
        print('\t\t\t\t',"-"*20,end="")
        print()
        print('\t\t\t\t',chr(187),"ASHMIT ARORA",chr(171))
        print('\t\t\t\t',"-"*20,end="")
        print()
        print('\t\t\t\t',chr(187),"INKUNIKA RANA",chr(171))
        print('\t\t\t\t',"-"*20,end="")
        print()
        print('\t\t\t\t',"-"*20,end="")
        print()
        c=input("PRESS ANY KEY TO CONTINUE:")
        print("="*99,end="")
        print("\t"*4,"1.BOOKING")
        print("\t"*3,"2.SHOW YOUR DATA")
        print("\t"*3,"3.UPDATE YOUR ACCOUNT")
        print("\t"*3,"4.EXIT")
        print("="*99,end="")

        ch=int(input("Enter the Choice:"))
        if ch==1:
            main()
        elif ch==2:
            a=show_data()
        elif ch==3:
            a=update_ch()
        elif ch==4:
            print("Thankyou Come Again :)")
            quit()
        else:
            print('ERROR 404:PAGE NOT FOUND')

def Ambulance_booking():
    date()
    mydb.autocommit=True
    ambc=['B016','C213','B028','D156']
    n=(input("Enter Patient Name:")).upper()
    age=input("Enter age:")
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gen=(input("Enter Your Gender:")).upper()
    phno=input("Enter your phno:")
    ac=input("Enter the Ambulance_code You Want to Book:")
    cl=input("Enter the Current_Location:")
    th=input("Enter thr Hospital_Location:")
    d=input("Enter Date of Booking:")
    t=input("Enter Time of Booking:")
    if ac not in ambc:
        print("No Such Ambulance Exists")
    else:
        q="select Hospital from Ambulance where\
        Ambulance_code='{}'".format(ac)
        cur.execute(q)
        data=cur.fetchall()[0]
        data=list(data)
        k=data[0]
        s="insert into Ambulance_Booking values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n,age,gen,phno,ac,cl,th,d,t)
        cur.execute(s)
        print('AMBULANCE BOOKED SUCCESSFULLY ')
        return True


def Ambulance_checking():
    date()
    mydb.autocommit=True
    print('1.Yes')
    print('2.No')
    ch=int(input("Do you want to continue or not:"))
    if ch==1:
        phno=input('Enter your PhoneNo.:')
        try:
          s2="select * from Ambulance_Booking where phno='{}'".format(phno)
          cur.execute(s2)
          data=cur.fetchall()[0]
          data=list(data)
          if phno==data[3]:
                s1="select * from Ambulance_Booking where phno='{}'".format(phno)
                cur.execute(s1)
                print(tabulate(cur,headers=["PName","Age","Gender","PhoneNo.","Ambulance_code","Cur_loc","Hos_loc","Date","Time"],tablefmt="double_outline"))  
        except:
            print('BOOKING DOES NOT EXISTS')
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')


def Ambulance_cancelling():
    mydb.autocommit=True
    print('1.Yes')
    print('2.No')
    ch=int(input("Do you want to continue or not:"))
    if ch==1:
        phno=input('Enter your phone number:')
        s1="delete from ambulance_booking where phno='{}'".format(phno)
        cur.execute(s1)
        print('AMBULANCE CANCELLED')
        return True
    elif ch==2:
        print('THANK YOU')
    else:
        print('ERROR 404:PAGE NOT FOUND')

def Ambulanceinfo():
    date()
    c="select * from Ambulance"
    cur.execute(c)
    print(tabulate(cur,headers=["Ambulance_type","Ambulance_code","With_In_5km","With_In_10km","Hospital"],tablefmt="double_outline"))

def main():
    print('1.YES')
    print('2.NO')
    c=int(input("Do you want to continue or not:"))
    while (c==1):
        date()
        print('\t\t\t','1:AMBULANCE INFO')
        print('\t\t\t','2.AMBULANCE BOOKING')
        print('\t\t\t','3.AMBULANCE CHECKING')
        print('\t\t\t','4.AMBULANCE CANCELLING')
        print('\t\t\t','5.LOG OUT')

        ch=int(input('Enter Your choice:'))
        if ch==1:
            Ambulanceinfo()
        elif ch==2:
            Ambulance_booking()
        elif ch==3:
            Ambulance_checking()
        elif ch==4:
            Ambulance_cancelling()
        elif ch==5:
            print('THANK YOU')
            break
        else:
            print('WRONG INPUT')

def register_user():
    
    
    username=username_entry.get()
    password=password_entry.get()
    repassword=repassword_entry.get()
    phone_number=phone_entry.get()

    if not username or not password or not repassword or not phone_number:
        messagebox.showerror("Error","All fields are required!")
        

    if password!=repassword:
        messagebox.showerror("Error","Passwords do not match!")
        

    try:
        cur.execute("INSERT INTO user_data values('{}','{}','{}')".format(username.upper(),password.upper(),phone_number))
        mydb.commit()
        messagebox.showinfo("Success","Registration successful!")
    except d.Error as err:
        print(err)
        messagebox.showerror("Error","Failed to register user!")
        
def login():
    
    username=login_username_entry.get()
    password=login_password_entry.get()

    try:
        cur.execute("SELECT password FROM user_data WHERE user_name='{}'".format(username.upper()))
        user=cur.fetchone()

        if user and user[0]==password.upper():
            messagebox.showinfo("Success","Login successful!")
        else:
            messagebox.showerror("Error","Invalid username or password!")
    except d.Error as err:
        print(err)
        messagebox.showerror("Error","Failed to login!")
    
def exit_app():
    root.destroy()
    

# Create main window
root = tk.Tk()
root.title("Registration and Login System")

# Registration frame
registration_frame=tk.LabelFrame(root, text="Register")
registration_frame.pack(padx=20, pady=20)
tk.Label(registration_frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(registration_frame)
username_entry.grid(row=0, column=1)

tk.Label(registration_frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(registration_frame, show='*')
password_entry.grid(row=1, column=1)

tk.Label(registration_frame, text="Re-enter Password:").grid(row=2, column=0)
repassword_entry = tk.Entry(registration_frame, show='*')
repassword_entry.grid(row=2, column=1)

tk.Label(registration_frame, text="Phone Number:").grid(row=3, column=0)
phone_entry = tk.Entry(registration_frame)
phone_entry.grid(row=3, column=1)

tk.Button(registration_frame, text="Register", command=register_user).grid(row=4, columnspan=2, pady=10)


# Login frame
login_frame=tk.LabelFrame(root, text="Login")
login_frame.pack(padx=20, pady=20)

tk.Label(login_frame, text="Username:").grid(row=0, column=0)
login_username_entry = tk.Entry(login_frame)
login_username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password:").grid(row=1, column=0)
login_password_entry = tk.Entry(login_frame, show='*')
login_password_entry.grid(row=1, column=1)

tk.Button(login_frame, text="Login", command=login).grid(row=2, columnspan=2, pady=10)


# Exit button
tk.Button(root,text="Exit",command=exit_app).pack(pady=20)

root.mainloop()





def show_data():
     date()
     u=(input("Enter Your Username:")).upper()
     p=(input("Enter Your Password:")).upper()
     try:
       s="Select user_name from user_data where password='{}'".format(p)
       cur.execute(s)
       data=cur.fetchall()[0]
       data=list(data)
       if data[0]==u:
            c="select user_name,password,phno from user_data where password='{}'".format(p)
            cur.execute(c)
            print(tabulate(cur,headers=["User_name","Password","PhoneNo."],tablefmt="double_grid"))
       else:
         print("INCORRECT PASSWORD OR USERNAME")
     except:
             print('ACCOUNT DOES NOT EXIST')            

def update_ch():
        date()
        print("Which Field of Your Account You Want to Update?")
        print('\t\t',"1.Password")
        print('\t\t',"2.UserName")
        print('\t\t',"3.Phoneno")
        
        ch=int(input("Enter Your choice:"))
        if ch==1:
                update_pass()
        elif ch==2:
                update_uname()
        elif ch==3:
                update_phno()
        else:
            print("WRONG INPUT :(")
       
def update_pass():
      mydb.autocommit=True
      u=(input("Enter Your Username:")).upper()
      p=(input("Enter Your Passsword:")).upper()
      try:
       s="Select password from user_data where user_name='{}'".format(u)
       cur.execute(s)
       data=cur.fetchall()[0]
       data=list(data)
       if data[0]==p:
               x=(input("Enter Password To Modify:")).upper()
               name=x
               m="update user_data set password='{}' where user_name='{}'".format(name,u)
               cur.execute(m)
               print("Welcome See Ya!")
               print()
               return True
       else:
          print("INCORRECT PASSWORD OR USERNAME")
          return False
      except:
        print('ACCOUNT DOES NOT EXIST')


def update_uname():
      mydb.autocommit=True
      u=(input("Enter Your Username:")).upper()
      p=(input("Enter Your Passsword:")).upper()
      try:
       s="Select user_name from user_data where password='{}'".format(p)
       cur.execute(s)
       data=cur.fetchall()[0]
       data=list(data)
       if data[0]==u:
               x=(input("Enter UserName To Modify:")).upper()
               name=x
               m="update user_data set user_name='{}' where password='{}'".format(name,p)
               cur.execute(m)
               print("User_name Changed Successfully")
               print()
               return True
       else:
          print("INCORRECT PASSWORD OR USERNAME")
          return False
      except:
        print('ACCOUNT DOES NOT EXIST')

def update_phno():
      mydb.autocommit=True
      u=(input("Enter Your Username:")).upper()
      p=(input("Enter Your Passsword:")).upper()
      try:
       s="Select user_name from user_data where password='{}'".format(p)
       cur.execute(s)
       data=cur.fetchall()[0]
       data=list(data)
       if data[0]==u:
               x=input("Enter PhoneNo. To Modify:")
               name=x
               m="update user_data set phno='{}' where password='{}'".format(name,p)
               cur.execute(m)
               print("Phone_Number Changed Successfully")
               print()
               return True
       else:
          print("INCORRECT PASSWORD OR USERNAME")
          return False
      except:
        print('ACCOUNT DOES NOT EXIST')

menu()

