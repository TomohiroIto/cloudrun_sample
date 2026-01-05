from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


class UserName(BaseModel):
    userName: str

app = FastAPI()

@app.get("/")
async def hello():
    return JSONResponse(content={'res': f'Hello, world'}, status_code=200)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info")
