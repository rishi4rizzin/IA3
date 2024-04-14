import tkinter.messagebox
from tkinter import Tk, Label, Entry, Button, Frame
import mysql.connector as sqlcon
import random as rd
from tkinter import Tk, Label, Entry, Button, Frame, messagebox, simpledialog, PhotoImage
from tkinter.constants import *



# Establish connection to MySQL database
try:
    con = sqlcon.connect(host="localhost", user="root", password="6363")
    cur = con.cursor(buffered=True)
    cur.execute("create database if not exists TaxiService")
    cur.execute("use TaxiService")
    cur.execute("create table if not exists booking (idno varchar(12) primary key, name char(50), "
                "age char(3), gender char(1), phone varchar(10), destination varchar(50))")
    cur.execute("create table if not exists booking_details (idno varchar(12) primary key, driver varchar(50), "
                "date varchar(20), time varchar(20), booking_no varchar(10))")
    print("Connection successful")
except sqlcon.Error as e:
    print(f"Error connecting to MySQL: {e}")

# Function for user registration
def register_user():
    def register():
        idno = e1.get()
        name = e2.get()
        age = e3.get()
        gender = e4.get()
        phone = e5.get()
        destination = e6.get()
        query = 'insert into booking values(%s, %s, %s, %s, %s, %s)'
        data = (idno, name, age, gender, phone, destination)
        cur.execute(query, data)
        con.commit()
        tkinter.messagebox.showinfo("Registration Complete", "You have been registered successfully.")

    root = Tk()
    root.title("Customer Registration")
    root.geometry("400x400")
    Label(root, text="Customer Registration", font='Arial 16 bold').pack()
    frame = Frame(root)
    frame.pack()

    fields = ["ID No.", "Name", "Age", "Gender M/F", "Phone", "Destination"]
    entries = []

    for idx, field in enumerate(fields):
        Label(root, text=field).place(x=10, y=70+idx*40)
        entry = Entry(root)
        entry.place(x=200, y=70+idx*40)
        entries.append(entry)

    Button(root, text="Submit", command=register).place(x=150, y=300)

    # Assigning each entry widget to its respective variable
    e1, e2, e3, e4, e5, e6 = entries  # Define the entry widgets before accessing them

    root.mainloop()



# Function for booking a taxi
import tkinter.messagebox

# Function for booking a taxi
def book_taxi():
    def booking_details():
        destination = x2.get()
        booking_date = x3.get()
        booking_time = x4.get()
        vehicle_type = x5.get()  # New field for vehicle type
        drivers = {
            "Chennai": ["John", "David", "Matthew"],
            "Thrissur": ["Michael", "James", "Christopher"],
            "Kochi": ["Daniel", "Robert", "Joseph"],
            "Palakkad": ["Richard", "Charles", "Thomas"],
            "Coimbatore": ["William", "Mark", "Brian"]
        }

        attractions = {
            "Chennai": ["Marina Beach", "Kapaleeshwarar Temple", "Fort St. George"],
            "Thrissur": ["Vadakkunnathan Temple", "Thrissur Zoo", "Athirappilly Waterfalls"],
            "Kochi": ["Mattancherry Palace", "Fort Kochi Beach", "Jew Town"],
            "Palakkad": ["Palakkad Fort", "Malampuzha Dam", "Parambikulam Tiger Reserve"],
            "Coimbatore": ["Dhyanalinga", "Marudhamalai Temple", "Kovai Kutralam Falls"]
        }

        if destination in drivers:
            selected_driver = rd.choice(drivers[destination])
            booking_no = rd.choice([23, 34, 12, 67, 53, 72])
            booking_details = f"Your taxi is booked to {destination}\nDriver: {selected_driver}\nDate: {booking_date}\n" \
                              f"Time: {booking_time}\nVehicle Type: {vehicle_type}\nBooking No: {booking_no}"  # Include vehicle type
            tkinter.messagebox.showinfo("Booking Details", booking_details)

            # Display attractions in the destination
            if destination in attractions:
                attraction_info = "\nAttractions in the destination:\n" + "\n".join(attractions[destination])
                tkinter.messagebox.showinfo("Attractions", attraction_info)
            else:
                tkinter.messagebox.showinfo("Attractions", "No attractions found in the destination.")

            # Show thank you message
            tkinter.messagebox.showinfo("Thank You", "Thank you for using our services!")

        else:
            tkinter.messagebox.showwarning("Invalid Destination", "Please enter a valid destination.")

    root = Tk()
    root.title("Book a Taxi")
    root.geometry("400x500")  # Increased height to accommodate the new field
    Label(root, text="Book a Taxi", font='Arial 16 bold').pack()
    frame = Frame(root)
    frame.pack()

    Label(root, text="Destination").place(x=50, y=70)
    x2 = Entry(root)
    x2.place(x=200, y=70)

    Label(root, text="Date").place(x=50, y=100)
    x3 = Entry(root)
    x3.place(x=200, y=100)

    Label(root, text="Time (24-hour format)").place(x=50, y=130)
    x4 = Entry(root)
    x4.place(x=200, y=130)

    Label(root, text="Vehicle Type").place(x=50, y=160)  # New field for vehicle type
    x5 = Entry(root)
    x5.place(x=200, y=160)

    Button(root, text="Submit", command=booking_details).place(x=150, y=230)  # Adjusted position

    root.mainloop()




