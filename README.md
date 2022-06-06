# Youtube to MP3 Converter

Application to make converting youtube to mp3 easier. Search and download mp3 for videos, all in one place. Made with `flask`.

## Disclaimer

Downloading the mp3 for videos that you do not have persmission to download (which is most of them) is **a direct violation of Youtube's Terms and Condition, sometimes illegal**. Do **NOT** use this application for doing this. I am **not responsible** for your actions if you decide to use this application. This application was intended to make downloading content which the owner of the video has _specifically said_ you can download (such as royalty free music) easier to download. I expect end users to use it for the same, thereby adhering to YouTube's policies.

## Dependencies

This application requires:

- Docker: a guide to install docker can be found [here](https://docs.docker.com/get-docker/)
  - If you are using Linux, you may have to install `docker-compose` manually, which is also a dependency for this to work properly. Guide can be found [here](https://docs.docker.com/compose/install/compose-plugin/#installing-compose-on-linux-systems)

## Build and Setup (One Time)

1. Open a new terminal and clone this repository using the following command:

```
git clone https://github.com/pranavrao145/youtube-to-mp3-converter
```

2. Change in to the project folder.

```
cd youtube-to-mp3-converter
```

3. Create and configure your Youtube API key (required to use this app).

- Go to [this page](https://console.developers.google.com/apis/credentials), signing in with your Google account if necessary.
- Create a project
  - If you haven't used this console before, click the New Project button on the right.
  - If you have used this console before, create a new project by clicking the current project name in the top left, then clicking New Project in the top right.
- Give your project a name, no organization is necessary.
  - If you have used the Google Console API before, you may have to switch to your new project manually in the top left of your screen (same place as New Project button).
- On the top left, click the Create Credentials, click API key, and copy the key on the screen.
- Go to where you cloned the folder, and edit the `sample.env file`, inserting your token where it says `your_token_here`.
- Rename `sample.env` to `.env`

4. In the terminal, use the following command to build the app:

```
docker-compose build
```

## Running the App (Each Time)

You can run the app by first opening a new terminal and changing into the project folder:

```
cd youtube-to-mp3-converter
```

Then run this command to actually run the app:

```
docker-compose up
```

## Using the App

Navigate to `localhost:6969` in your browser to use the app. To download a
video, search for the video in the search bar and hit `Download`. There is no
confirmation message, so you can just hit `Download` and move on to the next
video, doing multiple at a time. You can view progress in the terminal you ran
the app from. Any video is FINISHED downloading if you see a message in the
terminal like: `Deleting original file: <video-name>...`. If you download
multiple things at once, you should see this message for the LAST video you
downloaded, at which point you can safely assume all videos have been
downloaded successfully.

If you ever run into a `Forbidden` error, simply reload the page and
re-download the song that caused the error.

Any and all downloads will go to your `Downloads/yt-mp3-output` folder in the
home directory.

When done downloading songs, use `Control/Command+C` to exit the server in the
terminal.

## Updating

It is recommended to update the app every once in a while by opening a terminal
in the project folder and running the following command:

```
git pull origin master
```
