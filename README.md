# Timelapse Script for RPi

This repo contains a script `main.py` that takes a picture every N seconds, and saves it to the `images/` directory.

## Setup

Setup and activate venv

```sh
python -m venv venv
. venv/bin/activate
```

## Run

```sh
python main.py 
```

## Deployment

I've just been running this with tmux and ssh. Here are some quick steps

* SSH into the Raspberry Pi `ssh rpi` (or whatever hostname it's got)
* Install tmux if needed `sudo apt install tmux` (for ubuntu/raspian)
* Open a tmux session: `tmux`
* Setup the repo if you haven't already
* Start the script with `python main.py`
* Detach from the tmux session (ctrl+b d)
* Exit the ssh session

Voila!
