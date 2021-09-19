from typing import Optional

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_root():
    response = RedirectResponse(url='static/index.html')
    return response

