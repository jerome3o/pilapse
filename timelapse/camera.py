#!/usr/bin/env python

from typing import Union
from pathlib import Path
from datetime import datetime

from picamera import PiCamera

_camera = PiCamera()
_camera.resolution = (3280, 2464)


def take_picture(file_path: Union[str, Path]) -> None:
    file_path.parent.mkdir(exist_ok=True, parents=True)

    _camera.start_preview()
    _camera.capture(str(file_path))
    _camera.stop_preview()


def get_misc_picture_path() -> Path:
    return Path("pictures") / "testing_day_1" / f"test_{datetime.now():%Y-%m-%d_%H-%M-%S}.jpg"

def _main():
    take_picture(get_misc_picture_path())


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    _main()
