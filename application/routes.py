from application import app
from flask import render_template
from application import utils
from application.forms import SearchForm
import yt_dlp 


@app.route('/', methods=["GET", "POST"])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        search = form.query.data
        response = utils.getSearches(search)
        return render_template("home.html", title="Home", items=response, form=form)
    return render_template("home.html", title="Home", form=form)


@app.route('/download/<link>')
def download(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '~/Downloads/yt-mp3-output/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"{link}"])
    return ('', 204)
