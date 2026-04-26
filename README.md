# 🛠️ Network Automation Toolkit

Colección de herramientas Python para automatización y seguridad de redes.
Combina conocimientos de CCNA, Python y seguridad informática.

---

## 📋 Proyecto 1 — Ping Monitor

### Objetivo
Construir una herramienta en Python que automatice el monitoreo de conectividad de red, verificando si una lista de hosts está activa o inactiva y guardando el historial en una base de datos.

### ¿Qué construimos?
Un script que hace ping a una lista de IPs y dominios, evalúa su estado y guarda los resultados con fecha y hora en SQLite.

### Módulos utilizados
- `subprocess` → ejecución de comandos de red
- `os` → detección del sistema operativo
- `sqlite3` → persistencia de datos
- `datetime` → registro temporal

---

## 🔍 Proyecto 2 — Port Scanner

### Objetivo
Construir un script que evalúe qué puertos están abiertos o cerrados en una IP, identificando los servicios disponibles y guardando el historial en una base de datos.

### ¿Qué construimos?
Un escáner de puertos que intenta conectarse a una lista de puertos conocidos, determina su estado y registra los resultados con fecha y hora en SQLite.

### Módulos utilizados
- `socket` → conexiones de red para escanear puertos
- `sqlite3` → persistencia de resultados en base de datos
- `datetime` → registro temporal de cada escaneo

### Importancia en seguridad
Permite identificar servicios expuestos en una red. Puertos abiertos innecesarios representan vulnerabilidades potenciales.

---

## Tecnologías
`Python 3.13` · `SQLite` · `socket` · `subprocess` · `os` · `datetime`