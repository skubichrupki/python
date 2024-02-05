import pandas

# import dataframe (table/csv)
file_path = 'C:\\Users\\skupi\\Downloads\\GIT\\PYTHON\\BA\\Results.csv'
df = pandas.read_csv(file_path)

print(df.info())

