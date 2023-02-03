#!/usr/bin/env python

from typing import Union
from pathlib import Path

from picamera import PiCamera

_camera = PiCamera()
_camera.resolution = (3280, 2464)


def take_picture(file_path: Union[str, Path]) -> None:
    file_path.parent.mkdir(exist_ok=True, parents=True)

    _camera.start_preview()
    _camera.capture(str(file_path))
    _camera.stop_preview()
