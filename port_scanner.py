import socket    # conexiones de red para escanear puertos
import sqlite3   # guardar resultados en base de datos
import datetime  # registrar fecha y hora del escaneo

ip = "127.0.0.1"  # IP a escanear, usamos el loopback para probar

puertos = [
    22,    # SSH
    80,    # HTTP
    443,   # HTTPS
    3389   # RDP
]

conn = sqlite3.connect("port_scanner.sqlite")  # creamos o conectamos la base de datos
cursor = conn.cursor()                          # intermediario entre Python y SQLite

cursor.execute("""
    CREATE TABLE IF NOT EXISTS resultados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        ip TEXT,                               
        puerto TEXT,                           
        estado TEXT,                           
        fecha TEXT                             
    )
""")                                           # creamos la tabla si no existe
conn.commit()                                  # confirmamos la creación

for puerto in puertos:                         # recorremos cada puerto de la lista
    try:                                       # intentamos conectarnos al puerto
        socket.create_connection((ip, puerto), timeout=1)  # conexión con 1 seg de espera
        estado = "ABIERTO "                  # si conecta → puerto abierto
    except:                                    # si falla la conexión
        estado = "CERRADO "                  # puerto cerrado

    print(ip, puerto, estado)                  # mostramos resultado en consola

    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # fecha y hora actual

    cursor.execute(
        "INSERT INTO resultados VALUES (NULL, ?, ?, ?, ?)",  # insertamos en la tabla
        (ip, puerto, estado, fecha)                          # los 4 valores seguros
    )
    conn.commit()                              # guardamos cada resultado

print("\n--- HISTORIAL DE RESULTADOS ---")     # título del historial
cursor.execute("SELECT * FROM resultados")     # traemos todos los registros
registros = cursor.fetchall()                  # los guardamos en una lista

for registro in registros:                     # recorremos e imprimimos cada registro
    print(registro)

conn.close()                                   # cerramos la conexión correctamente