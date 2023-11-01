from fastapi_utils.tasks import repeat_every 
from fastapi import APIRouter, HTTPException
import random

router = APIRouter()

cupos = {
        "GC": 10,
        "PO": 10
        }

# Función para reiniciar los cupos después de 60 segundos
@router.on_event("startup")
@repeat_every(seconds=3600) 
def init_data():
	global cupos
	cupos["GC"] = 10
	cupos['PO'] = 10
	return cupos 

@router.post("/validador_cupos")
async def validador_cupos(data: dict):
	global cupos
	numero_aleatorio = random.randint(1, 20)
	tipo = data.get("tipo")
    # Verificar si hay cupos disponibles
	if cupos["GC"]> 0 and tipo == "GC" and numero_aleatorio == 20:
		cupos["GC"]-= 1
	elif cupos["PO"] > 0 and tipo == "PO" and numero_aleatorio == 20:
		cupos["PO"] -= 1
	else:
		raise HTTPException(status_code=400, detail="0")
	
	correo = data.get("correo")
	
	return {"respuesta": "1", "correo": correo}