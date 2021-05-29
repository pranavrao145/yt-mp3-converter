# Youtube to MP3 Converter
Application to make converting youtube to mp3 easier. Search and download mp3 for videos, all in one place.

## Dependencies
This application requires:
* FFmpeg: to use this application, install it on your system, and ensure it is added to PATH.
* Google Chrome or Chromium

## Build
To build this on Windows (pyinstaller):
* Clone the repository
* Run `pyinstaller -w -F --add-data "application;application" run.py -n "Youtube to MP3 Converter"`

To build this on MacOS/Linux (pyinstaller)
* Clone the repository
* Run `pyinstaller -w -F --add-data "application:application" run.py -n "Youtube to MP3 Converter"`
