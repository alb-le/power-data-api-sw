from fastapi import FastAPI
import uvicorn
from mangum import Mangum

from app.routes.basic_routes import router

app = FastAPI()
app.include_router(router)
handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
