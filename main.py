from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from core.units import Q_, convert_units

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    flow = Q_(1, 'meter ** 3 / second')
    flow = convert_units(flow, 'gallon / minute')
    return templates.TemplateResponse("home.html", {"request": request, "css": "home.css", "flow": flow})
