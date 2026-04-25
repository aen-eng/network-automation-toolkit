# Informe — Ping Monitor

## Objetivo

Construir una herramienta en Python que automatice el monitoreo de conectividad de red, verificando si una lista de hosts está activa o inactiva y guardando el historial en una base de datos.

## ¿Qué construimos?

Un script que hace ping a una lista de IPs y dominios, evalúa su estado y guarda los resultados con fecha y hora en SQLite.

## Tecnologías aplicadas

- `subprocess` → ejecución de comandos de red
- `os` → detección del sistema operativo
- `sqlite3` → persistencia de datos
- `datetime` → registro temporal

## Meta

Este proyecto es el primer paso del **Network Automation Toolkit**, una herramienta orientada a automatizar tareas reales de monitoreo y seguridad de redes, combinando conocimientos de Python, CCNA y seguridad informática.