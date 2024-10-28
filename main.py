import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conexión a la base de datos SQLite
conn = sqlite3.connect('gestion_clientes.db')
cursor = conn.cursor()

# Creación de la tabla de clientes (solo se ejecutará la primera vez)
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contacto TEXT NOT NULL,
    direccion TEXT,
    preferencias TEXT,
    fecha_creacion DATE DEFAULT CURRENT_DATE
)
''')
conn.commit()

# Creación de la tabla de interacciones
cursor.execute('''
CREATE TABLE IF NOT EXISTS interacciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    tipo TEXT NOT NULL,
    descripcion TEXT,
    fecha DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')
conn.commit()

# Función para agregar un cliente
def agregar_cliente(nombre, contacto, direccion='', preferencias=''):
    cursor.execute('''
    INSERT INTO clientes (nombre, contacto, direccion, preferencias)
    VALUES (?, ?, ?, ?)
    ''', (nombre, contacto, direccion, preferencias))
    conn.commit()
    print(f"Cliente {nombre} agregado exitosamente.")

# Función para editar un cliente
def editar_cliente(cliente_id, nombre=None, contacto=None, direccion=None, preferencias=None):
    campos = []
    valores = []
    
    if nombre:
        campos.append("nombre = ?")
        valores.append(nombre)
    if contacto:
        campos.append("contacto = ?")
        valores.append(contacto)
    if direccion:
        campos.append("direccion = ?")
        valores.append(direccion)
    if preferencias:
        campos.append("preferencias = ?")
        valores.append(preferencias)
        
    valores.append(cliente_id)
    query = f"UPDATE clientes SET {', '.join(campos)} WHERE id = ?"
    cursor.execute(query, valores)
    conn.commit()
    print(f"Cliente con ID {cliente_id} actualizado.")

# Función para eliminar un cliente
def eliminar_cliente(cliente_id):
    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    print(f"Cliente con ID {cliente_id} eliminado.")

# Función para listar todos los clientes
def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    df = pd.DataFrame(clientes, columns=['ID', 'Nombre', 'Contacto', 'Dirección', 'Preferencias', 'Fecha de Creación'])
    print(df)

# Función para agregar una interacción con un cliente
def agregar_interaccion(cliente_id, tipo, descripcion=''):
    cursor.execute('''
    INSERT INTO interacciones (cliente_id, tipo, descripcion)
    VALUES (?, ?, ?)
    ''', (cliente_id, tipo, descripcion))
    conn.commit()
    print(f"Interacción '{tipo}' con el cliente ID {cliente_id} agregada exitosamente.")

# Función para buscar clientes por nombre o fecha de creación y exportar todos si no se especifican filtros
def buscar_clientes(nombre=None, fecha_creacion=None):
    query = "SELECT * FROM clientes"
    valores = []
    
    if nombre or fecha_creacion:
        query += " WHERE 1=1"
        if nombre:
            query += " AND nombre LIKE ?"
            valores.append(f"%{nombre}%")
        if fecha_creacion:
            query += " AND fecha_creacion = ?"
            valores.append(fecha_creacion)

    cursor.execute(query, valores)
    clientes = cursor.fetchall()
    df = pd.DataFrame(clientes, columns=['ID', 'Nombre', 'Contacto', 'Dirección', 'Preferencias', 'Fecha de Creación'])
    print(df)

    # Guardar en un archivo CSV para informe
    df.to_csv("informe_clientes.csv", index=False)
    print("Informe generado en 'informe_clientes.csv'.")

# Función para visualizar clientes por preferencia
def graficar_preferencias():
    cursor.execute("SELECT preferencias, COUNT(*) as cantidad FROM clientes GROUP BY preferencias")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Preferencias', 'Cantidad'])

    # Graficar
    df.plot(kind='bar', x='Preferencias', y='Cantidad', legend=False)
    plt.title("Cantidad de Clientes por Preferencia")
    plt.xlabel("Preferencia")
    plt.ylabel("Cantidad")
    plt.show()

# Agregar clientes de ejemplo
agregar_cliente("Juan Pérez", "juan.perez@gmail.com", "123 Calle Falsa", "Tecnología")
agregar_cliente("Ana Gómez", "ana.gomez@example.com", "Calle 456", "Moda")
agregar_cliente("Luis Ramírez", "luis.ramirez@example.com", "Avenida Central 123", "Deportes")
agregar_cliente("Maria Fernanda López", "maria.lopez@example.com", "Calle 789", "Moda")
agregar_cliente("Carlos Méndez", "carlos.mendez@example.com", "Zona Industrial", "Tecnología")
agregar_cliente("Laura Sánchez", "laura.sanchez@example.com", "Calle Primavera 45", "Hogar")
agregar_cliente("Roberto Díaz", "roberto.diaz@example.com", "Boulevard Norte 321", "Deportes")
agregar_cliente("Gabriela Torres", "gabriela.torres@example.com", "Calle Oriente 56", "Tecnología")
agregar_cliente("Jorge Castillo", "jorge.castillo@example.com", "Av. Las Flores 33", "Gastronomía")
agregar_cliente("Elena Jiménez", "elena.jimenez@example.com", "Plaza del Sol", "Moda")
agregar_cliente("Sofía Martínez", "sofia.martinez@example.com", "Zona Sur", "Gastronomía")
agregar_cliente("Raúl Gómez", "raul.gomez@example.com", "Calle Sur 123", "Automotriz")

# Mostrar todos los clientes y la gráfica de preferencias al inicio
listar_clientes()
graficar_preferencias()

# Generar el informe completo de clientes sin filtros
buscar_clientes()

# Cierra la conexión al finalizar el programa
conn.close()
