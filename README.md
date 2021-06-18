# Youtube to MP3 Converter
Application to make converting youtube to mp3 easier. Search and download mp3 for videos, all in one place. Made with `flask` and `flaskwebgui`.

## Disclaimer
Downloading the mp3 for videos that you do not have persmission to download (which is most of them) is **a direct violation of Youtube's Terms and Condition, sometimes illegal**. Do **NOT** use this application for doing this. I am **not responsible** for your actions if you decide to use this application. This application was intended to make downloading content which the owner of the video has *specifically said* you can download (such as royalty free music) easier to download. I expect end users to use it for the same, thereby adhering to YouTube's policies.

## Dependencies
This application requires:
* FFmpeg: to use this application, install it on your system, and ensure it is added to PATH.
* Google Chrome or Chromium

## Build
### Windows
* Clone the repository
* Create a .env file with a 16-character SECRET_KEY variable and a YOUTUBE_API_TOKEN variable containing a Youtube Data API Key.
* Run `pipenv shell` (or source whatever venv you are using)
* Run `pipenv install` (alternatively you can use `pip install -r requirements.txt`, but pipenv is recommended)
* Run `pyinstaller -w -F --add-data "application;application" run.py -n "Youtube to MP3 Converter"`

### MacOS/Linux
* Clone the repository
* Create a .env file with a 16-character SECRET_KEY variable and a YOUTUBE_API_TOKEN variable containing a Youtube Data API Key.
* Run `pipenv shell` (or source whatever venv you are using)
* Run `pipenv install` (alternatively you can use `pip3 install -r requirements.txt`, but pipenv is recommended)
* Run `pyinstaller -w -F --add-data "application:application" run.py -n "Youtube to MP3 Converter"`

## Run
* If you build using the instructiosn above, the executable will be under `{Project Root}\dist\'`
  * For Windows: Clicking on the .exe should open it
  * For MacOS/Linux: Clicking may work, but recommended to run it from the terminal (`./Youtube\ to\ MP3\ Converter`)
