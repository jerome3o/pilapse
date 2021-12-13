#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
from datetime import datetime


def main():
    camera = PiCamera()
    camera.resolution = (3280, 2464)
    camera.start_preview()
    sleep(1)

    file_dir = './pictures'

    now = datetime.now()

    dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = 'test' + dt_string + '.jpg'

    file_path = file_dir + file_name
    camera.capture(file_path)
    camera.stop_preview()


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    main()