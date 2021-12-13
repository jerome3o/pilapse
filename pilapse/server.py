from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

from pilapse.camera import get_misc_picture_path, take_picture


app = FastAPI()
app.mount("/pictures", StaticFiles(directory="pictures"), name="pictures")


@app.get("/take")
def take():
    path = get_misc_picture_path()
    take_picture(path)
    return RedirectResponse(f'/{path.resolve().relative_to(Path(".").resolve())}')


@app.get("/list")
def list_pictures():
    return [str(p) for p in Path("pictures").rglob("*.jpg")]


scheduler.add_job(take, "interval", minutes=1)
