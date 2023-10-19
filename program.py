import pyodbc

# Connection parameters
server = 'SKUBI_PECET\SQLEXPRESS'
database = 'tda'
username = 'your_username'
password = 'your_password'

# Use Trusted_Connection for Windows Authentication
connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

# Connection cursor
cursor = connection.cursor()

ins_query = "INSERT INTO Worker (Description) VALUES ('knur')"
sel_query = "SELECT * FROM Worker"

# Execute SQL Insert Query
cursor.execute(ins_query)

# Commit Query
connection.commit() 

# Execute SQL Select Query
cursor.execute(sel_query)

# Rows is a table
# for every row (i) in rows print row
rows = cursor.fetchall()
for i in rows:
    print(i)

# Close the connection
cursor.close()
connection.close()