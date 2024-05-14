import sqlite3
conn=sqlite3.connect("sqlite.db") #for making & connecting database
conn.execute('''
create table student (
    st_id INT AUTO_INCREMENT PRIMARY KEY,
    st_name VARCHAR (50),
    st_class VARCHAR (50),
    st_contact VARCHAR (13),
    st_address VARCHAR (50),
    st_email VARCHAR (30)
)
''')
conn.close()