from fastapi import APIRouter, HTTPException
from fastapi_utils.tasks import repeat_every # pip install fastapi-utils

router = APIRouter()

cupos = {
        "GC": 10,
        "PO": 10
        }

# Función para reiniciar los cupos después de 10 segundos
@router.on_event("startup")
@repeat_every(seconds=60) 
def init_data():
	global cupos
	cupos["GC"] = 10
	cupos['PO'] = 10
	return cupos 

@router.post("/validador_cupos")
async def validador_cupos(data: dict):
	global cupos
	tipo = data.get("tipo")
    # Verificar si hay cupos disponibles
	if cupos["GC"]> 0 and tipo == "GC":
		cupos["GC"]-= 1
	elif cupos["PO"] > 0 and tipo == "PO":
		cupos["PO"] -= 1
	else:
		raise HTTPException(status_code=400, detail="0")
	
	correo = data.get("correo")
	
	return {"respuesta": "1", "correo": correo}