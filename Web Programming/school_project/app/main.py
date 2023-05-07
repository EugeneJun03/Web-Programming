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
    return templates.TemplateResponse("main_page.html", {"request": request})
    
@app.get("/1st")
def read_bye_page(request: Request):
    return templates.TemplateResponse("1st.html", {"request": request})
@app.get("/2nd")
def read_bye_page(request: Request):
    return templates.TemplateResponse("2nd.html", {"request": request})
@app.get("/3rd")
def read_bye_page(request: Request):
    return templates.TemplateResponse("3rd.html", {"request": request})
@app.get("/4th")
def read_bye_page(request: Request):
    return templates.TemplateResponse("4th.html", {"request": request})

@app.get("/study_time")
def read_index(request: Request):
    return templates.TemplateResponse("study_time.html", {"request": request})

@app.get("/ranking")
def read_index(request: Request):
    return templates.TemplateResponse("time_rank.html", {"request": request})

@app.get("/personal")
def read_index(request: Request):
    return templates.TemplateResponse("personal.html", {"request": request})