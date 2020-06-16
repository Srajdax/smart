# SMART version 0.3

SMART is a small script to enhance my productivity in encoding videos, it provides presets for encoding video/movies.

[CHANGELOG](CHANGELOG.md)

- [SMART version 0.3](#smart-version-03)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Current limitations](#current-limitations)
  - [Test Environment](#test-environment)


> *Project unstable*, work still on progress


## Requirements

- ffmpeg and ffprobe (https://ffmpeg.org) installed and added to PATH
- python depencies, can be installed using `pip install -r requirements.txt`

## Usage

```
usage: smart.py [-h] -i INPUT [-l] [-c CONFIG] [-p PRESET] [-v VIDEO] [-a AUDIO] [-yuv {420-8,420-10,422-8,422-10,444-8,444-10}]
                [-r {360,480,720,1080,2160,native} [{360,480,720,1080,2160,native} ...]] [-m {mp4,mkv,mov}] [-o OUTPUT]

SMART - a simple script to ease and automate video encoding

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The input file to be encoded
  -l, --list-preset     List all the presets available
  -c CONFIG, --config CONFIG
                        The .yaml configuration file for the presets, default file 'configuration.yaml' in the current directory
  -p PRESET, --preset PRESET
                        Select a global preset
  -v VIDEO, --video VIDEO
                        Select a video preset, default is 'x264-fast-crf'
  -a AUDIO, --audio AUDIO
                        Select an audio preset, default is 'aac-256'
  -yuv {420-8,420-10,422-8,422-10,444-8,444-10}, --chroma-subsampling {420-8,420-10,422-8,422-10,444-8,444-10}
                        Select the chroma subsampling and the bit depth, supports [420-8, 420-10, 422-8, 422-10, 444-8, 444-10], default is
                        '420-8'
  -r {360,480,720,1080,2160,native} [{360,480,720,1080,2160,native} ...], --resize {360,480,720,1080,2160,native} [{360,480,720,1080,2160,native} ...]
                        Provide a list to resize the video and output it in multiple size
  -m {mp4,mkv,mov}, --mux {mp4,mkv,mov}
                        Select container for the encoded file (available: mp4, mov, mkv), default is 'mp4'
  -o OUTPUT, --output OUTPUT
                        The output name of the encoded file, default name 'output'
```

## Current limitations

- It is not possible to indicate custom parameters on the CLI, this tool is not designed and suited for this purpose as it will only be a wrapper for ffmpeg in the latter case.
- The script heavily rely on the ffmpeg/ffprobe version that you have installed and your workstation capability. Therefore presets such as hardware accelerated ones (e.g. NVIDIA, AMD) could not work on your computer.
- Supports for only 1 video track and 1 audio track
- Audio track must be in stereo

## Test Environment

- Python 3.8.2
- macOS Catalina 10.15.5 / AMD Radeon 5500m / Intel i9 
- ffmpeg version 4.2.2 Copyright (c) 2000-2019 the FFmpeg developers
  built with Apple clang version 11.0.0 (clang-1100.0.33.8)
  configuration: --enable-gpl --enable-version3 --enable-sdl2 --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libdav1d --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-appkit --enable-avfoundation --enable-coreimage --enable-audiotoolbox