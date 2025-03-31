import _sqlite3

con = _sqlite3.connect("NOVA.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id interger primary key, name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command (id, name, path) VALUES (null, 'android studio', 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
cursor.execute(query)
con.commit()