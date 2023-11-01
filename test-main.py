import requests
import concurrent.futures

url = "http://127.0.0.1:8000/validador_cupos"

def realizar_solicitud(i):
    response = requests.post(url, json={"correo": f"usuario{i}@ejemplo.com", "tipo": "PO"})
    print(f"Solicitud {i}: {response.status_code}")

# Número total de solicitudes
total_solicitudes = 100

# Realizar solicitudes de forma concurrente
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(realizar_solicitud, range(total_solicitudes))