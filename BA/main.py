# import pandas
import pyodbc
from prettytable import PrettyTable
from dotenv import load_dotenv

load_dotenv()

# Define the connection string
server = 'skubi_pecet\SQLEXPRESS'
database = 'tda'
username = 'scooby'
password = 'scooby'
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

connection = pyodbc.connect(conn_str)
cursor = connection.cursor()
query = 'SELECT * FROM item'
cursor.execute(query)

columns = [column[0] for column in cursor.description]
rows = cursor.fetchall()
table = PrettyTable(columns)


for row in rows:
    table.add_row(row)

table.border = True

print(table)

cursor.close()
connection.close()
