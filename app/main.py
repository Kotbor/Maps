from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from .Parser import GetJsonList
import os
import uvicorn

path = os.getcwd() 
filename = "files\\2.xlsx"

xlfile = os.path.join(path, filename)


app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_root():
    response = RedirectResponse(url='static/index.html')
    return response

@app.get("/2")
def read_root():
    response = RedirectResponse(url='static/index2.html')
    return response


@app.get('/deliveries')
def deliveriels():
    response = GetJsonList(xlfile)
    return {"data": response[:10]}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)