# Importamos sqlite3
import sqlite3 

# Conectamos con la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Creamos una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER,
        email TEXT UNIQUE   
    )
''')

# Insertarmos usuarios
cursor.execute('''
    INSERT INTO usuarios (nombre,edad,email)
    VALUES ('Mayra', 20, 'mayrayazminmoyano@gmail'),
            ('Lautaro', 21, 'lautaroloyola@gmail'),
            ('Luciana', 25, 'lucianamoreno@gmail'),
            ('Marilen', 19, 'marilencornejo@gmail'),
            ('Melina', 20, 'melinamoyano@gmail'),
            ('Leandro', 20, 'leandroyapur@gmail')
    ''')

# Consultamos los usuarios
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

# Actualizamos un usuario
cursor.execute('''
    UPDATE usuarios SET edad = 21 WHERE nombre = 'Mayra'
''',)

# Eliminamos un usuario
cursor.execute('''DELETE FROM usuarios WHERE nombre = 'Leandro'
''')

# Guardamos los cambios y cerramos la conexion
conn.commit()
conn.close()