from fastapi import FastAPI
from routers import cupos

app = FastAPI()

app.include_router(cupos.router)

@app.get("/")
async def cupos_disponibles():
    return {"total": 10}
	
