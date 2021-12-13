#!/usr/bin/env python

from typing import Union
from pathlib import Path
from datetime import datetime

from picamera import PiCamera

_camera = PiCamera()
_camera.resolution = (3280, 2464)


def take_picture(file_path: Union[str, Path]) -> None:
    _camera.start_preview()
    _camera.capture(str(file_path))
    _camera.stop_preview()


def main():
    take_picture(Path("pictures") / f"test_{datetime.now():%Y-%m-%d_%H-%M-%S}.jpg")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
