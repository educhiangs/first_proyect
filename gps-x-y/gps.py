import re

def parse_gps(gps_string):
    # Extrae todos los números (enteros o decimales)
    numbers = re.findall(r"(\d+\.?\d*)", gps_string)
    # Busca la letra de dirección (N, S, E, W) sin guiones problemáticos
    direction = re.findall(r"[NSEWnsew]", gps_string)
    
    if len(numbers) < 3 or not direction:
        raise ValueError("No se encontraron suficientes datos (grados, minutos, segundos o dirección).")
    
    degrees = float(numbers[0])
    minutes = float(numbers[1])
    seconds = float(numbers[2])
    dir_letter = direction[-1].upper()
    
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if dir_letter in ['S', 'W']:
        decimal *= -1
    return decimal

print("--- Conversor GPS a Google Maps ---")
print("Copia y pega la línea completa de ExifTool:\n")

try:
    lat_input = input("Latitud: ")
    lon_input = input("Longitud: ")

    lat = parse_gps(lat_input)
    lon = parse_gps(lon_input)
    
    url = f"https://google.com{lat:.6f},{lon:.6f}"
    
    print(f"\nDecimal: {lat:.6f}, {lon:.6f}")
    print("Abriendo Google Maps...")

except Exception as e:
    print(f"\nError: {e}")

input("\nPresiona Enter para cerrar...")
