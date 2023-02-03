# timelapse

Run a Raspberry Pi with a camera to make time lapses

## Setup

```bash
# you may need to use virtualenv
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

## Running

After activating the virtual environment:

```bash
uvicorn --host 0.0.0.0 timelapse.server:app --reload
```

## Compiling into video

These are quick notes for manual testing

```
ffmpeg -r 60  -pattern_type glob -i '*.jpg' -y video.mp4

ffmpeg -i video.mp4 -vf "transpose=2" video2.mp4
```

