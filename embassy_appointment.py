import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="avinash"
)
mycursor = mydb.cursor()

class Appointment:
    def __init__(self, user, date, time, purpose):
        self.user = user
        self.date = date
        self.time = time
        self.purpose = purpose

    def get_details(self):
        return f'Appointment for {self.user} on {self.date} at {self.time} for {self.purpose}'

class AppointmentScheduler:
    def createdb():
        try:
            mycursor.execute("CREATE DATABASE Embassy")
        except Exception:
            print('Already Created DB')

    def useDB():
        try:
            mycursor.execute("USE Embassy")
            print("using DB")
        except Exception:
            print('Already Used DB')
    
    def createTable():
        try:
            mycursor.execute("CREATE TABLE Appsedul(user varchar(30),date varchar(20),time varchar(30),purpose varchar(30))")
            print("Table created successfully")
        except Exception:
            print('Already Created Table')
    
    def schedule_appointments():
        user=input("Enter user's name: ")
        date=input("Enter appointment date: ")
        time=input("Enter appointment time: ")
        purpose=input("Enter Purpose of appointment: ")
        try:
            mycursor.execute("INSERT INTO Appsedul(user,date,time,purpose) values(%s,%s,%s,%s)",(user,date,time,purpose))
            mydb.commit()
            print(f'Appointment scheduled successfully for {user}')          
        except Exception: 
            print('Issue while inserting data')

    def view_appointments():
        mycursor.execute("SELECT * FROM Appsedul")
        appointments = mycursor.fetchall()
        print("All appointment details:-")
        for appointment in appointments:
            print(Appointment(*appointment).get_details())
            
    
    def update_Appointment():
        date=input("Enter new date: ")
        user=input("Enter the name of user whose data to be updated: ")
        try:
            mycursor.execute("UPDATE Appsedul SET date=%s WHERE user=%s",(date,user))
            mydb.commit()
            print(f'Rescheduled appointment for {user} on {date} Successfully!')
        except Exception:
            print('Issue while rescheduling')
            
    def delete_Appointment():
        user=input("Enter name of user to be deleted: ")
        try:
            mycursor.execute("DELETE FROM Appsedul WHERE user=%s",(user,))
            mydb.commit()
            print(f'Appointment of {user} has been cancelled')
        except Exception:
            print('Issue while Deleting')
        
As=AppointmentScheduler
As.createdb()
As.useDB()
As.createTable()
As.schedule_appointments()
As.update_Appointment()
As.delete_Appointment()
As.view_appointments()
