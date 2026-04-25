import subprocess # ejecuta comandos externos desde Python
import os         # detecta el sistema operativo (Windows/Linux/Mac)
import sqlite3    # maneja la base de datos local
import datetime   # genera fecha y hora actual

# lista de hosts a monitorear
hosts = [
    "8.8.8.8",    # Google DNS
    "1.1.1.1",    # Cloudflare DNS
    "127.0.0.1",  # loopback - tu propia PC
    "google.com", # dominio real
]

# detectamos el OS para usar el comando correcto
if os.name == "nt":
    comando = "ping -n 1" # Windows: -n cantidad de paquetes
else:
    comando = "ping -c 1" # Linux/Mac: -c cantidad de paquetes

# creamos o conectamos la base de datos
conn = sqlite3.connect("ping_monitor.sqlite")
cursor = conn.cursor() # intermediario para ejecutar comandos SQL

# creamos la tabla solo si no existe para no sobreescribir datos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS resultados (
        id INTEGER PRIMARY KEY AUTOINCREMENT, # id único automático
        host TEXT,                            # IP o dominio consultado
        estado TEXT,                          # ACTIVO o INACTIVO
        fecha TEXT                            # fecha y hora del ping
    )
""")
conn.commit() # confirmamos la creación de la tabla

# recorremos cada host de la lista
for p in hosts:
    resultado = subprocess.run(
        f"{comando} {p}",    # armamos el comando: ping -n 1 8.8.8.8
        capture_output=True, # capturamos la salida sin mostrarla
        shell=True           # ejecutamos en la terminal del sistema
    )

    # evaluamos el resultado del ping
    if resultado.returncode == 0:  # 0 = comando exitoso
        estado = "ACTIVO ✅"
    else:                          # 1 = comando fallido
        estado = "INACTIVO ❌"

    print(p, estado) # mostramos resultado en consola

    # obtenemos fecha y hora actual en formato legible
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # insertamos el resultado en la base de datos
    # NULL → SQLite genera el id automáticamente
    cursor.execute(
        "INSERT INTO resultados VALUES (NULL, ?, ?, ?)",
        (p, estado, fecha) # valores seguros, previene inyección SQL
    )
    conn.commit() # guardamos cada resultado inmediatamente

# mostramos el historial completo guardado en la BD
print("\n--- HISTORIAL DE RESULTADOS ---")
cursor.execute("SELECT * FROM resultados") # traemos todos los registros
registros = cursor.fetchall()              # los guardamos en una lista

for registro in registros: # recorremos e imprimimos cada registro
    print(registro)

conn.close() # cerramos la conexión correctamente