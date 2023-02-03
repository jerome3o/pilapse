import logging
from pathlib import Path
from collections import defaultdict

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from apscheduler.schedulers.background import BackgroundScheduler
from starlette.responses import HTMLResponse

from timelapse.settings import CameraType, Settings
from timelapse.utils import get_time_str

_logger = logging.getLogger(__name__)
# scheduler = BackgroundScheduler()
settings = Settings()

# To avoid picam imports breaking on non rpi machines. TODO: specify platform specific requirements.txt
if settings.camera_type == CameraType.PICAM:
    from timelapse.camera.picam import take_picture
elif settings.camera_type == CameraType.WEBCAM:
    from timelapse.camera.webcam import take_picture


# TODO: enable webbased configuration of timelapses

app = FastAPI()
app.mount(
    "/pictures",
    StaticFiles(directory=settings.picture_path),
    name="pictures"
)
templates = Jinja2Templates(directory="templates")


@app.get("/snap", response_class=HTMLResponse)
def take(request: Request):
    path = Path(f"pictures/snaps/snap_{get_time_str()}.png")
    _logger.info(f"Taking picture {path}")
    take_picture(path)
    path = f'/{path.resolve().relative_to(Path(".").resolve())}'

    return templates.TemplateResponse("snap.html", {"p": path, "request": request})


@app.get("/list")
def list_pictures(request: Request):
    all_pics = [p for p in Path(settings.picture_path).rglob("*.png")]
    collections = defaultdict(list)
    for p in all_pics:
        collections[p.parts[-2]].append(p)

    return templates.TemplateResponse("list.html", {"pictures": collections, "request": request})


# scheduler.add_job(take, "interval", minutes=1)
# scheduler.start()
logging.basicConfig(level=logging.INFO)
