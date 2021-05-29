from application import app
from flask import render_template, redirect, flash
from application import utils
from application.forms import SearchForm
import youtube_dl

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
            'outtmpl': '~/Downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"{link}"])
    flash("Video downloaded successfully. Check your Downloads folder.", "success")
    return redirect('/')

