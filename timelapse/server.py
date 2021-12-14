import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from apscheduler.schedulers.background import BackgroundScheduler

from timelapse.camera import get_misc_picture_path, take_picture

_logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler()

# TODO: enable webbased configuration of timelapses

app = FastAPI()
app.mount("/pictures", StaticFiles(directory="pictures"), name="pictures")


@app.get("/take")
def take():
    path = get_misc_picture_path()
    _logger.info(f"Taking picture {path}")
    take_picture(path)
    return RedirectResponse(f'/{path.resolve().relative_to(Path(".").resolve())}')


@app.get("/list")
def list_pictures():
    return [str(p) for p in Path("pictures").rglob("*.jpg")]


scheduler.add_job(take, "interval", minutes=1)
scheduler.start()
logging.basicConfig(level=logging.INFO)
