from enum import Enum
from pydantic import BaseSettings, Field


class CameraType(Enum):
    WEBCAM = "webcam"
    PICAM = "picam"


class Settings(BaseSettings):
    camera_type: CameraType = Field(
        default=CameraType.WEBCAM,
        env='CAMERA_TYPE',
    )
    picture_path: str = Field(default="./pictures", env="PICTURE_PATH")
