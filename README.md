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