# Function to display list of drivers
# Function to display list of drivers
def display_drivers():
    root = Tk()
    root.title("List of Drivers")
    root.geometry("600x400")  # Increased width to accommodate new information
    root.configure(bg="#f0f0f0")  # Set background color

    # Title label
    title_label = Label(root, text="List of Drivers", font='Arial 16 bold', bg="#ffd700", fg='black', pady=10)
    title_label.pack()

    # Frame for driver information
    driver_frame = Frame(root, bg="#f0f0f0")
    driver_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)  # Fill both directions, expand, add padding

    drivers_list = {
        "Chennai": [("John", "Negative"), ("David", "Positive"), ("Matthew", "Not tested")],  # Example data
        "Thrissur": [("Michael", "Negative"), ("James", "Negative"), ("Christopher", "Positive")],
        "Kochi": [("Daniel", "Not tested"), ("Robert", "Negative"), ("Joseph", "Negative")],
        "Palakkad": [("Richard", "Negative"), ("Charles", "Positive"), ("Thomas", "Not tested")],
        "Coimbatore": [("William", "Negative"), ("Mark", "Positive"), ("Brian", "Negative")]
    }

    for key, value in drivers_list.items():
        # Subtitle label for each city
        city_label = Label(driver_frame, text=f"{key} Drivers:", font='Arial 12 bold', bg="#f0f0f0", pady=5)
        city_label.pack(anchor=W)

        # Display driver information
        for driver, status in value:
            driver_info_label = Label(driver_frame, text=f"Driver: {driver}, Covid Status: {status}", font='Arial 10', bg="#f0f0f0")
            driver_info_label.pack(anchor=W, padx=20)

    root.mainloop()

def view_bookings():
    # Fetch previous bookings from the database
    cur.execute("SELECT * FROM booking_details")
    bookings = cur.fetchall()

    # Create a new window to display the bookings
    root = Tk()
    root.title("Previous Bookings")
    root.geometry("400x400")
    Label(root, text="Previous Bookings", font='Arial 16 bold').pack()

    if not bookings:
        Label(root, text="No previous bookings", font='Arial 12').pack()
    else:
        # Display each booking in the window
        for booking in bookings:
            Label(root, text=f"Booking No: {booking[4]}", font='Arial 12').pack()
            Label(root, text=f"Destination: {booking[0]}", font='Arial 12').pack()
            Label(root, text=f"Driver: {booking[1]}", font='Arial 12').pack()
            Label(root, text=f"Date: {booking[2]}", font='Arial 12').pack()
            Label(root, text=f"Time: {booking[3]}", font='Arial 12').pack()
            Label(root, text="---------------------", font='Arial 12').pack()

    root.mainloop()

