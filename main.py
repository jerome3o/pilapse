import picamera
from datetime import datetime
from time import sleep
import shutil
import os

# Sleep time in seconds
_SLEEP_TIME = 10

def _take_picture():
    try:
        date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        picture_str = f'images/image_{date_str}.jpg'
        latest_str = 'images/image_latest.jpg'

        print(f"Taking picture: {picture_str}")

        os.system(f"raspistill --output {picture_str}")
        shutil.copy(picture_str, latest_str)

    #    camera = picamera.PiCamera()
    #    camera.capture(latest_str)
    #    camera.capture(picture_str)
    #    camera.close()
    except Exception:
        pass


def main():
    while True:
        _take_picture()
        sleep(_SLEEP_TIME)

if __name__ == "__main__":
    main()
