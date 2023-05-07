from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
app = FastAPI()
current_dir=os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=f"{current_dir}/pages/static"), name="static")
templates = Jinja2Templates(directory= f"{current_dir}/pages")
@app.get("/")
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/bye")
def read_bye_page(request: Request):
    return templates.TemplateResponse("bye.html", {"request": request})