from tkinter import messagebox, simpledialog

import tkinter.messagebox

# Function to cancel a booking
def cancel_booking():
    # Prompt user to enter booking ID
    booking_id = simpledialog.askstring("Cancel Booking", "Enter booking ID to cancel:")

    if not booking_id:
        # User clicked cancel or entered empty string
        return

    try:
        # Execute DELETE query to remove booking from the database
        cur.execute("DELETE FROM booking_details WHERE booking_no = %s", (booking_id,))
        con.commit()

        # Check if any row was affected (booking was canceled)
        if cur.rowcount > 0:
            messagebox.showinfo("Booking Canceled", f"Booking {booking_id} has been canceled successfully.")
        else:
            messagebox.showwarning("Booking Not Found", f"No booking with ID {booking_id} found.")
    except sqlcon.Error as e:
        # Display error message if cancellation fails
        messagebox.showerror("Error", f"Failed to cancel booking: {e}")
    





# Function to view previous bookings
def view_bookings():
    # Fetch previous bookings from the database
    cur.execute("SELECT * FROM booking_details")
    bookings = cur.fetchall()

    # Create a new window to display the bookings
    root = Tk()
    root.title("Previous Bookings")
    root.geometry("400x400")
    Label(root, text="Previous Bookings", font='Arial 16 bold').pack()

    if not bookings:
        Label(root, text="No previous bookings", font='Arial 12').pack()
    else:
        # Display each booking in the window
        for booking in bookings:
            Label(root, text=f"Booking No: {booking[4]}", font='Arial 12').pack()
            Label(root, text=f"Destination: {booking[0]}", font='Arial 12').pack()
            Label(root, text=f"Driver: {booking[1]}", font='Arial 12').pack()
            Label(root, text=f"Date: {booking[2]}", font='Arial 12').pack()
            Label(root, text=f"Time: {booking[3]}", font='Arial 12').pack()
            Label(root, text="---------------------", font='Arial 12').pack()

    root.mainloop()

# Main GUI for Taxi Booking Service
def main_gui():
    root = Tk()
    root.title("Taxi Booking Service")
    root.geometry("400x400")
    root.configure(bg="#f0f0f0")  # Set background color

    # Title label
    title_label = Label(root, text="Welcome to Taxi Booking Service", bg='#ffd700', fg='black', font='Arial 16 bold', pady=10)
    title_label.pack()

    # Frame for buttons
    button_frame = Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=20)

    # Register button
    register_btn = Button(button_frame, text="Register", font="Arial 12", width=15, command=register_user)
    register_btn.grid(row=0, column=0, padx=10)

    # Book a Taxi button
    book_taxi_btn = Button(button_frame, text="Book a Taxi", font="Arial 12", width=15, command=book_taxi)
    book_taxi_btn.grid(row=0, column=1, padx=10)

    # List of Drivers button
    drivers_btn = Button(button_frame, text="List of Drivers", font="Arial 12", width=15, command=display_drivers)
    drivers_btn.grid(row=1, column=0, padx=10, pady=5)

    # Previous Bookings button
    bookings_btn = Button(button_frame, text="Previous Bookings", font="Arial 12", width=15, command=view_bookings)
    bookings_btn.grid(row=1, column=1, padx=10, pady=5)

    # Cancel Booking button
    cancel_btn = Button(button_frame, text="Cancel Booking", font="Arial 12", width=15, command=cancel_booking)
    cancel_btn.grid(row=2, column=0, columnspan=2, pady=5)

    # Exit button
    exit_btn = Button(root, text="Exit", font="Arial 12", width=10, command=root.destroy)
    exit_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()

