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
- Supports for only 1 video track and 1 audio track
- Audio track must be in stereo

## Test Environment

- Python 3.8.2
- macOS Catalina 10.15.4 / AMD Radeon 5500m / Intel i9 
- ffmpeg version 4.2.2 Copyright (c) 2000-2019 the FFmpeg developers
  built with Apple clang version 11.0.0 (clang-1100.0.33.8)
  configuration: --enable-gpl --enable-version3 --enable-sdl2 --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libdav1d --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-appkit --enable-avfoundation --enable-coreimage --enable-audiotoolbox