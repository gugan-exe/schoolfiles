import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # change if your MySQL username is different
    password="your_password",  # change this to your password
    database="lost_found_db"
)

cursor = conn.cursor()

# Functions
def add_lost_item():
    name = input("Enter item name: ")
    desc = input("Enter description: ")
    loc = input("Enter location: ")
    date = input("Enter date lost (YYYY-MM-DD): ")
    sql = "INSERT INTO lost_items (name, description, location, lost_date) VALUES (%s, %s, %s, %s)"
    val = (name, desc, loc, date)
    cursor.execute(sql, val)
    conn.commit()
    print("Lost item added.\n")

def view_lost_items():
    cursor.execute("SELECT * FROM lost_items")
    rows = cursor.fetchall()
    print("\n Lost Items List:")
    for row in rows:
        print(row)

def add_found_item():
    name = input("Enter item name: ")
    desc = input("Enter description: ")
    loc = input("Enter location: ")
    date = input("Enter date found (YYYY-MM-DD): ")
    sql = "INSERT INTO found_items (name, description, location, found_date) VALUES (%s, %s, %s, %s)"
    val = (name, desc, loc, date)
    cursor.execute(sql, val)
    conn.commit()
    print("Found item added.\n")

def view_found_items():
    cursor.execute("SELECT * FROM found_items")
    rows = cursor.fetchall()
    print("\n Found Items List:")
    for row in rows:
        print(row)

# Main Menu
while True:
    print("\n====== Lost & Found Reporting System ======")
    print("1. Add Lost Item")
    print("2. View Lost Items")
    print("3. Add Found Item")
    print("4. View Found Items")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_lost_item()
    elif choice == "2":
        view_lost_items()
    elif choice == "3":
        add_found_item()
    elif choice == "4":
        view_found_items()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")

# Close the connection
conn.close()
