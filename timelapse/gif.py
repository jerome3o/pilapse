import logging

from pathlib import Path
from typing import List
from PIL import Image


_logger = logging.getLogger(__file__)


# TODO: integrate with service


def main():
    # create_gif_for_session("misc", fps=5)
    create_gif_for_session("testing_day_1", fps=30)


def create_gif_for_session(session: str, fps: float = 60):

    files = list((Path("pictures") / session).glob("*.jpg"))
    file_out = Path("outputs") / f"{session}.gif"

    create_gif_from_files(
        files=files[::5],
        file_out=file_out,
        fps=fps,
    )


def create_gif_from_files(files: List[Path], file_out: Path, fps: int = 60):
    _logger.info("Loading images")
    imgs = [Image.open(f) for f in sorted(files)]
    n_frames = len(imgs)

    _logger.info("Rotating images")
    img, *imgs = [i.resize((x // 4 for x in i.size)).rotate(90) for i in imgs]

    _logger.info("Saving GIF")
    img.save(
        fp=file_out,
        format="GIF",
        append_images=imgs,
        save_all=True,
        loop=0,
        duration=n_frames / fps,
    )
    _logger.info("Done!")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
