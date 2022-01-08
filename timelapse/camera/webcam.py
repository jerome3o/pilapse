from logging import getLogger
from typing import Union
from pathlib import Path
from contextlib import contextmanager

import cv2

_logger = getLogger(__name__)


@contextmanager
def webcam():
    cap = cv2.VideoCapture(0)
    yield cap
    cap.release()
    cv2.destroyAllWindows()


def take_picture(file_path: Union[str, Path], buffer_frames: int = 20):

    with webcam() as cap:

        Path(file_path).parent.mkdir(exist_ok=True, parents=True)
        ret, frame = cap.read()  # return a single frame in variable `frame`

        if ret:
            cv2.imwrite(str(file_path), frame)
        else:
            _logger.error("Failed to take picture")


def main():
    take_picture("test.png")


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    main()
