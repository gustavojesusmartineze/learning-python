from datetime import datetime, timedelta

# Fecha y hora actual
now = datetime.now()
print(now)

# Fecha de hoy
today = datetime.today()
print(today)

# fecha de otro dia 
specific_date = datetime(2025, 10, 9)
print(f"Fecha específica: {specific_date}")

# formatear fechas
formatted_date = specific_date.strftime("%d/%m/%Y")
print(f"Fecha formateada: {formatted_date}")


# formatear fechas
formatted_date = specific_date.strftime("%d/%m/%y")
print(f"Fecha formateada: {formatted_date}")


# formatear fecha con hora
formatted_date_time = now.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha y hora formateada: {formatted_date_time}")


# 4. Operaciones con fechas (sumar/restar dias, minutos, segundos, horas, meses)
yesterday = now - timedelta(days=1)
print(f"Ayer: {yesterday}")

# sumar 10 dias
ten_days_later = now + timedelta(days=10)
print(f"Dentro de 10 días: {ten_days_later}")

# restar 10 dias
ten_days_ago = now - timedelta(days=10)
print(f"Hace 10 días: {ten_days_ago}")

year = now.year
month = now.month
day = now.day

print(f"Año: {year}, Mes: {month}, Día: {day}")

# 5. Comparar fechas
if now > specific_date:
  print("La fecha actual es mayor a la fecha específica")
else:
  print("La fecha actual es menor a la fecha específica")



  # 5. Obtener componentes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# 6. Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2025, 2, 12, 15, 30, 0)
difference = date2 - date1
print(f"Diferencia entre las fechas: {difference}")