from datetime import datetime, timedelta 

# Obtener la fecha, hora, minutos, segundos, microsegundos actual
now = datetime.now()
print(now)

# Crear una fecha y hora especifica
# Si no especificas un valor, por defecto pone todos 0 
specific_date = datetime(2025, 2, 10, 8)
print(specific_date)

# Formatear fechas 
# metodo strftime() para formatear fechas 
# pasarle el objeto datetime y el formato especificado
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

format_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

# Operaciones con fechas (sumar/restar dias, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

# Obtener componentes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2025, 2, 12, 15, 30, 0)
difference = date2 - date1
print(f"Diferencia entre las fechas: {difference}")