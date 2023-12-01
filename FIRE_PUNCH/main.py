import pyodbc

# Connect to your SQL Server database
# server = input("Enter the SQL Server name: ")
# database = input("Enter the database name: ")
# username = input("Enter your SQL Server username: ")
# password = input("Enter your SQL Server password: ")
server = ''
database = ''
username = ''
password = ''

conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def insert_message(message):
    # Insert the message into the database
    cursor.execute("INSERT INTO [Smietnisko].[dbo].[FP_Message] (Message) VALUES (?)", message)
    conn.commit()

def show_latest_message():
    # Retrieve the latest message from the database
    cursor.execute("SELECT Message FROM [Smietnisko].[dbo].[FP_Message] ORDER BY Message_ID DESC")
    rows = cursor.fetchall()
    if rows:
            print("Latest messages:")
            for row in rows:
                print(row.Message)
    else:
        print("No messages available.")

# Get user input
message = input("Type your message: ")

# Insert the message into the database
insert_message(message)

# Show the latest message
show_latest_message()

# Close the connection
cursor.close()
conn.close()