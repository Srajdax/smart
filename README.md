# SMART

> *Project unstable*, work still on progress

SMART is a small script to enhance my productivity in encoding videos, it provides presets for encoding video/movies.

## Requirements

- ffmpeg and ffprobe (https://ffmpeg.org) installed and added to PATH
- python depencies, can be installed using `pip install -r requirements.txt`

## Usage

TODO

## Current limitations

- It is not possible to indicate custom parameters on the CLI, this tool is not designed and suited for this purpose as it will only be a wrapper for ffmpeg in the latter case.
- The script heavily rely on the ffmpeg/ffprobe version that you have installed and your workstation capability. Therefore presets such as hardware accelerated ones (e.g. NVIDIA, AMD) could not work on your computer.
